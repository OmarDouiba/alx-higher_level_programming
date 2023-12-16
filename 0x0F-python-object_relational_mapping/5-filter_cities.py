#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
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

    query = """
    SELECT cities.name FROM cities
    JOIN states
    ON states.id=cities.state_id
    WHERE states.name=%s
    ORDER BY cities.id
    """
    cursor = connection.cursor()
    cursor.execute(query, (argv[4],))
    res = cursor.fetchall()

    list_names = [row[0] for row in res]
    print(", ".join(list_names))

    # OR 2nd way
    # list_names = []
    # for row in res:
    #     list_names.append(row[0])
    # print(", ".join(list_names))

    # OR 3nd way
    # i = len(res)
    # for row in res:
    #     for name in row:
    #         print(", ".join(name), end="")
    #         if i - 1 != 0:
    #             print(end=", ")
    #         i -= 1
    # print()

    cursor.close()
    connection.close()
