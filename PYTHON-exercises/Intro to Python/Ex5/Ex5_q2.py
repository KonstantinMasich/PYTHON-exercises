# ============================= #
# EX 5, Q2: password            #
# Konstantin Masich 326893955   #
# VM: Ubuntu 16.10 x64 Python 3 #
# ============================= #
import csv 
from collections import defaultdict

MIN_SYMBOLS = 2
TXT_INPUT_FILENAME  = "linux-etc-passwd.txt"
CSV_INPUT_FILENAME  = "linux-etc-passwd.csv"
TXT_OUTPUT_FILENAME = "Q2_out.txt"
CSV_OUTPUT_FILENAME = "Q2_out.csv"

# Version 1 - for .txt files
# For Moti: if you use the ".txt" version of linux-etc-passwd file, please
# use this section. Otherwise use the 2nd section (uncomment it).
# Assuming [0]-place is for username, [2]-place is for user ID:
try:
    infile  = open(TXT_INPUT_FILENAME)
    outfile = open(TXT_OUTPUT_FILENAME, 'w')
    for line in infile:
        # Ignoring empty lines and comment lines:
        if (len(line) <= MIN_SYMBOLS) or (line.startswith('#')):
            continue
        # Writing:
        outfile.write(line.split(':')[0] + "\t"  + line.split(':')[2] + "\n")
    infile.close()
    outfile.close()
except IOError:
    print("Error: specified file does not exist!")


# Version 2 - for .csv files
# Assuming a comma separated file looks like:
# root,x,0,0,root,/root,/bin/bash
# Where [0]-place is for username and [2]-place is for user ID
# Note that this version creates a CSV file as well, so names and 
# IDs are separated by commas and not by TABs.
"""
with open(CSV_INPUT_FILENAME) as infile:
    reader = csv.DictReader(infile) # read rows into a dictionary format
    filedata = {}
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for header, value in row.items():
            try:
                filedata[header].append(value)
            except KeyError:
                filedata[header] = [value]
    usernames = filedata['username']
    userids   = filedata['userid']
    outfile = open(CSV_OUTPUT_FILENAME, 'w')
    outfile.write("username,userid\n")
    for u_name, u_id in zip(usernames, userids):
        outfile.write(u_name + "," + u_id + "\n")
"""
