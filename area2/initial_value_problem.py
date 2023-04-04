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


def system_first_order_differential_equation(f_uvx, g_uvx, u, v, x, x_, u0, v0):
    u_ = [0 for i in range(len(x_))]
    v_ = [0 for i in range(len(x_))]
    u_[0] = u0
    v_[0] = v0

    for i in range(len(x_) - 1):
        h = (x_[i+1] - x_[i])

        u1 = f_uvx.subs(x, x_[i]).subs(u, u_[i]).subs(v, v_[i])
        v1 = g_uvx.subs(x, x_[i]).subs(u, u_[i]).subs(v, v_[i])

        u_[i+1] = u_[i] + h * u1
        v_[i+1] = v_[i] + h * v1
        
    return u_, v_

def system_first_order_differential_equation_final_value(f_uvx, g_uvx, u, v, x, x_, u0, v0):
    u_ = u0
    v_ = v0

    for i in range(len(x_) - 1):
        h = (x_[i+1] - x_[i])

        u1 = f_uvx.subs(x, x_[i]).subs(u, u_).subs(v, v_)
        v1 = g_uvx.subs(x, x_[i]).subs(u, u_).subs(v, v_)

        u_ = u_ + h * u1
        v_ = v_ + h * v1
        
    return u_, v_

def heun_method_edo_solver(f_ux, u, x, x_, u0):
    u_ = [0 for i in range(len(x_))]
    u_[0] = u0

    for n in range(len(x_) - 1):
        h = x_[n+1] - x_[n]

        # first approximation
        u_[n+1] = u_[n] + h * f_ux.subs(x, x_[n]).subs(u, u_[n])
        
        f_un_xn = f_ux.subs(x, x_[n]).subs(u, u_[n])
        f_un1_xn1 = f_ux.subs(x, x_[n+1]).subs(u, u_[n+1])

        temp = (f_un_xn + f_un1_xn1) / 2
        
        # approximation correction
        u_[n+1] = u_[n] + h * temp
    return u_

def heun_method_edo_solver_last_value(f_ux, u, x, x_, u0):
    u_ = u0

    for n in range(len(x_) - 1):
        h = x_[n+1] - x_[n]

        # first approximation
        u_aux = u_ + h * f_ux.subs(x, x_[n]).subs(u, u_)
        
        f_un_xn = f_ux.subs(x, x_[n]).subs(u, u_)
        f_un1_xn1 = f_ux.subs(x, x_[n+1]).subs(u, u_aux)

        temp = (f_un_xn + f_un1_xn1) / 2
        
        # approximation correction
        u_[n+1] = u_[n] + h * temp
    return u_