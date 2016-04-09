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

def unique_words():
  words = {}
  for line in f:
    line = line.replace(',', '')
    line_stripped = [x.strip() for x in line.split(' ')]
    for word in line_stripped:
      if(word in words):
        words[word] += 1
      else:
        words[word] = 1
  return words

def num_unique_words():
  words = unique
  return len(words)

def top_words():
  words = unique_words()
  import operator
  sorted_words = sorted(words.items(), key=operator.itemgetter(1))
  sorted_words_desc = sorted_words[::-1]
  top_ten = sorted_words_desc[:10]
  return top_ten

