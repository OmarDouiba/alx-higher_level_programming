#!/usr/bin/python3
"""
script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa
where name matches the argument.
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
                WHERE BINARY name='{:s}'
                """.format(argv[4]))

    res = cur.fetchall()

    for state in res:
        print(state)
    cur.close()
    connection.close()
