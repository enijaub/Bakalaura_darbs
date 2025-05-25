import time
import psycopg2

DB_NAME = 'power_data'
DB_USER = 'admin'
DB_PASSWORD = 'pass'
DB_HOST = 'localhost'
DB_PORT = 5432
TABLE_NAME = 'electricity'
OUTPUT_FILE = 'postgresql_results5_filter_time.txt'
REPEAT_COUNT = 100

with open(OUTPUT_FILE, 'w') as out:
    out.write(f"{REPEAT_COUNT} atkartojums | Pilnas tabulas izgusana no '{TABLE_NAME}'\n\n")

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

        start = time.perf_counter()
        cur.execute(f"""
            SELECT * FROM {TABLE_NAME}
            WHERE time >= '2007-02-01' AND time < '2007-02-08';
        """)

        rows = cur.fetchall()
        end = time.perf_counter()
        duration = end - start

        print(f"{len(rows)} ieraksti izguti | Laiks: {duration:.2f} s")
        out.write(f"Atkartojums {run}: {len(rows)} ieraksti | Laiks: {duration:.2f} s\n")

        cur.close()
        conn.close()

print(f"\nRezultati saglabāti: {OUTPUT_FILE}")