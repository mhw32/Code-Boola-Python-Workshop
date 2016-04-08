# ------------------------------------ 
# CODE BOOLA 2015 PYTHON WORKSHOP
# Mike Wu, Jonathan Chang, Kevin Tan
# Puzzle Challenges Number 3
# ------------------------------------ 

# Let's do something with cool math
# figures and plots. This will be 
# super cool. I promise. 

# ------------------------------------ 
# INSTRUCTIONS: 

# I'm interested in the shape of a
# parametric curve. I know the formula, 
# but I just can't seem to understand 
# what it looks like! I've set up more 
# of the code already, but I need some 
# help saving the plot. 

# Write a function that takes in no 
# arguments and saves the plot to 
# the following pathname: './test.png'.

# We've imported the matplotlib library
# which is super popular for plotting 
# graphs. 

# HINT: One of the functions in the 
# library is savefig(pathname). Use it:
# 
#   plt.savefig(pathname)

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
mpl.rcParams['legend.fontsize'] = 10

def savefigure():
  fig = plt.figure()
  ax = fig.gca(projection='3d')
  theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
  z = np.linspace(-2, 2, 100)
  r = z**2 + 1
  x = r * np.sin(theta)
  y = r * np.cos(theta)
  ax.plot(x, y, z, label='parametric curve')
  ax.legend()
  ... # Fill this out!

# Take a look at your saved figure! 
# It should now be in the medium folder!
