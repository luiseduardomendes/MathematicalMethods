import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

sp.init_printing()

def general_regression(f0, x, x0, y0, fator_termos = None):
    
    A = general_regression_coeffs(f0, x, x0, y0)

    f = 0
    for i in range(len(A)):
        if fator_termos == None:
            f += f0[i] * A[i]
        else:
            f += f0[i] * fator_termos[i](A[i])
    return f

def general_regression_coeffs(f0, x, x0, y0):
    v = sp.Matrix(
        [
            [
                float(f0[j].subs(x,x0[i])) 
                for j in range(len(f0))
            ] 
            for i in range(len(x0))
        ]
    )
    return (v.T * v).inv() * (v.T * sp.Matrix(y0))

def linear_regression(x, x0, y0):
    return general_regression(
        [x**0, x**1],
        x, x0, y0
    )

def linear_regression_coeffs(x0, y0):
    x = sp.Symbol('x')
    return general_regression_coeffs(
        [x**0, x**1],
        x, x0, y0
    )