#!/usr/bin/python3
"""
script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
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
    select_db = """
    SELECT * FROM states
    WHERE name='{}'
    ORDER BY id ASC
    """.format(argv[4])

    cursor = connection.cursor()
    cursor.execute(select_db)
    res = cursor.fetchall()

    for row in res:
        print(row)
    
    cursor.close()
    connection.close()