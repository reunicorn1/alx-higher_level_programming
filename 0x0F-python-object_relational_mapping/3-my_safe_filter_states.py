#!/usr/bin/python3

"""
2. Filter states by user input
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name = %s\
            ORDER BY states.id", (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
