#!/usr/bin/env python3
from mysql.connector import connect
from sys import argv


try:
    with connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    ) as connection:
        select_all = """
        SELECT * FROM states
        """
        with connection.cursor() as cursor:
            cursor.execute(select_all)
            resualt = cursor.fetchall()
            for row in resualt:
                print(row)
except Exception as e:
    print(e)
