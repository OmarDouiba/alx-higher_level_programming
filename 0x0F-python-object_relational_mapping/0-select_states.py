#!/usr/bin/env python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        with MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            password=argv[2],
            database=argv[3]
        ) as connection:
            select_all = """
            SELECT * FROM states
            ORDER BY states.id ASC
            LIMIT 5
            """
            with connection.cursor() as cursor:
                cursor.execute(select_all)
                resualt = cursor.fetchall()
                for row in resualt:
                    print(row)
    except Exception as e:
        print(e)
