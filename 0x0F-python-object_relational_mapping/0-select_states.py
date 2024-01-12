#!/usr/bin/env python3
#  script that lists all states from the database hbtn_0e_0_usa.

if __name__ = '__main__':
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3]
        )
    cur = connection.cursor()

    cur.execute(f"SELECT * FROM states")
    for state in cur:
        print(state)

    cur.close()
    connection.close()