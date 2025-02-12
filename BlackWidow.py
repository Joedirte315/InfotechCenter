# Import necessary libraries
import sys  # Provides access to system-specific parameters and functions
import time  # Provides functions for time-related tasks (e.g., pausing the program)
import random
from time import sleep


# ANSI escape sequences for coloring the text
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"  # Reset to default color

# Display developer information in green
print(f"{GREEN}Welcome Branch - Developer: Joseph Nuyen{RESET}")

# Display the system version in yellow
print(f"\n{YELLOW}Welcome to InfoTechCenter V1.0{RESET}")

# Initialize the counter variable for the loop and the ellipsis counter
x = 0  # Loop counter to track how many iterations have occurred
ellipsis = 0  # This will control how many dots to display in the booting message

# Start a loop that runs 20 times to simulate the system boot process
while x != 20:
    x += 1  # Increment the loop counter by 1 on each iteration
    # Construct the booting message with an increasing number of dots (ellipsis)
    message = f"{YELLOW}Infotech Center System Booting{RESET}" + "." * ellipsis
    ellipsis += 1  # Increment the number of dots for the next iteration
    # Print the message in red, overwriting the previous output to simulate progress
    sys.stdout.write(f"\r{RED}{message}{RESET}")
    time.sleep(0.5)  # Wait for half a second before the next iteration
    
    # Reset the number of dots after reaching 4 to start the sequence again
    if ellipsis == 4:
        ellipsis = 0
    
    # When the loop reaches 20 iterations, print the final boot-up success message
    if x == 20:
        print(f"\n\n{GREEN}Operating System Booted Up - Retina Scanned - Access Granted{RESET}\n")

# Print a decorative separator line
print("\n*****************************************\n")
print("Weather Branch - Developer: Joseph Nuyen")

# Import necessary libraries
import random  # For generating random weather conditions

# Weather function to determine the current weather condition
def weather():
    # List of possible weather conditions
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny", "Nagasaki"]
    # Randomly choose one of the weather conditions from the list
    return random.choice(weatherForecastList)  # Return the randomly selected weather condition

# Function to handle vehicle response based on the weather condition
def vehiclesResponseSystem(weatherCondition):
    # Common message template
    message = "\nThe National Weather Service has updated your alarm by 30 minutes because of the forecast of the {} weather condition."
    print(message.format(weatherCondition))

    # Handle response based on specific weather condition
    if weatherCondition == "Nagasaki":
        print("You're probably gonna die because it's {} 2.0".format(weatherCondition))
    else:
        print("WRS has been engaged only allowing us to drive 55mph.")

# Store the selected weather condition into the variable `weatherAlert`
weatherAlert = weather()

# Call the function to execute the vehicle response based on the weather condition
vehiclesResponseSystem(weatherAlert)

