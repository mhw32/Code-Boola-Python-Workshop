# ------------------------------------ 
# CODE BOOLA 2015 PYTHON WORKSHOP
# Mike Wu, Jonathan Chang, Kevin Tan
# Puzzle Challenges Number 4
# ------------------------------------

# Not going to lie, this one is almost
# IMPOSSIBLE level. It's pretty hard.
# I'd be so proud if you get this!

# ------------------------------------

# INSTRUCTIONS: 

# Have you ever heard of the power set?
# It's the set of all subsets of a set.
# Tongue twister, am I right?

# It's not that bad though. Think of it 
# like this: 

# Given a set [1,2,3]
# The power set is [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
# because [1] is a subset of [1,2,3], and so is [1,2]

# HINT: given a set A, the null set [], 
#       and A itself is always in A's power set.

# Write a function that takes a parameter lst 
# and returns the powerset.

# EXAMPLES: 

# power_set([]) => [[]]
# power_set([1]) => [[], [1]]
# power_set([1,2]) => [[], [2], [1], [1,2]]
# power_set([1,2,3]) => [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
# power_set([1,2,3,4]) => # [[],[4],[3],[3,4],[2],[2,4],[2,3],[2,3,4],[1],[1,4],[1,3],[1,3,4], [1,2],[1,2,4],[1,2,3],[1,2,3,4]]

def powerset(lst):
  pass