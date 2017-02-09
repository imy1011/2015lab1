'''
Created on Feb 8, 2017
@author: loanvo

Description:
'''


import pandas as pd
import numpy as np
import matplotlib as mplt
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import scipy as sp


x = np.arange(0, 10, .3)
y = np.sin(x)
ynoisy = y + np.random.randn(len(y))
plt.figure(1)
plt.plot(x, y, 'o-', label='A sine wave')
plt.plot(x, ynoisy, '-', label='Noisy since')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend(loc='lower right')



print("Make a 3 row x 4 column array of random numbers")
x = np.random.random((3, 4))
print(x)
print()

print("Add 1 to every element")
x = x + 1
print(x)
print()

print("Get the element at row 1, column 2")
print(x[1, 2])
print()

# The colon syntax is called "slicing" the array. 
print("Get the first row")
print(x[0, :])
print()

print("Get every 2nd column of the first row")
print(x[0, ::2])
print()

print('Max x:', x.max())
print('Max element of each row:', x.max(axis=0))
print('Min x:', x.min())
print('Mean x:', x.mean())

numOfSimulations = 500
numOfTrialsInEachSimulation = 500
numOfSuccesses = np.random.binomial(numOfTrialsInEachSimulation, .5, (numOfSimulations, 1)) 
# print(coinTosses)
plt.figure(2)
plt.hist(numOfSuccesses)


# The Monty Hall Problem---------------------------------------------------
nsims = 10
"""
Function
--------
simulate_prizedoor

Generate a random array of 0s, 1s, and 2s, representing
hiding a prize between door 0, door 1, and door 2

Parameters
----------
nsim : int
    The number of simulations to run

Returns
-------
prizedoors : array
    Random array of 0s, 1s, and 2s

Example
-------
>>> print simulate_prizedoor(3)
array([0, 0, 2])
"""
def simulate_prizedoor(nsim):
    prizedoors = np.random.choice([0, 1, 2], size=nsim)  # or can use: np.random.randint(0,3,size=nsim)
    return prizedoors
prizedoors = simulate_prizedoor(nsims)
print('Prize doors:   ', prizedoors)

"""
Function
--------
simulate_guess

Return any strategy for guessing which door a prize is behind. This
could be a random strategy, one that always guesses 2, whatever.

Parameters
----------
nsim : int
    The number of simulations to generate guesses for

Returns
-------
guesses : array
    An array of guesses. Each guess is a 0, 1, or 2

Example
-------
>>> print simulate_guess(5)
array([0, 0, 0, 0, 0])
"""

def simulate_guess(nsim):
    # guesses = np.random.choice([0, 1, 2], size=nsim)  
    # or can use: 
    guesses = np.random.randint(0, 3, size=nsim)
    return guesses
guesses = simulate_guess(nsims)
print('Guesses:       ', guesses)

"""
Function
--------
goat_door

Simulate the opening of a "goat door" that doesn't contain the prize,
and is different from the contestants guess

Parameters
----------
prizedoors : array
    The door that the prize is behind in each simulation
guesses : array
    THe door that the contestant guessed in each simulation

Returns
-------
goats : array
    The goat door that is opened for each simulation. Each item is 0, 1, or 2, and is different
    from both prizedoors and guesses

Examples
--------
>>> print goat_door(np.array([0, 1, 2]), np.array([1, 1, 1]))
>>> array([2, 2, 0])
"""
def goat_door(prizedoors, guesses):
    # the show host favors opening door 0 if it is not the prize or guess door.
    # If it is he then favors opening door 1 if door 1 is not the prize or guess door.
    # goats = [0 if p!=0 and g!=0 else (1 if p!=1 and g!=1 else 2) for p,g in zip(prizedoors,guesses)]
    goats = np.random.randint(0, 3, size=prizedoors.size)
    while True:
        bad = (goats == prizedoors) | (goats == guesses)  # the __or__ method in an object overloads the bitwise or operator (|), not the boolean or operator.
        if not any(bad):
            return goats
        else:
            goats[bad] = np.random.randint(0, 3, size=bad.sum())
goatdoors = goat_door(prizedoors, guesses)
print('Goat doors:    ', goatdoors)



"""
Function
--------
switch_guess

The strategy that always switches a guess after the goat door is opened

Parameters
----------
guesses : array
     Array of original guesses, for each simulation
goatdoors : array
     Array of revealed goat doors for each simulation

Returns
-------
The new door after switching. Should be different from both guesses and goatdoors

Examples
--------
>>> print switch_guess(np.array([0, 1, 2]), np.array([1, 2, 1]))
>>> array([2, 0, 0])
"""
def switch_guess(guesses, goatdoors):
    newguesses = np.zeros(guesses.size, dtype=int)
    while True:
        bad = (newguesses == guesses) | (newguesses == goatdoors)
        if not any(bad):
            return newguesses
        else:
            newguesses[bad] = newguesses[bad] + 1
switchguesses = switch_guess(guesses, goatdoors)
print('Switch guesses:', switchguesses)


"""
Function
--------
win_percentage

Calculate the percent of times that a simulation of guesses is correct

Parameters
-----------
guesses : array
    Guesses for each simulation
prizedoors : array
    Location of prize for each simulation

Returns
--------
percentage : number between 0 and 100
    The win percentage

Examples
---------
>>> print win_percentage(np.array([0, 1, 2]), np.array([0, 0, 0]))
33.333
"""
def win_percentage(guesses, prizedoors):
    return (guesses == prizedoors).mean() * 100
winpercentage = win_percentage(np.array([0, 1, 2]), np.array([0, 0, 0]))
print(winpercentage)


nsim = 10000

# keep guesses
print("Win percentage when keeping original door")
print(win_percentage(simulate_prizedoor(nsim), simulate_guess(nsim)))

# switch
pd = simulate_prizedoor(nsim)
guess = simulate_guess(nsim)
goats = goat_door(pd, guess)
guess = switch_guess(guess, goats)
print("Win percentage when switching doors")
print(win_percentage(pd, guess).mean())
# plt.show()
