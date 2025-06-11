import matplotlib.pyplot as plt
import sys

# instantiate variables 
b = 0
nb = 0
nb_ = 0
b_nb = 0
bresult = []
nbresult = []

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

    # append initial populations 
    bresult.append(b)
    nbresult.append(nb)

def observe():
    global b, nb, bresult, nbresult
    # Add the new variable states to the time series
    bresult.append(b)
    nbresult.append(nb)

def update():
    global b, nb, nb_b, b_nb, bresult, nbresult
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
# code necessary for running in console 
    #args = sys.argv
    #if (args.__len__ < 4):
        # Raise usage exception if there aren't enough arguments
        #raise Exception("Usage: miniproject1 <belief popularity> <belief-nonbelief conversion> <nonbelief-belief conversion>")
    #else:
        #initialize(args[1], (1 - args[1]), args[2], args[3])
    
# code for running in ide
    # believer prop, non-believer prop, nb-b conversion rate, b-nb conversion rate
    initialize(.20, .50, 0.1, 0.60)

    for i in range(0,10):
        update()
        observe()

    print(bresult)
    print(nbresult)
    plt.plot(bresult, label = "believers")
    plt.plot(nbresult, label = "non-believers")

    plt.legend()

    plt.show()

main()