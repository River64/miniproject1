from pylab import *
import sys

def initialize(b0, nb0, nb_b0, b_nb0):
    global b, nb, nb_b, b_nb, bresult, nbresult

    # Popularity of believers
    b = b0
    # Popularity of non-believers
    nb = nb0

    # Non-believer -> believer conversion rate (constant)
    nb_b = nb_b0
    # Believer -> non-believer conversion rate (constant)
    b_nb = b_nb0

    # Time series for results
    bresult = [b]
    nbresult = [nb]

def observe():
    global b, nb, bresult, nbresult
    # Add the new variable states to the time series
    bresult.append(b)
    nbresult.append(nb)

def update():
    # Current states of both variables
    prevb = b
    prevnb = nb 
    # new believers - if there are more believers than nonbelievers, multiply that difference by the conversion rate
    new_b = nb_b * max(prevb - prevnb, 0)
    # same but for new non-believers
    new_nb = b_nb * max(prevnb - prevb, 0)

    b = prevb + new_b - new_nb
    nb = prevnb + new_nb - new_b

def main():
    args = sys.argv
    if (args.__len__ < 4):
        # Raise usage exception if there aren't enough arguments
        raise Exception("Usage: miniproject1 <belief popularity> <belief-nonbelief conversion> <nonbelief-belief conversion>")
    else:
        initialize(args[1], (1 - args[1]), args[2], args[3])
        for t in range(0,30):
            update()
            observe()
        plot(bresult, nbresult)
        show()
