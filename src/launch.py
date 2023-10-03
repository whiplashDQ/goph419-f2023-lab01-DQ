"""Launch functions for the mission"""
import numpy as np
import math

def arcsin(x):
    """Calculate the inverse sine of x from  [-pi/2, pi/2] using the Taylor series]"""
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
        error_s= (term/result)
    
    return np.sqrt(0.5*result)


def launch_angle(ve_v0, alpha):
    """Calculate the launch angle from vertical given
    velocity ratio and target altitude ratio.
    """
    sin_launch_angle = (1 + alpha) * np.sqrt(1 - (alpha / (1 + alpha)) * (ve_v0**2))
    launch_angle = arcsin(sin_launch_angle)
    return launch_angle #return as the radian of the launch angle


def launch_angle_range(ve_v0, alpha, tol_alpha):
    """Calculate the range of launch angles for a given
    velocity ratio, target altitude ratio, and tolerance.
    """
    max_altitude_ratio_min_launch_angle = (1 + tol_alpha) * alpha
    max_launch_angle = launch_angle(ve_v0, max_altitude_ratio_min_launch_angle)
    max_altitude_ratio_max_launch_angle = (1 - tol_alpha) * alpha
    min_launch_angle = launch_angle(ve_v0, max_altitude_ratio_max_launch_angle)
    launch_angle_range = np.array([max_launch_angle, min_launch_angle])
    return launch_angle_range


def min_altitude_ratio(ve_v0):  
    """Utility function for computing minimum possible peak altitude ratio
    for a given velocity ratio.
    """
    alpha = -(ve_v0**2 - 2) / (ve_v0**2 - 1)
    #make sure alpha is not greater than 1
    
    return alpha

def max_altitude_ratio(ve_v0):
    """Utility function for computing maximum possible peak altitude ratio
    for a given velocity ratio.
    """
    alpha = 1/((ve_v0**2)-1)
    return alpha 


def min_velocity_ratio(alpha):
    """Utility function for computing minimum possible velocity ratio
    for a given target peak altitude ratio.
    """
    ve_v0 = np.sqrt((2 + alpha) / (1 + alpha))
    return ve_v0


def max_velocity_ratio(alpha):
    """Utility function for computing maximum possible velocity ratio
    for a given target peak altitude ratio.
    """
    ve_v0 = np.sqrt((1 + alpha) / alpha)
    return 