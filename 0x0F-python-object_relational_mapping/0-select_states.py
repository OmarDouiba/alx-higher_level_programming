#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    try:
        with MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        ) as connection:
            select_all = """
            SELECT * FROM states
            ORDER BY id ASC
            """
            with connection.cursor() as cursor:
                cursor.execute(select_all)
                resualt = cursor.fetchall()
                for row in resualt:
                    print(row)
                cursor.close()
                connection.close()
    except Exception as e:
        print(e)
