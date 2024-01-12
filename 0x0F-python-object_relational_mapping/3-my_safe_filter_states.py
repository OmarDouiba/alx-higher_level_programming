#!/usr/bin/python3
"""
my_safe_filter_states from SQL injection.
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
    cur.execute("""
                SELECT * FROM states
                WHERE BINARY name=%(name)s
                """, {'name': argv[4]})
    # OR
    # cur.execute("""
    # SELECT * FROM states
    # WHERE name=%s
    # ORDER BY id ASC
    # """)

    res = cur.fetchall()

    for state in res:
        print(state)
    cur.close()
    connection.close()
