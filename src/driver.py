import numpy as np
import matplotlib.pyplot as plt


from launch import (launch_angle_range,
                    min_altitude_ratio, 
                    max_altitude_ratio, 
                    min_velocity_ratio, 
                    max_velocity_ratio
)

def main():
    """Plot launch angle ranges given
    values for ve_v0, alpha, and tol_alpha.
    """
    # plot launch angle range for a fixed velocity ratio
    ve_v0 = 0.2
    tol_alpha = 0.04
    min_alpha = min_altitude_ratio(ve_v0)
    max_alpha = max_altitude_ratio(ve_v0)
    alpha_range = np.linspace(min_alpha, max_alpha, 100)
    y = launch_angle_range
    plt.plot(x,y)
    
    








    # plot launch angle range for a fixed target altitude
    
    

if __name__ == "__main__":
    main()