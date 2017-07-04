# ============================= #
# EX 11, Q3: "find" in re       #
# Konstantin Masich 326893955   #
# VM: Ubuntu 16.10 x64 Python 3 #
# ============================= #

import re

for fname in dir(re):
	if "find" in fname:
		print(fname)
