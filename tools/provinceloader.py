# provinceloader.py
# Written by Nathan Newcomer
#
# Tool to load provinces from definition.csv into the sqlite database.

import sys
import sqlite3

# check for command line arg file
if len(sys.argv) != 2:
    print("Enter the file path/name as the only argument.")
    sys.exit()


# open db connection
connection = sqlite3.connect("ck3.db")
cursor = connection.cursor()

# open file
file = open(sys.argv[1], "r")

# read lines into db
count = 0
file.readline()
for line in file:
    if line == "\n":
        break

    values = line.split(";")

    if len(values) < 5:
        print("Error: Unexpected data")
        print(line)
        connection.close()
        sys.exit()

    current_id = int(values[0])
    red = int(values[1])
    green = int(values[2])
    blue = int(values[3])
    name = values[4]
    sql = "INSERT INTO provinces VALUES (?, ?, ?, ?, ?)"
    cursor.execute(sql, (current_id, red, green, blue, name))
    print(f"Inserted {values}")

    count += 1


connection.commit()
print(f"Inserted {count} rows into the database.")
connection.close()