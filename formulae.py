import numpy as np
import math

def combinations(n,k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n-k))

def arrangements(n,k):
    return np.math.factorial(n) // np.math.factorial(n-k)

def permutation(n):
    return np.math.factorial(n)

def bayesformula(p_a_b, p_b, p_a):
    return p_a_b*p_b/p_a

def probability(m,n):
    return m/n

def bernulli(n,k,p):
    return(combinations(n,k)*(p**k)*((1-p)**(n-k)))

def puasson(la,m):
    return(((la**m)/np.math.factorial(m))*(math.e**(-1*la)))

def expected_value_for_probability(n,p):
    return n*p

def standard_deviation_for_probability(n,p):
    return np.math.sqrt(expected_value(n,p)*(1-p))

def expected_value(x):
    a = 0
    for i in x:
        a += i
    return 1/(len(x))*a

def dispersion(x):
    a = 0
    exp_val_x = expected_value(x)
    for i in x:
        a += (i-exp_val_x)*(i-exp_val_x)
    return a/(len(x))

def dispersion_displaced(x):
    a = 0
    exp_val_x = expected_value(x)
    for i in x:
        a += (i-exp_val_x)*(i-exp_val_x)
    return a/(len(x))

def standard_deviation(x):
    return np.math.sqrt(dispersion(x))

def standard_deviation_displaced(x):
    return np.math.sqrt(dispersion_displaced(x))

def percentile25 (array):
    array.sort()
    k25 = 25/100 * len(array)
    if k25%(int(k25))>1:
        k25 = int(k25)
    else:
        k25 = int(k25)-1
    return array[k25]

def percentile75 (array):
    array.sort()
    k75 = 75/100 * len(array)
    if k75%(int(k75))>1:
        k75 = int(k75)
    else:
        k75 = int(k75)-1
    return array[k75]

def median (array):
    array.sort()
    if len(array)%2 == 0:
        return (array[len(array)//2-1]+array[len(array)//2])/2
    else:
        return (array[len(array)+1/2])

def inter_quartile(array):
    return percentile75(array) - percentile25(array)

def avg (array):
    a = 0
    for i in array:
        a += i
    return (a/len(array))
