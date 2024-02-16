#!/usr/bin/python3

"""
4. Cities by states
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM\
            cities LEFT JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
