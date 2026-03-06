#!/usr/bin/python3
"""
A module that filters states by user input.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    state_name = sys.argv[4]

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
    cur.execute(query.format(state_name))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
