import numpy as np
import matplotlib.pyplot as plt


from launch import (launch_angle_range,
                    min_altitude_ratio, 
                    max_altitude_ratio, 
                    min_velocity_ratio, 
                    max_velocity_ratio)

def main():
    """Plot launch angle ranges given
    values for ve_v0, alpha, and tol_alpha.
    """

    """ plot launch angle range for a fixed velocity ratio
    """
    ve_v0 = 2.0 #fixed velocity ratio
    tol_alpha = 0.04
    min_alpha = min_altitude_ratio(ve_v0) # Calculate the minimum alpha value from launch file 
    max_alpha = max_altitude_ratio(ve_v0) # Calculate the maximum alpha value from launch file
    alpha_values = np.linspace(min_alpha, max_alpha, 100)
    # create a list first and calculate launch angle ranges for each alpha value 
    launch_angle_ranges = []
    for alpha in alpha_values:
        launch_angle_range_values = launch_angle_range(ve_v0, alpha, tol_alpha)
        launch_angle_ranges.append(launch_angle_range_values)
    # Convert the list of arrays into  NumPy array in order to do the slice later  
    launch_angle_ranges = np.array(launch_angle_ranges)
    # Separate (slice) the launch angle ranges lines into max and min
    max_launch_angles = launch_angle_ranges[:, 0]
    min_launch_angles = launch_angle_ranges[:, 1]

    # Plot the max and min launch angles vs alpha
    plt.figure(figsize=(10, 5)) # set the figure size
    plt.plot(alpha_values, max_launch_angles, label='Max Launch Angle') # plot the max launch angle
    plt.plot(alpha_values, min_launch_angles, label='Min Launch Angle') # plot the min launch angle
    # label the plot
    plt.xlabel('Alpha')
    plt.ylabel('Launch Angle')
    plt.title('Alpha vs Launch Angle Range')
    plt.legend()
    # Save the plot in the figures folder
    plt.savefig("E:/goph_419/lab01/goph419-f2023-lab01-DQ/figures/launch_angle_range_vs_alpha.png")
    plt.show()


    """plot launch angle range for a fixed target altitude
    """    
    alpha  = 0.25 #fixed alpha
    tol_alpha = 0.04
    min_ve_v0 = min_velocity_ratio(alpha) # Calculate the minimum ve_v0 value from launch file
    max_ve_v0 = max_velocity_ratio(alpha) # Calculate the maximum ve_v0 value from launch file
    ve_v0_values = np.linspace(min_ve_v0, max_ve_v0, 100)
    # create a list first and calculate launch angle ranges for each ve_v0 value
    launch_angle_ranges = []
    for ve_v0 in ve_v0_values:
        launch_angle_range_values = launch_angle_range(ve_v0, alpha, tol_alpha)
        launch_angle_ranges.append(launch_angle_range_values)
    # Convert the list of arrays into  NumPy array in order to do the slice later
    launch_angle_ranges = np.array(launch_angle_ranges)
    # Separate the launch angle ranges lines into max and min
    max_launch_angles = launch_angle_ranges[:, 0]
    min_launch_angles = launch_angle_ranges[:, 1]

    # Plot the max and min launch angles vs ve_v0
    plt.figure(figsize=(10, 5)) # set the figure size
    plt.plot(ve_v0_values, max_launch_angles, label='Max Launch Angle',color='red') # plot the max launch angle
    plt.plot(ve_v0_values, min_launch_angles, label='Min Launch Angle',color='blue') # plot the min launch angle
    # label the plot 
    plt.xlabel('ve_v0')
    plt.ylabel('Launch Angle')
    plt.title('ve_v0 vs Launch Angle Range')
    plt.legend()
    # Save the plot in the figures folder
    plt.savefig("E:/goph_419/lab01/goph419-f2023-lab01-DQ/figures/Launch_angle_range_vs_ve_v0.png")
    plt.show()

if __name__ == "__main__":
    main()