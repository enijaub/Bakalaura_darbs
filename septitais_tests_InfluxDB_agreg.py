import time
from influxdb import InfluxDBClient

DB_NAME = 'test3_power_data'
MEASUREMENT = 'electricity'
OUTPUT_FILE = 'influxdb_results7_agreg.txt'
REPEAT_COUNT = 100

with open(OUTPUT_FILE, 'w') as out:
    out.write(f"{REPEAT_COUNT} atkartojumi | Agregatvaicajums: MEAN(Global_active_power)\n\n")

    for run in range(1, REPEAT_COUNT + 1):
        print(f"Atkārtojums {run}/{REPEAT_COUNT}")

        client = InfluxDBClient(host='localhost', port=8086, database=DB_NAME)

        query = f"SELECT MEAN(Global_active_power) FROM {MEASUREMENT}"
        start = time.perf_counter()
        result = client.query(query)
        end = time.perf_counter()
        duration = end - start

        points = list(result.get_points())
        if points:
            mean_value = points[0].get("mean")
        else:
            mean_value = None

        print(f"Vaicajums izpildits | Rezultats: {mean_value} | Laiks: {duration:.2f} s")
        out.write(f"Atkartojums {run}: Rezultats: {mean_value} | Laiks: {duration:.2f} s\n")

print(f"\nRezultati saglabati: {OUTPUT_FILE}")