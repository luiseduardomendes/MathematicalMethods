import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
from pprint import pprint

sp.init_printing()

def divided_differences(x_, y_, x):
#retorna um polinômio formado pelo conjunto de dados de entrada
    n = len(x_)
    
    # k = divided differences table
    k = divided_differences_table(x_, y_)
    
    # coeffs
    a = [k[i][0] for i in range(n)]

    p = 0
    for i in range(n):
        c = 1
        for j in range(0, i):
            c *= (x - x_[j])
        p += a[i] * c
    p = sp.simplify(p)
    return p

def divided_differences_table(x_, y_):
    n = len(x_)
    k = [[0 for __ in range (n)] for _ in range(n)]
    for i in range(n):
        k[0][i] = y_[i]
    for i in range(1, n):
        for j in range(0, n-i):
            k[i][j] = (k[i-1][j+1] - k[i-1][j]) / (x_[j+i] - x_[j])
    return k    

def lagrangian_coefficients(x0, x):
    n = len(x0)
    
    L = [1 for _ in range(n)]
    for k in range(n):
        for j in range(n):
            if (k != j):
                L[k] *= (x - x0[j])/(x0[k] - x0[j])
    return L

def lagrangian_polynomial(x0, y0, x):
    n = len(x0)

    L = lagrangian_coefficients(x0, x)
    
    p = 0
    for k in range(n):
        p += L[k] * y0[k]
    p = sp.simplify(p)
    return p