# ============================= #
# EX 5, Q3: class grades        #
# Konstantin Masich 326893955   #
# VM: Ubuntu 16.10 x64 Python 3 #
# ============================= #

import json
import os

# Change dir constant if needed.
# By default, "scores" directory with json files should be in the
# same directory as this file (Ex5_q3.py)
WORKING_DIR = "scores"

for _, _, filenames in os.walk(WORKING_DIR):
    for fname in filenames:
        try:
            f = open(WORKING_DIR + "/" + fname)
            print("File: " + WORKING_DIR + "/" + fname)
            data = json.load(f)
            for row in data:
                print(row['math'])
        except IOError:
            print("Error opening file!")
