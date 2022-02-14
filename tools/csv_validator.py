# csv_validator.py
# A tool that validates the CSV file (formatting, validating with provinces.png)
# Written by Nathan Newcomer

import sys

def exit_error(reason: str, line_num: int):
    print("Error on line {0}".format(line_num))
    print(reason)
    exit(-1)

# check for command line arg file
if len(sys.argv) != 2:
    print("Enter the file path/name as the only argument.")
    sys.exit()


# open file
file = open(sys.argv[1], "r")

line_num = 1
prov_num = 0
colors = set()

# check lines
for line in file:
    values = line.split(";")

    # length check
    if len(values) != 7:
        exit_error("Incorrect number of items in line.", line_num)

    # values 
    if (not values[0].isnumeric()):
        exit_error("ID contains non-digits.", line_num)

    if (not values[1].isnumeric()):
        exit_error("Red value contains non-digits.", line_num)

    if (not values[2].isnumeric()):
        exit_error("Green value contains non-digits.", line_num)

    if (not values[3].isnumeric()):
        exit_error("Blue value contains non-digits.", line_num)

    prov_id = int(values[0])
    r = int(values[1])
    g= int(values[2])
    b = int(values[3])

    # check if id is sequential
    if prov_num != prov_id:
        exit_error("Province ID is not in sequential order.")

    rgb = (r, g, b)
    #check RGB uniqueness
    if rgb in colors:
        exit_error("RGB not unique.")

    colors.add(rgb)

    line_num += 1
    prov_num += 1