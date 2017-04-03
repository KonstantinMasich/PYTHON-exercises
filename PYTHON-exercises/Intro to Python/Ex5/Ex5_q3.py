# ============================= #
# EX 5, Q3: class grades        #
# Konstantin Masich 326893955   #
# VM: Ubuntu 16.10 x64 Python 3 #
# ============================= #

import json
import os

# Change dir constant if needed.
# By default, "scores" directory with json files should be in the
# SAME directory as this file (Ex5_q3.py)
WORKING_DIR = "scores"

for _, _, filenames in os.walk(WORKING_DIR):
    for fname in filenames:
        try:
            # Loading data from file:
            f = open(WORKING_DIR + "/" + fname)
            print(WORKING_DIR + "/" + fname)
            data = json.load(f)
            # Retrieving data:
            mathgrades = []
            scigrades  = []
            litgrades  = []
            for row in data:
                mathgrades.append(row['math'])
                scigrades.append(row['science'])
                litgrades.append(row['literature'])
            # Printing results:
            print("\tscience: min", min(scigrades), "max", max(scigrades), \
                  "average", (sum(scigrades)/len(scigrades)))
            print("\tliterature: min", min(litgrades), "max", max(litgrades), \
                  "average", (sum(litgrades)/len(litgrades)))
            print("\tmath: min", min(mathgrades), "max", max(mathgrades), \
                  "average", (sum(mathgrades)/len(mathgrades)))
        except IOError:
            print("Error opening file!")
