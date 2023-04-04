import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

sp.init_printing()

def first_order_differential_equation(f_ux, u, x, x_, u0):
    u_ = [0 for i in range(len(x_))]
    u_[0] = u0

    for i in range(len(x_) - 1):
        h = (x_[i+1] - x_[i])
        u1 = f_ux.subs(x, x_[i]).subs(u, u_[i])

        u_[i+1] = u_[i] + h * u1
        
    return u_

def first_order_differential_equation_final_value(f_ux, u, x, x_, u0):
    u_ = u0

    for i in range(len(x_) - 1):
        h = (x_[i+1] - x_[i])
        u1 = f_ux.subs(x, x_[i]).subs(u, u_)

        u_ = u_ + h * u1
        
    return u_


def system_first_order_differential_equation(f_ux, u, x, x_, u0):
    u_ = [0 for i in range(len(x_))]
    u_[0] = u0

    for i in range(len(x_) - 1):
        h = (x_[i+1] - x_[i])
        u1 = f_ux.subs(x, x_[i]).subs(u, u_[i])

        u_[i+1] = u_[i] + h * u1
        
    return u_

def system_first_order_differential_equation_final_value(f_ux, u, x, x_, u0):
    u_ = u0

    for i in range(len(x_) - 1):
        h = (x_[i+1] - x_[i])
        u1 = f_ux.subs(x, x_[i]).subs(u, u_)

        u_ = u_ + h * u1
        
    return u_
