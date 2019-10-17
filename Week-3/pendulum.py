import math

def period(L,g):
    try:
        T = 2*math.pi*math.sqrt(L/g)
    except ZeroDivisionError:
        raise ValueError
    else:
        return T    
