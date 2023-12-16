#!/usr/bin/python3
"""
script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument. But this time, safe from SQL injections!
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        db=argv[3]
    )

    query = """
    SELECT * FROM states
    WHERE name=%s
    ORDER BY id ASC
    """
    cursor = connection.cursor()
    cursor.execute(query, (argv[4],))

    # OR you can use
    # query = """
    # SELECT * FROM states
    # WHERE name=%(nameIs)s
    # """
    # cursor = connection.cursor()
    # cursor.execute(query, {'nameIs': argv[4]})

    res = cursor.fetchall()
    for row in res:
        print(res)

    cursor.close()
    connection.close()
