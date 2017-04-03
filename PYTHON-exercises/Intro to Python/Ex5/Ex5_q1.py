# ============================= #
# EX 5, Q1: wc                  #
# Konstantin Masich 326893955   #
# VM: Ubuntu 16.10 x64 Python 3 #
# ============================= #

# New line symbol is counted as a distinct char.

filename = input("Please specify an input file: ")
try:
    f = open(filename)
    # Setting up counters:
    charsno = 0        # total amount of chars in file
    wordsno = 0        # total amount of words in file
    dist_words = set() # set of distinct words
    linesno = 0        # amount of lines in file
    # Passing at each line in file:
    for line in f:
        # 1. Update amount of chars:
        charsno += len(line)
        # 2. Update amount of words:
        words = line.split()
        #words = re.compile("(?<!^)\s+(?=[A-Z])(?!.\s)").split(line)
        wordsno += len(words)
        # 3. Update amount of lines:
        linesno += 1
        # 4. Update amount of distinct words:
        dist_words.update(words)
        # It's a set so it will take care of repeating
        # words for us.
    
    #Result:
    print("Amount of chars: ", charsno)
    print("Amount of words: ", wordsno)
    print("Amount of lines: ", linesno)
    print("Amount of distinct words: ", len(dist_words))
    f.close()
except IOError:
    print("Error: specified file does not exist!")
