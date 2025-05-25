import time
from influxdb import InfluxDBClient

DB_NAME = 'test3_power_data'
MEASUREMENT = 'electricity'
OUTPUT_FILE = 'influxdb_results6_filter_field.txt'
REPEAT_COUNT = 100

with open(OUTPUT_FILE, 'w') as out:
    out.write(f"{REPEAT_COUNT} atkartojumi | Pilnas tabulas izgusana\n\n")

    for run in range(1, REPEAT_COUNT + 1):
        print(f"Atkartojums {run}/{REPEAT_COUNT}")

        client = InfluxDBClient(host='localhost', port=8086, database=DB_NAME)

        query = (
            f"SELECT * FROM {MEASUREMENT} "
            f"WHERE Voltage > 250"
        )

        start = time.perf_counter()
        result = client.query(query)
        end = time.perf_counter()
        duration = end - start

        points = list(result.get_points())
        count = len(points)

        print(f"Vaicajums izpildits: {count} ieraksti | {duration:.2f} s")
        out.write(f"Atkartojums {run}: {count} ieraksti | Laiks: {duration:.2f} s\n")

print(f"\nRezultati saglabati: {OUTPUT_FILE}")