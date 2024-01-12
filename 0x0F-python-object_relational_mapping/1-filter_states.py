#!/usr/bin/python3
"""
script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3],
    )

    cur = connection.cursor()
    query = cur.execute("""
                        SELECT * from states
                        WHERE name LIKE BINARY 'N%'
                        """)

    res = cur.fetchall()

    for state in res:
        print(state)
    cur.close()
    connection.close()
