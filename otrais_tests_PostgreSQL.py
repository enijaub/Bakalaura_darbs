import csv
import time
import psycopg2

DB_NAME = 'power_data'
DB_USER = 'admin'
DB_PASSWORD = 'pass'
DB_HOST = 'localhost'
DB_PORT = 5432
TABLE_NAME = 'electricity'
INPUT_FILE = 'household_power_consumption.txt'
OUTPUT_FILE = 'postgresql_results2_batch50.txt'
BATCH_SIZE = 50
REPEAT_COUNT = 25

print("Datu ielade")
read_start = time.perf_counter()
rows = []

with open(INPUT_FILE, 'r') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        date_str = row['Date']
        time_str = row['Time']
        try:
            timestamp = time.strptime(date_str + ' ' + time_str, '%d/%m/%Y %H:%M:%S')
            iso_time = time.strftime('%Y-%m-%dT%H:%M:%S', timestamp)
        except ValueError:
            continue
        try:
            values = (
                iso_time,
                float(row['Global_active_power'].strip().replace(',', '.')),
                float(row['Global_reactive_power'].strip().replace(',', '.')),
                float(row['Voltage'].strip().replace(',', '.')),
                float(row['Global_intensity'].strip().replace(',', '.')),
                float(row['Sub_metering_1'].strip().replace(',', '.')),
                float(row['Sub_metering_2'].strip().replace(',', '.')),
                float(row['Sub_metering_3'].strip().replace(',', '.')),
            )
            rows.append(values)
        except (ValueError, KeyError):
            continue

read_end = time.perf_counter()
read_time = read_end - read_start
print(f"Dati ieladeti ({len(rows)} rindu) | Lasisana: {read_time:.2f} s")

with open(OUTPUT_FILE, 'w') as out:
    out.write(f"{REPEAT_COUNT} atkartojumi | BATCH_SIZE = {BATCH_SIZE}\n")
    out.write(f"Datu punktu skaits: {len(rows)} | Faila nolasisana: {read_time:.2f} s\n\n")

    for run in range(1, REPEAT_COUNT + 1):
        print(f"Atkartojums {run}/{REPEAT_COUNT}")
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        cur.execute(f"DROP TABLE IF EXISTS {TABLE_NAME};")
        cur.execute(f"""
            CREATE TABLE {TABLE_NAME} (
                time TIMESTAMPTZ NOT NULL,
                global_active_power DOUBLE PRECISION,
                global_reactive_power DOUBLE PRECISION,
                voltage DOUBLE PRECISION,
                global_intensity DOUBLE PRECISION,
                sub_metering_1 DOUBLE PRECISION,
                sub_metering_2 DOUBLE PRECISION,
                sub_metering_3 DOUBLE PRECISION
            );
        """)
        conn.commit()

        write_start = time.perf_counter()
        inserted = 0

        for i in range(0, len(rows), BATCH_SIZE):
            batch = rows[i:i + BATCH_SIZE]
            try:
                cur.executemany(
                    f"""
                    INSERT INTO {TABLE_NAME} (
                        time, global_active_power, global_reactive_power, voltage, global_intensity,
                        sub_metering_1, sub_metering_2, sub_metering_3
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                    """,
                    batch
                )
                inserted += len(batch)
            except Exception as e:
                print(f"Kluda rakstot pie {inserted}: {e}")

        conn.commit()
        write_end = time.perf_counter()
        write_time = write_end - write_start

        print(f"{inserted} ieraksti | Rakstisana: {write_time:.2f} s")
        out.write(f"Atkartojums {run}: Rakstisana {write_time:.2f} s\n")

        cur.close()
        conn.close()

print(f"Visi {REPEAT_COUNT} atkartojumi pabeigti")
print(f"Rezultati saglabati: {OUTPUT_FILE}")