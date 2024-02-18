"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='irongrom2'
)
try:
    with conn:
        with conn.cursor() as cur:
            with open('north_data/employees_data.csv') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', row)

            with open('north_data/customers_data.csv') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', row)

            with open('north_data/orders_data.csv') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', row)

finally:
    conn.close()
