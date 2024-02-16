#!/usr/bin/python3

"""
1. Filter states
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3], port=3306)
    cursor = db.cursor()
    qry = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id"
    cursor.execute(qry)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
