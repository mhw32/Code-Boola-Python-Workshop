# ------------------------------------ 
# CODE BOOLA 2015 PYTHON WORKSHOP
# Mike Wu, Jonathan Chang, Kevin Tan
# Puzzle Challenges Number 2
# ------------------------------------ 

# Ready for something fun? In this 
# problem and the next problem, we 
# are going to make an ENCRYPTION
# and DECRYPTION algorithm. Remember
# the demo I showed you? You'll be 
# able to do that. Wow.

# ------------------------------------ 
# INSTRUCTIONS: 

# We are making what is called a cipher.
# Remember in puzzle 10 in the easy folder, 
# we learned about chr() and ord()?

# Well... using those, we can make a 
# cool secret message creation system.

# Here's the plan:
# Given any string, we can get it
# into a list of characters. We can
# also convert each character into 
# an integer. 

# Let's say we have a variable KEY. 
# KEY is just some integer and it 
# represents your SECRET key.  

# Let's add KEY to each integer from
# the string. Then let's convert the
# string back into characters. 

# Now we have some wacky looking string!
# PERFECT!

# EXAMPLES:
# encrypt('test', 12) => '\x80q\x7f\x80'
# encrypt('lots of fun', 12) => 'x{\x80\x7f,{r,r\x81z'
# encrypt('superhero', 5) => 'xzujwmjwt'

def encrypt(s, key):
    pass
