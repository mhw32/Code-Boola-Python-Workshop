# ------------------------------------ 
# CODE BOOLA 2015 PYTHON WORKSHOP
# Mike Wu, Jonathan Chang, Kevin Tan
# Puzzle Challenges Number 8
# ------------------------------------ 

#                   /88888888888888888888888888\
#                   |88888888888888888888888888/
#                    |~~____~~~~~~~~~"""""""""|
#                   / \_________/"""""""""""""\
#                  /  |              \         \
#                 /   |  88    88     \         \
#                /    |  88    88      \         \
#               /    /                  \        |
#              /     |   ________        \       |
#              \     |   \______/        /       |
#   /"\         \     \____________     /        |
#   | |__________\_        |  |        /        /
# /""""\           \_------'  '-------/       --
# \____/,___________\                 -------/
# ------*            |                    \
#   ||               |                     \
#   ||               |                 ^    \
#   ||               |                | \    \
#   ||               |                |  \    \
#   ||               |                |   \    \
#   \|              /                /"""\/    /
#      -------------                |    |    /
#      |\--_                        \____/___/
#      |   |\-_                       |
#      |   |   \_                     |
#      |   |     \                    |
#      |   |      \_                  |
#      |   |        ----___           |
#      |   |               \----------|
#      /   |                     |     ----------""\
# /"\--"--_|                     |               |  \
# |_______/                      \______________/    )
#                                               \___/

# ------------------------------------ 
# INSTRUCTIONS: 

# Let's work with some dictionaries. 
# A common situation with dictionaries
# is that I have two lists, lstA and 
# lstB, and I want to every element
# of lstA to the matching element in 
# lstB. 

# Write a function that takes as arguments
# two lists, lstA & lstB, and returns a 
# dictionary that maps the 0th element of 
# lstA to the 0th element of lstB, the 1st
# element of lstA to the 1st element of lstB, 
# etc. 

# If the two lists are not the same length, 
# return an empty dictionary.

# EXAMPLES
# d = dictionarify(['a', 'b', 'c'], [1, 2, 3])
# d['a'] => should be 1
# d['b'] => should be 2
# d['c'] => should be 3

# d = dictionarify(['a', 'b', 'c', 'a'], [1, 2, 3, 4])
# d['a'] => should be 4
# d['b'] => should be 2
# d['c'] => should be 3

# d = dictionarify(['a' ,'b'], [1])
# d => should be {}

def dictionarify(lstA, lstB):
  pass
