#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3]
    )

    cursor = connection.cursor()
    cursor.execute("""
                   SELECT id, name FROM cities
                   ORDER BY id ASC;""")

    res = cursor.fetchall()
    for row in res:
        print(row)

    cursor.close()
    connection.close()
