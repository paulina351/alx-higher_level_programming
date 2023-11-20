#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""


from sys import argv
import MySQLdb


def list_states():
    """Receives arguments argv to list from database

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """
    username = argv[1]
    password = argv[2]
    db = argv[3]
    connect = MySQLdb.connect(host="localhost", port=3306, user=username,
                              passwd=password, db=db, charset="utf8")

    c = connect.cursor()
    c.execute('SELECT * FROM states ORDER BY id ASC;')
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)
    c.close()
    connect.close()


if __name__ == "__main__":
    list_states()
