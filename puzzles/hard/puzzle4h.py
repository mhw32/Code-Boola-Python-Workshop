# ------------------------------------ 
# CODE BOOLA 2015 PYTHON WORKSHOP
# Mike Wu, Jonathan Chang, Kevin Tan
# Puzzle Challenges Number 3
# ------------------------------------ 

# Alright... part 2 of the fun part.
# Get ready!

# ------------------------------------ 
# INSTRUCTIONS: 

# We have a wacky string now and no 
# one who looks at it knows what your
# original string was. But let's say
# you want to send this to your friend
# and you want your friend to be able
# to know what your original string was!

# Assuming your friend knows the key, 
# how can we do this?

# Here's a hint: instead of adding the
# key, what if you subtracted it from 
# the wacky string?

# EXAMPLES:
# decrypt('\x80q\x7f\x80', 12) => 'test'
# decrypt('x{\x80\x7f,{r,r\x81z', 12) => 'lots of fun'
# decrypt('xzujwmjwt', 5) => 'superhero'

def decrypt(w, key):
  pass

# Now you have a full ENCRYPTION 
# system. Be careful though... what
# we just made was simple but it 
# is CRACKABLE! That means people 
# can still find out what your message
# was without the secret key. 

# For the most part though, you can
# now pass secret messages to anyone
# who knows the secret key.

