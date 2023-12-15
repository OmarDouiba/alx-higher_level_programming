#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
        )
    select_all = """
    SELECT * FROM states
    ORDER BY states.id ASC
    """
    cursor = connection.cursor()
    cursor.execute(select_all)
    resualt = cursor.fetchall()
    for row in resualt:
        print(row)
    cursor.close()
    connection.close()
