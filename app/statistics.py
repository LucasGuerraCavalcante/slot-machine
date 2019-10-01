import numpy as np
import pandas as pd

# Creating the Arrays

reel1 = np.array([
    ['7',          1],
    ['A',          3],
    ['Spades',     2],
    ['Clubs',      1],
    ['Hearts',     7],
    ['Diamonds',   5],
    ['Happy Face', 2]
])

reel2 = np.array([
    ['7',          1],
    ['A',          2],
    ['Spades',     2],
    ['Clubs',      5],
    ['Hearts',     3],
    ['Diamonds',   5],
    ['Happy Face', 6]
])

reel3 = np.array([
    ['7',          1],
    ['A',          1],
    ['Spades',     2],
    ['Clubs',      8],
    ['Hearts',     3],
    ['Diamonds',   4],
    ['Sad Face',   2]
])

# Turning then into data frames

reel1 = pd.DataFrame(reel1, columns=['type','qt'])
reel2 = pd.DataFrame(reel2, columns=['type','qt'])
reel3 = pd.DataFrame(reel3, columns=['type','qt'])

# Turning all values from 'qt' column into int

reel1 = reel1.astype({'qt': int})
reel2 = reel2.astype({'qt': int})
reel3 = reel3.astype({'qt': int})

# Getting the sum of each value from 'qt' (quantity) column

totalReel1 = reel1['qt'].sum()
totalReel2 = reel2['qt'].sum()
totalReel3 = reel3['qt'].sum()

print("{} {} {}".format(totalReel1, totalReel2, totalReel3))

# -----------------------------------------------------------

# Total (totalReel1 x totalReel2 x totalReel3)

total = totalReel1*totalReel2*totalReel3

# Function to calculate the probability of any sequence
# It works receiving the index related to the symbol that you want in each reel
def prob(n1,n2,n3):
    
    val1 = reel1.iloc[n1]['qt']
    val2 = reel2.iloc[n2]['qt']
    val3 = reel3.iloc[n3]['qt']

    return str(round(((val1*val2*val3)/total)*100, 3)) + '%'  

# [7 7 7] sequence 
prob1 = prob(0,0,0)
print('[7 7 7] sequence {}'.format(prob1))

# [A A A] sequence 
prob1 = prob(1,1,1)
print('[A A A] sequence {}'.format(prob1))

# [♠ ♠ ♠] sequence 
prob1 = prob(2,2,2)
print('[♠ ♠ ♠] sequence {}'.format(prob1))

# [♠ ♠ A] sequence 
prob1 = prob(2,2,1)
print('[♠ ♠ A] sequence {}'.format(prob1))

# [♣ ♣ ♣] sequence 
prob1 = prob(3,3,3)
print('[♣ ♣ ♣] sequence {}'.format(prob1))

# [♣ ♣ A] sequence 
prob1 = prob(3,3,1)
print('[♣ ♣ A] sequence {}'.format(prob1))

# [♥ ♥ ♥] sequence 
prob1 = prob(4,4,4)
print('[♥ ♥ ♥] sequence {}'.format(prob1))

# [♥ ♥ A] sequence 
prob1 = prob(4,4,1)
print('[♥ ♥ A] sequence {}'.format(prob1))

# [♦ ♦ ♦] sequence 
prob1 = prob(5,5,5)
print('[♦ ♦ ♦] sequence {}'.format(prob1))

# [♦ ♦ A] sequence 
prob1 = prob(5,5,1)
print('[♦ ♦ A] sequence {}'.format(prob1))

# [☺ ☺ ANY] sequence

prob1 = str(round(((2*6)/(21*23))*100, 3)) + '%'  
print('[☺ ☺ ANY] sequence {}'.format(prob1))

# [☺ ANY ANY] sequence

prob1 = str(round((2/21)*100, 3)) + '%'  
print('[☺ ANY ANY] sequence {}'.format(prob1))