# ------------------------------------
# CODE BOOLA 2015 PYTHON WORKSHOP
# Mike Wu, Jonathan Chang, Kevin Tan
# Puzzle Challenges Number 1
# ------------------------------------

# Crafted to really give you a hard
# time. Please please please do not
# spend too much time on this!

#     |\_|X|_/|
#    /         \
#  =(  O     O  )=
#   -\    o    /-
#    / .-----. \
#  /_ | o   o |_ \
# (U  |       |  U)
#    _|_     _|_
#   (   )---(   )
#   Hello   Kitty

# ------------------------------------
# INSTRUCTIONS:

f = open('rap.txt', 'r+')

#this function should find all the unique words and put them in a dictionary
#i.e dictionary = {'word' : 'count'}
def unique_words():
    words = {} #dictionary that contains unique words
    for line in f: #read each line in the file
        line = line.replace(',', '')
        line_stripped = [x.strip() for x in line.split(' ')]
        print line_stripped
        #now you have an array (line_stripped) of the words in each line
        #add them to your dictionary and keep track of count
    pass

#find the biggest vocab by finding the number of unique words
def num_unique_words():
    words = unique_words()
    #return number of unique words
    pass

def top_ten_words():
    words = unique_words()
    import operator #sorts words by count
    sorted_words = sorted(words.items(), key=operator.itemgetter(1))
    print words
    # now find the top 10 and return
    pass
