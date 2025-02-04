# Import necessary libraries
import sys  # Provides access to system-specific parameters and functions
import time  # Provides functions for time-related tasks (e.g., pausing the program)

# Display developer information
print("Welcome Branch - Developer: Joseph Nuyen")

# Display the version of the InfoTechCenter system
print("\nWelcome to InfoTechCenter V1.0")

# Initialize the counter variable for the loop and the ellipsis counter
x = 0  # Loop counter to track how many iterations have occurred
ellipsis = 0  # This will control how many dots to display in the booting message

# Start a loop that runs 20 times to simulate the system boot process
while x != 20:
    x += 1  # Increment the loop counter by 1 on each iteration
    # Construct the booting message with an increasing number of dots (ellipsis)
    message = ("Infotech Center System Booting" + "." * ellipsis)
    ellipsis += 1  # Increment the number of dots for the next iteration
    # Print the message, overwriting the previous output to simulate a progress indicator
    sys.stdout.write("\r" + message)
    time.sleep(0.5)  # Wait for half a second before the next iteration
    
    # Reset the number of dots after reaching 4 to start the sequence again
    if ellipsis == 4:
        ellipsis = 0
    
    # When the loop reaches 20 iterations, print the final boot-up success message
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted\n")



