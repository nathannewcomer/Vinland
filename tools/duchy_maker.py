# duchy.py
# Written by Nathan Newcomer

# ids are province ids belonging to a county

import sys
import sqlite3
import traceback

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
try:
    for prov_id in prov_ids:
        result = cursor.execute(sql, (prov_id,)).fetchone()
        county = result[0]
        assert isinstance(county, str), f"Expected county to be of type string, got {type(county)}"
        counties.append(county)

    print("counties are:", counties)

    # get county capital name from province id
    sql = "SELECT county FROM barony WHERE province = ?"
    result = cursor.execute(sql, (capital_id,)).fetchone()
    county_capital = result[0]
    assert isinstance(county_capital, str), f"Expected county_capital to be of type string, got {type(county_capital)}"

    print("Capital is:", county_capital)

    # insert duchy
    sql = "INSERT INTO duchy VALUES (?, ?, ?, ?, ?)"
    cursor.execute(sql, (duchy_name, 0x000000, 0x000000, None, county_capital))

    print("Added duchy", duchy_name, "to database.")

    # add duchy to associated county column
    for county in counties:
        sql = "UPDATE county SET duchy = ? WHERE name = ?"
        cursor.execute(sql, (duchy_name, county))

    print("Associated duchy to counties.")
    connection.commit()
    print("Success!")
except sqlite3.Error as er:
    print('SQLite error: %s' % (' '.join(er.args)))
    print("Exception class is: ", er.__class__)
    print('SQLite traceback: ')
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))

connection.close()