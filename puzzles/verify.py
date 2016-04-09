import sys, numpy as np, os
sys.path.append('./easy')
from puzzle1e import president
from puzzle2e import hypotenuse
from puzzle3e import loops
from puzzle4e import detect
from puzzle5e import createList
from puzzle6e import factorial
from puzzle7e import reverse_lst
from puzzle8e import select
from puzzle9e import clean
from puzzle10e import listify

sys.path.append('./medium')
from puzzle1m import largest_digit
from puzzle2m import sum_digits
from puzzle3m import reverse
from puzzle4m import convert
from puzzle5m import dictionarify

sys.path.append('./hard')
from puzzle1h import fizzbuzz
from puzzle2h import palindrome
from puzzle3h import encrypt
from puzzle4h import decrypt

# --------------------------

easy_pts   = np.zeros(10)
medium_pts = np.zeros(5)
hard_pts   = np.zeros(4)
impos_pts  = np.zeros(1)

total_easy_pts   = [1, 4, 4, 3, 2, 5, 4, 3, 5, 3]
total_medium_pts = [4, 5, 5, 5, 9]
total_hard_pts   = [6, 5, 4, 4]
total_impos_pts  = [0]

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):

  try:
    if (hasattr(expected, '__call__')):
      OK = expected(got)
    else:
      OK = (got == expected)
  except:
    OK = False

  prefix = '[OK]' if OK else '[X]'

  print ('%s got: %s, expected: %s' % (prefix, repr(got), repr(expected)))
  return OK

print '====================================='
print '||   CODE BOOLA PUZZLE CHALLENGE   ||'
print '||          FUNCTION OUTPUTS       ||'
print '====================================='

#  ------------- Easy problem grading. -------------

print '-------------------------------------'
print '|        1) EASY PUZZLES            |'
print '-------------------------------------'

print '--- PROBLEM ONE ---'
print '>>> FUNCTION CALL: president()'
easy_pts[0] += test(president(), lambda s: type(s) == type(''))

print '--- PROBLEM TWO ---'
print '>>> FUNCTION CALL: hypotenuse(3,4)'
easy_pts[1] += test(hypotenuse(3,4), 5)
print '>>> FUNCTION CALL: hypotenuse(5,12)'
easy_pts[1] += test(hypotenuse(5,12), 13)
print '>>> FUNCTION CALL: hypotenuse(6,8)'
easy_pts[1] += test(hypotenuse(6,8), 10)
print '>>> FUNCTION CALL: hypotenuse(1,1)'
easy_pts[1] += test(hypotenuse(1,1), 1.4142135623730951)

