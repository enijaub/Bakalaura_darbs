import csv
import time
from influxdb import InfluxDBClient

DB_NAME = 'test3_power_data'
MEASUREMENT = 'electricity'
INPUT_FILE = 'household_power_consumption.txt'
OUTPUT_FILE = 'influxdb_results3_batch100.txt'
BATCH_SIZE = 100
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

        fields = {}
        for key in ['Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity',
                    'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']:
            val = row.get(key, '').strip()
            if val in ('', '?'):
                continue
            try:
                fields[key] = float(val.replace(',', '.'))
            except ValueError:
                continue

        if len(fields) == 7:
            point = {
                "measurement": MEASUREMENT,
                "time": iso_time,
                "fields": fields
            }
            rows.append(point)

read_end = time.perf_counter()
read_time = read_end - read_start
print(f"Dati ieladeti ({len(rows)} rindu) | Lasisanas laiks: {read_time:.2f} s")

with open(OUTPUT_FILE, 'w') as out:
    out.write(f"Atskaite: {REPEAT_COUNT} atkartojumi | BATCH_SIZE = {BATCH_SIZE}\n")
    out.write(f"Datu punktu skaits: {len(rows)} | Faila nolasisana: {read_time:.2f} s\n\n")

    for run in range(1, REPEAT_COUNT + 1):
        print(f"\nAtkartojums {run}/{REPEAT_COUNT}")

        client = InfluxDBClient(host='localhost', port=8086)
        try:
            client.drop_database(DB_NAME)
        except:
            pass
        client.create_database(DB_NAME)
        client.switch_database(DB_NAME)

        write_start = time.perf_counter()
        inserted = 0

        for i in range(0, len(rows), BATCH_SIZE):
            batch = rows[i:i + BATCH_SIZE]
            try:
                client.write_points(batch)
                inserted += len(batch)
            except Exception as e:
                print(f"Kluda pie {inserted}: {e}")

        write_end = time.perf_counter()
        write_time = write_end - write_start

        print(f"{inserted} punkti rakstiti | Rakstisanas laiks: {write_time:.2f} s")
        out.write(f"Atkartojums {run}: Rakstisana {write_time:.2f} s\n")

print(f"\nVisi {REPEAT_COUNT} atkartojumi pabeigti")
print(f"Rezultati saglabati: {OUTPUT_FILE}")