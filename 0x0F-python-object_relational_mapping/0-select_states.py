#!/usr/bin/python3

"""
0. Get all states
"""

import sys
import MySQLdb

db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                     passwd=sys.argv[2], database=sys.argv[3], port=3306)
cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY states.id")
rows = cursor.fetchall()
for row in rows:
    print(row)
