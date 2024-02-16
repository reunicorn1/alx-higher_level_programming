#!/usr/bin/python3

"""
5. All cities by state
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities LEFT JOIN states\
            ON cities.state_id = states.id WHERE states.name = %s\
            ORDER BY cities.id", (sys.argv[4],))
    rows = cursor.fetchall()
    print((", ".join([row[0] for row in list(rows)])))
