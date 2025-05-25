import time
import psycopg2

DB_NAME = 'power_data'
DB_USER = 'admin'
DB_PASSWORD = 'pass'
DB_HOST = 'localhost'
DB_PORT = 5432
TABLE_NAME = 'electricity'
OUTPUT_FILE = 'postgresql_results7_agreg.txt'
REPEAT_COUNT = 100

with open(OUTPUT_FILE, 'w') as out:
    out.write(f"{REPEAT_COUNT} atkartojums | Agregatvaicajums: AVG(global_active_power)\n\n")

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
            SELECT AVG(global_active_power)
            FROM {TABLE_NAME};
        """)
        result = cur.fetchone()
        end = time.perf_counter()
        duration = end - start

        avg_value = result[0]

        print(f"Videja vertiba: {avg_value:.4f} | Laiks: {duration:.2f} s")
        out.write(f"Atkartojums {run}: Videja vertiba: {avg_value:.4f} | Laiks: {duration:.2f} s\n")

        cur.close()
        conn.close()

print(f"\nRezultati saglabati: {OUTPUT_FILE}")