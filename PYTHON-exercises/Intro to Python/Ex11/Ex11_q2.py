# ============================= #
# EX 11, Q2: aux module usage   #
# Konstantin Masich 326893955   #
# VM: Ubuntu 16.10 x64 Python 3 #
# ============================= #

# ================================================================================================ #
# NOTICE
# This is one of the exercises I wrote for another course (Neural Networks) during previous year.
# It uses various packages and modules which were downloaded from Internet and installed, in
# particular - Pandas and CSV. 
# Initially was written in Python 2.7 as we used it for the course.
#
# This gets a CSV file of a specific structure, reads its "description" column for each row, and
# constructs a dictionary of the most frequent words in the file, plus a matrix of frequencies of
# said words in each row.
# Does not count stopwords.
#
# You can change NUM_OF_FEATURES constant to get different number of the most frequent words.
# ================================================================================================ #

NUM_OF_FEATURES = 10 # Change me if you want!

import csv
import time # For running time measurement
import numpy as np  # NumPy for work with sci functions
import pandas as pd # Pandas for processing data frame from CSV

STOP_WORDS = ['all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once', 'new','must','please','one','within','k']
STOP_WORDS_EXTENDED = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "k", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "s", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

# ==================================================================================== #
# ============================ EXTRACT FEATURES SECTION ============================== #
# ==================================================================================== #
def extract_features_testing(filepath, num_of_features):
	# 0. Load dataframe
	df = pd.read_csv(filepath, ',', usecols=['FullDescription'])
	# 1. Clean dataframe
	# 1a. Delete punctuation
	df = df['FullDescription'].str.replace('[^\w\s]','')
	# 1b. Lower case and split data string
	df = df.str.lower().str.split()
	# 1c. Delete stopwords
	df = df.apply(lambda x: [item for item in x if item not in STOP_WORDS])
	# 1d. Previous operations produce a list of words; merge them back to strings
	df = df.apply(lambda item: ' '.join(item))
	# 2. Form a dictionary
	# 2a. Get num_of_features of most frequent words in data
	freq_series = pd.Series(' '.join(df).split()).value_counts()[:num_of_features]
	# 2b. Go through freq_series and make a key-value dictionary
	dictionary = []
	temp = 0
	for i in freq_series:
		dictionary.append([temp, freq_series.index[temp]])
		temp += 1
	# 3. Form matrix
	result_matrix = [[] for x in range(len(df.index))]
	row_iterator = 0
	for row in df:
		for dic_entry in dictionary:
			entry_count = row.count(dic_entry[1])
			result_matrix[row_iterator].append(entry_count)
		row_iterator += 1
	return result_matrix, dictionary
	
# ==================================================================================== #
# ================================= MAIN WORKFLOW ==================================== #
# ==================================================================================== #
print ("<<<=====   STARTING WORKFLOW   =====>>>")
print ("_______________________________________________________________\n")

# 1. Form dictionary and matrix
start_time = time.time()
matrix, dictionary = extract_features_testing("Data_tar1.csv", 16)
print("Result dictionary")
for key, val in dictionary:
	print(key, val)
print("\nResult frequencies matrix:")
for row in matrix:
	print(row)
print("\n--- Entire function executed in %s seconds ---" % (time.time() - start_time))

print ("_______________________________________________________________\n")
print ("=====>>>   ENDING WORKFLOW   <<<=====")
