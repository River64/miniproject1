from pylab import *

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
    global b, nb, nb_b, b_nb
    # Current states of both variables
    prevb = b
    prevnb = nb 
    # new believers - if there are more believers than nonbelievers, multiply that difference by the conversion rate
    new_b = nb_b * max(prevb - prevnb, 0)
    # same but for new non-believers
    new_nb = b_nb * max(prevnb - prevb, 0)

    b = prevb + new_b - new_nb
    nb = prevnb + new_nb - new_b

'''
for initb in arange(0.1, 0.6, 0.1):
    for initnb in arange (0.1, 0.6, 0.1):
        for initnb_b in arange (0.1, 0.3, 0.1):
            for initb_nb in arange (0.1, 0.3, 0.1):
                initialize(initb, initnb, initnb_b, initb_nb)
                '''
initialize(0.15, 0.1, 0.05, 0.1)
for t in range(0,10):
    update()
    observe()
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(bresult)
print("\n")
print(nbresult)
plot(x, bresult)
plot(x, nbresult)
show()