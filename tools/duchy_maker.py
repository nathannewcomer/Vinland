# duchy.py
# Written by Nathan Newcomer

# ids are province ids belonging to a county

import sys
import sqlite3

if len(sys.argv) < 3:
    print("Usage: (program) (duchy) [province ids]")
    print("The county containing the last province id will become the capital")
    sys.exit()

# open db connection
connection = sqlite3.connect("ck3.db")
cursor = connection.cursor()

duchy_name = sys.argv[1]
prov_ids = sys.argv[2:]
capital_id = sys.argv[-1]

counties = []

# get counties from given province ids
sql = "SELECT county FROM barony WHERE province = ?"
for prov_id in prov_ids:
    result = cursor.execute(sql, (prov_id,))
    county = result.fetchone()
    counties.append(str(county))

# get county capital name from province id
sql = "SELECT county FROM barony WHERE province = ?"
county_capital = str(cursor.execute(sql, (capital_id,)).fetchone()[0])

# insert duchy
sql = "INSERT INTO duchy VALUES (?, ?, ?, ?, ?)"
cursor.execute(sql, (duchy_name, 0x000000, 0x000000, None, county_capital))

# add duchy to associated county column
for county in counties:
    sql = "UPDATE county SET duchy = ? WHERE name = ?"
    cursor.execute(sql, (duchy_name, county))

connection.commit()
connection.close()

print("success!")