print '--- PROBLEM THREE ---'
print '>>> FUNCTION CALL: loops(5)'
easy_pts[2] += test(loops(5), [0, 1, 2, 3, 4])
print '>>> FUNCTION CALL: loops(1)'
easy_pts[2] += test(loops(1), [0])
print '>>> FUNCTION CALL: loops(0)'
easy_pts[2] += test(loops(0), [])
print '>>> FUNCTION CALL: loops(10)'
easy_pts[2] += test(loops(10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print '--- PROBLEM FOUR ---'
print '>>> FUNCTION CALL: detect(12)'
easy_pts[3] += test(detect(12), True)
print '>>> FUNCTION CALL: detect(9)'
easy_pts[3] += test(detect(9), False)
print '>>> FUNCTION CALL: detect(10)'
easy_pts[3] += test(detect(10), False)

print '--- PROBLEM FIVE ---'
print ">>> FUNCTION CALL: createList(['hi', 34, 0, '64', 'five'], 100)"
easy_pts[4] += test(createList(['hi', 34, 0, '64', 'five'], 100), ['hi', 34, 0, '64', 'five', 100])
print ">>> FUNCTION CALL: ccreateList([None, 1, '2', 'lkj', 41], True)"
easy_pts[4] += test(createList([None, 1, '2', 'lkj', 41], True), [None, 1, '2', 'lkj', 41, True])

print '--- PROBLEM SIX ---'
print '>>> FUNCTION CALL: factorial(1)'
easy_pts[5] += test(factorial(1), 1)
print '>>> FUNCTION CALL: factorial(10)'
easy_pts[5] += test(factorial(10), 3628800)
print '>>> FUNCTION CALL: factorial(-1)'
easy_pts[5] += test(factorial(-1), None)
print '>>> FUNCTION CALL: factorial(0)'
easy_pts[5] += test(factorial(0), 1)
print '>>> FUNCTION CALL: factorial(4)'
easy_pts[5] += test(factorial(4), 24)

print '--- PROBLEM SEVEN ---'
print '>>> FUNCTION CALL: reverse_lst([1, 2, 3])'
easy_pts[6] += test(reverse_lst([1, 2, 3]), [3, 2, 1])
print '>>> FUNCTION CALL: reverse_lst([])'
easy_pts[6] += test(reverse_lst([]), [])
print '>>> FUNCTION CALL: reverse_lst([1])'
easy_pts[6] += test(reverse_lst([1]), [1])
print '>>> FUNCTION CALL: reverse_lst([1, 1, 1, 2, 1, 1])'
easy_pts[6] += test(reverse_lst([1, 1, 1, 2, 1, 1]), [1, 1, 2, 1, 1, 1])

print '--- PROBLEM EIGHT ---'
print '>>> FUNCTION CALL: select(12345)'
easy_pts[7] += test(select(12345), "1")
print '>>> FUNCTION CALL: select(519)'
easy_pts[7] += test(select(519), "5")
print '>>> FUNCTION CALL: select(2)'
easy_pts[7] += test(select(2), "2")

print '--- PROBLEM NINE ---'
print '>>> FUNCTION CALL: clean("hi this is mike"), "hithisismike")'
easy_pts[8] += test(clean("hi this is mike"), "hithisismike")
print '>>> FUNCTION CALL: clean("")'
easy_pts[8] += test(clean(""), "")
print '>>> FUNCTION CALL: clean(" ")'
easy_pts[8] += test(clean(" "), "")
print '>>> FUNCTION CALL: clean("omg      spaces")'
easy_pts[8] += test(clean("omg      spaces"), "omgspaces")
print '>>> FUNCTION CALL: clean("freebie")'
easy_pts[8] += test(clean("freebie"), "freebie")

print '--- PROBLEM TEN ---'
t1 = {'a':1, 'b':2, 'c':3}
t2 = {}
t3 = {'a':1235}
print ">>> FUNCTION CALL: listify({'a':1, 'b':2, 'c':3})"
easy_pts[9] += test(listify(t1), ['a', 'b', 'c'])
print ">>> FUNCTION CALL: listify({})"
easy_pts[9] += test(listify(t2), [])
print ">>> FUNCTION CALL: listify({'a':1235})"
easy_pts[9] += test(listify(t3), ['a'])

print '-------------------------------------'
print '|        2) MEDIUM PUZZLES          |'
print '-------------------------------------'

print '--- PROBLEM ONE ---'
print ">>> FUNCTION CALL: largest_digit(12345)"
medium_pts[0] += test(largest_digit(12345),5)
print ">>> FUNCTION CALL: largest_digit(11111)"
medium_pts[0] += test(largest_digit(11111),1)
print ">>> FUNCTION CALL: largest_digit(54321)"
medium_pts[0] += test(largest_digit(54321),5)
print ">>> FUNCTION CALL: largest_digit(5432123456789123)"
medium_pts[0] += test(largest_digit(5432123456789123),9)

print '--- PROBLEM TWO ---'
print ">>> FUNCTION CALL: sum_digits(10)"
medium_pts[1] += test(sum_digits(10), 1)
print ">>> FUNCTION CALL: sum_digits(13)"
medium_pts[1] += test(sum_digits(13), 4)
print ">>> FUNCTION CALL: sum_digits(1000000)"
medium_pts[1] += test(sum_digits(1000000),1)
print ">>> FUNCTION CALL: sum_digits(123456789)"
medium_pts[1] += test(sum_digits(123456789), 45)
print ">>> FUNCTION CALL: sum_digits(9)"
medium_pts[1] += test(sum_digits(9),9)

print '--- PROBLEM THREE ---'
print '>>> FUNCTION CALL: reverse("blah")'
medium_pts[2] += test(reverse("blah"), "halb")
print '>>> FUNCTION CALL: reverse("tset")'
medium_pts[2] += test(reverse("tset"), "test")
print '>>> FUNCTION CALL: reverse("racecar")'
medium_pts[2] += test(reverse("racecar"), "racecar")
print '>>> FUNCTION CALL: reverse("12367")'
medium_pts[2] += test(reverse("12367"), "76321")
print '>>> FUNCTION CALL: reverse("")'
medium_pts[2] += test(reverse(""), "")

print '--- PROBLEM FOUR ---'
print '>>> FUNCTION CALL: convert("cat")'
medium_pts[3] += test(convert("cat"), 312)
print '>>> FUNCTION CALL: convert("dog")'
medium_pts[3] += test(convert("dog"), 314)
print '>>> FUNCTION CALL: convert("boola")'
medium_pts[3] += test(convert("boola"), 525)
print '>>> FUNCTION CALL: convert("1467")'
medium_pts[3] += test(convert("1467"), 210)
print '>>> FUNCTION CALL: convert("")'
medium_pts[3] += test(convert(""), 0)

print '--- PROBLEM FIVE ---'
print ">>> d1 = dictionarify(['a', 'b', 'c'], [1, 2, 3])"
print ">>> d2 = dictionarify(['a', 'b', 'c', 'a'], [1, 2, 3, 4])"
print ">>> d3 = dictionarify(['a' ,'b'], [1])"
d1 = dictionarify(['a', 'b', 'c'], [1, 2, 3])
d2 = dictionarify(['a', 'b', 'c', 'a'], [1, 2, 3, 4])
d3 = dictionarify(['a' ,'b'], [1])

if not d1 is None:
  print ">>> FUNCTION CALL: d1['a']"
  medium_pts[4] += test(d1['a'], 1)
  print ">>> FUNCTION CALL: d1['b']"
  medium_pts[4] += test(d1['b'], 2)
  print ">>> FUNCTION CALL: d1['c']"
  medium_pts[4] += test(d1['c'], 3)
  print ">>> FUNCTION CALL: len(d1)"
  medium_pts[4] += test(len(d1), 3)
else:
  print '[X] d1 is None'
if not d2 is None:
  print ">>> FUNCTION CALL: d2['a']"
  medium_pts[4] += test(d2['a'], 4)
  print ">>> FUNCTION CALL: d2['b']"
  medium_pts[4] += test(d2['b'], 2)
  print ">>> FUNCTION CALL: d2['c']"
  medium_pts[4] += test(d2['c'], 3)
  print ">>> FUNCTION CALL: len(d2)"
  medium_pts[4] += test(len(d2), 3)
else:
  print '[X] d2 is None'
if not d3 is None:
  print ">>> FUNCTION CALL: d3"
  medium_pts[4] += test(d3, {})
else:
  print '[X] d3 is None'

print '-------------------------------------'
print '|        3) HARD PUZZLES            |'
print '-------------------------------------'

print '--- PROBLEM ONE ---'
print ">>> FUNCTION CALL: fizzbuzz(3)"
hard_pts[0] += test(fizzbuzz(3), [1, 2, 'Fizz'])
print ">>> FUNCTION CALL: fizzbuzz(5)"
hard_pts[0] += test(fizzbuzz(5), [1, 2, 'Fizz', 4, 'Buzz'])
print ">>> FUNCTION CALL: fizzbuzz(0)"
hard_pts[0] += test(fizzbuzz(0), [])
if not fizzbuzz(15) is None:
  print ">>> FUNCTION CALL: len(fizzbuzz(15))"
  hard_pts[0] += test(len(fizzbuzz(15)), 15)
  print ">>> FUNCTION CALL: fizzbuzz(15)[-1]"
  hard_pts[0] += test(fizzbuzz(15)[-1], 'FizzBuzz')
  print ">>> FUNCTION CALL: fizzbuzz(15)[-5:]"
  hard_pts[0] += test(fizzbuzz(15)[-5:], ['Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'])
else:
  print '[X] fizzbuzz(15) is None'

print '--- PROBLEM TWO ---'
print ">>> FUNCTION CALL: palindrome('racecar')"
hard_pts[1] += test(palindrome('racecar'), True)
print ">>> FUNCTION CALL: palindrome('sample')"
hard_pts[1] += test(palindrome('sample'), False)
print ">>> FUNCTION CALL: palindrome('do geese see god')"
hard_pts[1] += test(palindrome('do geese see god'), True)
print ">>> FUNCTION CALL: palindrome('')"
hard_pts[1] += test(palindrome(''), False)
print ">>> FUNCTION CALL: palindrome('freebie')"
hard_pts[1] += test(palindrome('freebie'), False)

print '--- PROBLEM THREE ---'
print ">>> FUNCTION CALL: encrypt('test', 12)"
hard_pts[2] += test(encrypt('test', 12), '\x80q\x7f\x80')
print ">>> FUNCTION CALL: encrypt('lots of fun', 12)"
hard_pts[2] += test(encrypt('lots of fun', 12), 'x{\x80\x7f,{r,r\x81z')
print ">>> FUNCTION CALL: encrypt('superhero', 5)"
hard_pts[2] += test(encrypt('superhero', 5), 'xzujwmjwt')
print ">>> FUNCTION CALL: encrypt('', 124)"
hard_pts[2] += test(encrypt('', 124), '')

print '--- PROBLEM FOUR ---'
print ">>> FUNCTION CALL: decrypt('\x80q\x7f\x80', 12)"
hard_pts[3] += test(decrypt('\x80q\x7f\x80', 12), 'test')
print ">>> FUNCTION CALL: decrypt('x{\x80\x7f,{r,r\x81z', 12)"
hard_pts[3] += test(decrypt('x{\x80\x7f,{r,r\x81z', 12), 'lots of fun')
print ">>> FUNCTION CALL: decrypt('xzujwmjwt', 5)"
hard_pts[3] += test(decrypt('xzujwmjwt', 5), 'superhero')
print ">>> FUNCTION CALL: decrypt('', 124)"
hard_pts[3] += test(decrypt('', 124), '')

print '\n'
print '====================================='
print '||   CODE BOOLA PUZZLE CHALLENGE   ||'
print '||          SCORING SYSTEM         ||'
print '====================================='

print """
                _____
               /_____\\
          ____[\`---'/]____
         /\ #\ \_____/ /# /\\
        /  \# \_.---._/ #/  \\
       /   /|\  |   |  /|\   \\
      /___/ | | |   | | | \___\\
      |  |  | | |---| | |  |  |
      |__|  \_| |_#_| |_/  |__|
      //\\\\  <\ _//^\\\\_ />  //\\\\
      \||/  |\//// \\\\\\\\/|  \||/
            |   |   |   |
            |---|   |---|
            |---|   |---|
            |   |   |   |
            |___|   |___|
            /   \   /   \\
           |_____| |_____|
           |HHHHH| |HHHHH|
"""

print '-------------------------------------'
print '|        1) EASY PUZZLES            |'
print '-------------------------------------'
for i in range(len(easy_pts)):
  print 'PUZZLE %i                       (+%d/%d)' % (i+1, easy_pts[i], total_easy_pts[i])
print '                    SUB-SCORE (%d/%d)' % (np.sum(easy_pts), np.sum(total_easy_pts))

print '-------------------------------------'
print '|        2) MEDIUM PUZZLES          |'
print '-------------------------------------'
for i in range(len(medium_pts)):
  print 'PUZZLE %i                       (+%d/%d)' % (i+1, medium_pts[i], total_medium_pts[i])
print '                    SUB-SCORE (%d/%d)' % (np.sum(medium_pts), np.sum(total_medium_pts))

print '-------------------------------------'
print '|        3) HARD PUZZLES            |'
print '-------------------------------------'
for i in range(len(hard_pts)):
  print 'PUZZLE %i                       (+%d/%d)' % (i+1, hard_pts[i], total_hard_pts[i])
print '                    SUB-SCORE (%d/%d)' % (np.sum(hard_pts), np.sum(total_hard_pts))

print '====================================='

earned_pts = np.sum(easy_pts) + np.sum(medium_pts) + np.sum(hard_pts) + np.sum(impos_pts)
total_earned_pts = np.sum(total_easy_pts) + np.sum(total_medium_pts) + np.sum(total_hard_pts) + np.sum(total_impos_pts)

print '                  TOTAL SCORE (%d/%d)' % (earned_pts, total_earned_pts)
print '====================================='

