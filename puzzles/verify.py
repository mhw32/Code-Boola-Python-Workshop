import sys
sys.path.append('./easy')
from puzzle1e import president
from puzzle2e import hypotenuse
from puzzle3e import every_nth
from puzzle4e import *
from puzzle5e import *
from puzzle6e import *
from puzzle7e import *
from puzzle8e import *
from puzzle9e import *
from puzzle10e import *

sys.path.append('./medium')
from puzzle1m import largest_digits
from puzzle2m import sum_digits
from puzzle3m import savefigure
from puzzle4m import reverse
from puzzle5m import convert
from puzzle6m import dictionarify

sys.path.append('./hard')
from puzzle1h import fizzbuzz
from puzzle2h import palindrome
from puzzle3h import encrypt
from puzzle4h import decrypt

sys.path.append('./impossible')
from puzzle1i import impossible

print '-------------------------------------'
print '-------------------------------------'
print '||   CODE BOOLA PUZZLE CHALLENGE   ||'
print '||          SCORING SYSTEM         ||'
print '-------------------------------------'
print '-------------------------------------'
print '\n'
print '-------------------------------------'
print '|        1) EASY PUZZLES            |'
print '-------------------------------------'
print '                    SUB-SCORE (%d/%d)' 
print '\n'
print '-------------------------------------'
print '|        2) MEDIUM PUZZLES          |'
print '-------------------------------------'
print '                    SUB-SCORE (%d/%d)'
print '\n'
print '-------------------------------------'
print '|        3) HARD PUZZLES            |'
print '-------------------------------------'
print '                    SUB-SCORE (%d/%d)'
print '\n'
print '-------------------------------------'
print '|        4) HARD PUZZLES            |'
print '-------------------------------------'
print '                    SUB-SCORE (%d/%d)'
print '\n'
print '-------------------------------------'
print '|        5) IMPOSSIBLE PUZZLES      |'
print '-------------------------------------'
print '                    SUB-SCORE (%d/%d)'
print '\n'
print '-------------------------------------'
print '-------------------------------------'
print '                  TOTAL SCORE (%d/%d)'