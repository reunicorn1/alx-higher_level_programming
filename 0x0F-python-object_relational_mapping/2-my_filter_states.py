#!/usr/bin/python3

"""
2. Filter states by user input
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="127.0.0.1", user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3], port=3306)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = '{}'\
            ORDER BY states.id".format(sys.argv[4])
    print(query)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
