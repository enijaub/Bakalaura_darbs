# Bakalaura darba pielikumi

Šajā repozitorijā ir pievienoti visi Python skripti un rezultātu faili, kas izmantoti un iegūti bakalaura darba praktiskajā daļā. Faili itever trīs testu tipus: datu ievade, datu nolasīšana un vaicājumu izpilde trim datubāzēm — InfluxDB, TimescaleDB un PostgreSQL.

Kopumā repozitorijā ir 42 faili:
- 21 ievades skripts (`*.py`) – 9 datu ievades skripti (katrai datubāzei 3), 3 nolasīšanas testi un 9 vaicājumu izpildes skripti;
- 21 rezultātu fails (`*.txt`) – atbilstošie izvades dati katram testam.

Zemāk atrodams visu pielikumu saraksts atbilstoši numerācijai Bakalaura darbā:

| Pielikums        | Fails                                  | Apraksts                                        |
|------------------|----------------------------------------|-------------------------------------------------|
| 1. pielikums     | pirmais_tests_InfluxDB.py                | InfluxDB – datu ievades skripts ar batch = 10   |
| 2. pielikums     | otrais_tests_InfluxDB.py               | InfluxDB – datu ievades skripts ar batch = 50  |
| 3. pielikums     | tresais_tests_InfluxDB.py              | InfluxDB – datu ievades skripts ar batch = 100 |
| 4. pielikums     | pirmais_tests_TimescaleDB.py             | TimescaleDB – datu ievades skripts ar batch = 10 |
| 5. pielikums     | otrais_tests_TimescaleDB.py            | TimescaleDB – datu ievades skripts ar batch = 50 |
| 6. pielikums     | tresais_tests_TimescaleDB.py           | TimescaleDB – datu ievades skripts ar batch = 100 |
| 7. pielikums     | pirmais_tests_PostgreSQL.py              | PostgreSQL – datu ievades skripts ar batch = 1 |
| 8. pielikums     | otrais_tests_PostgreSQL.py             | PostgreSQL – datu ievades skripts ar batch = 10 |
| 9. pielikums     | tresais_tests_PostgreSQL.py            | PostgreSQL – datu ievades skripts ar batch = 100 |
| 10. pielikums    | ceturtais_tests_InfluxDB.py                     | InfluxDB – datu nolasīšanas skripts            |
| 11. pielikums    | ceturtais_tests_TimescaleDB.py                  | TimescaleDB – datu nolasīšanas skripts         |
| 12. pielikums    | ceturtais_tests_PostgreSQL.py                   | PostgreSQL – datu nolasīšanas skripts          |
| 13. pielikums    | piektais_tests_InfluxDB_filter_time.py                   | InfluxDB – laika vaicājuma tests               |
| 14. pielikums    | sestais_tests_InfluxDB_filter_field.py                  | InfluxDB – lauka vaicājuma tests               |
| 15. pielikums    | septitais_tests_InfluxDB_agreg.py              | InfluxDB – agregātvaicājuma tests              |
| 16. pielikums    | piektais_tests_TimescaleDB_filter_time.py                | TimescaleDB – laika vaicājuma tests            |
| 17. pielikums    | sestais_tests_TimescaleDB_filter_field.py               | TimescaleDB – lauka vaicājuma tests            |
| 18. pielikums    | septitais_tests_TimescaleDB_agreg.py           | TimescaleDB – agregātvaicājuma tests           |
| 19. pielikums    | piektais_tests_PostgreSQL_filter_time.py                 | PostgreSQL – laika vaicājuma tests             |
| 20. pielikums    | sestais_tests_PostgreSQL_filter_field.py                | PostgreSQL – lauka vaicājuma tests             |
| 21. pielikums    | septitais_tests_PostgreSQL_agreg.py            | PostgreSQL – agregātvaicājuma tests            |
| 22. pielikums    | influxdb_results1_batch10.txt        | InfluxDB – datu ievades rezultāti ar batch = 10 |
| 23. pielikums    | influxdb_results2_batch50.txt       | InfluxDB – datu ievades rezultāti ar batch = 50 |
| 24. pielikums    | influxdb_results3_batch100.txt      | InfluxDB – datu ievades rezultāti ar batch = 100 |
| 25. pielikums    | timescaledb_results1_batch10.txt     | TimescaleDB – datu ievades rezultāti ar batch = 10 |
| 26. pielikums    | timescaledb_results2_batch50.txt    | TimescaleDB – datu ievades rezultāti ar batch = 50 |
| 27. pielikums    | timescaledb_results3_batch100.txt   | TimescaleDB – datu ievades rezultāti ar batch = 100 |
| 28. pielikums    | postgresql_results1_batch10.txt      | PostgreSQL – datu ievades rezultāti ar batch = 10 |
| 29. pielikums    | postgresql_results2_batch50.txt     | PostgreSQL – datu ievades rezultāti ar batch = 50 |
| 30. pielikums    | postgresql_results3_batch100.txt    | PostgreSQL – datu ievades rezultāti ar batch = 100 |
| 31. pielikums    | influxdb_results4_full_table.txt             | InfluxDB – datu nolasīšanas rezultāti          |
| 32. pielikums    | timescaledb_results4_full_table.txt          | TimescaleDB – datu nolasīšanas rezultāti       |
| 33. pielikums    | postgresql_results4_full_table.txt           | PostgreSQL – datu nolasīšanas rezultāti        |
| 34. pielikums    | influxdb_results5_filter_time.txt           | InfluxDB – laika vaicājuma rezultāti           |
| 35. pielikums    | influxdb_results6_filter_field.txt          | InfluxDB – lauka vaicājuma rezultāti           |
| 36. pielikums    | influxdb_results7_agreg.txt      | InfluxDB – agregātvaicājuma rezultāti          |
| 37. pielikums    | timescaledb_results5_filter_time.txt        | TimescaleDB – laika vaicājuma rezultāti        |
| 38. pielikums    | timescaledb_results6_filter_field.txt       | TimescaleDB – lauka vaicājuma rezultāti        |
| 39. pielikums    | timescaledb_results7_agreg.txt   | TimescaleDB – agregātvaicājuma rezultāti       |
| 40. pielikums    | postgresql_results5_filter_time.txt         | PostgreSQL – laika vaicājuma rezultāti         |
| 41. pielikums    | postgresql_results6_filter_field.txt        | PostgreSQL – lauka vaicājuma rezultāti         |
| 42. pielikums    | postgresql_results7_agreg.txt    | PostgreSQL – agregātvaicājuma rezultāti        |


