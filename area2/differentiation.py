import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def diff_fwd(x, y):
    n = len(x)
    
    y_1 = [(y[i + 1] - y[i])/(x[i + 1] - x[i]) for i in range(n-1)] + [np.nan]
    return y_1

def diff_bwd(x, y):
    n = len(x)
    y_1 = [np.nan] + [(y[i] - y[i-1])/(x[i] - x[i-1]) for i in range(1, n)]
    return y_1

def diff_mid(x, y, h=None):
    n = len(x)
    if h == None:
        y_1 = np.array([np.nan] + [(y[i+1] - y[i-1])/(x[i+1] - x[i-1]) for i in range(1, n-1)] + [np.nan])
    else:
        y_1 = np.array([np.nan] + [(y[i+1] - y[i-1])/(2*h) for i in range(1, n-1)] + [np.nan])
    return y_1


def diff_2(x, y):
    n = len(x)
    y_1 = [0] + [(y[i+1] - 2* y[i] + y[i-1])/((x[i+1] - x[i-1]) * (x[i+1] - x[i-1])) for i in range(1, n-1)]
    y_1[0] = np.nan
    y_1.append(np.nan)
    y_1 = np.array(y_1)
    return y_1