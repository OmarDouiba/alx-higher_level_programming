#!/usr/bin/python3

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
    WHERE name LIKE "N%"
    ORDER BY id ASC
    """

    cursor = connection.cursor()
    cursor.execute(select_data)
    data = cursor.fetchall()

    for row in data:
        print(row)
    cursor.close()
    connection.close()
    