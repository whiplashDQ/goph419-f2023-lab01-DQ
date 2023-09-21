"""Launch functions for the mission"""
import numpy as np
import math

def arcsin(x):
    n_max=600
    error_critertion=0.5*10**-5
    error_s= error_critertion
    n = 1
    result= 0
    while error_s >=error_critertion and n <=n_max:
        upper_part = (2*x)**(2*n) 
        lower_part = (n**2)*(math.factorial(2*n)/(math.factorial(n))**2)
        term       = upper_part / lower_part   
        result += term
        n += 1
        error_s= term
        print(n)
    return np.sqrt(0.5*result)

x = float(input("Enter the value of x in radian: "))
result = arcsin(x)
print(result)

def launch_angle(ve_v0, alpha, tol_alpha):
    """this fuction calculate """
    return