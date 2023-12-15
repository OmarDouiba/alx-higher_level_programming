#!/usr/bin/python3
"""
script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa.
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    select_data = """
    SELECT * FROM states
    WHERE name LIKE 'N%'
    ORDER BY id ASC
    """
    cursor = connection.cursor()
    cursor.execute(select_data)
    data = cursor.fetchall()

    for row in data:
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    connection.close()
