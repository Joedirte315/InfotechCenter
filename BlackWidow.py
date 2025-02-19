
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

import random  # Importing random module for random selections
from time import sleep  # Importing sleep to add delays for realism

# Displaying program header
print("\n********************************************************\n")
print("Gasoline Branch - Developer: Joseph Nuyen\n")

def gasLevelGauge():
    """Returns a random gas level from predefined states."""
    return random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"])

def gasStations():
    """Returns a random gas station from the list."""
    return random.choice(["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ee's"])

def gasLevelAlert():
    """Checks gas level and provides an appropriate alert."""
    gas_level = gasLevelGauge()  # Get a random gas level
    station = gasStations()  # Get a random gas station

    # Dictionary mapping gas levels to corresponding messages
    messages = {
        "Empty": (
            "You outta gas bub\n",  # Alert when the tank is empty
            "Calling AAA"  # Suggest calling roadside assistance
        ),
        "Low": (
            "You bouta haseth zero gasoline particles in yo tank cuh, checking GPS...",
            f"Closest gas place is {station}, which is {random.uniform(1, 25):.2f} miles away"
        ),
        "Quarter Tank": (
            "Gang you finna run outta 8 Carbon molecules and 18 Hydrogen molecules, "
            "but you have time to get to a petrol station.",
            f"Closest petrol station is {station}, which is {random.uniform(25.1, 50):.2f} kilometers away"
        ),
        "Half Tank": ("You got half a tank so you chillin fr fr ong no cap",),  # No urgent action needed
        "Three Quarter Tank": ("You got three quarters of a tank so we be bussin bussin",),  # Plenty of fuel left
        "Full Tank": ("Your gasohol holder is full gang, no more petrol station for u",)  # No need to refuel
    }

    # Print the corresponding message based on gas level
    for msg in messages[gas_level]:
        print(msg)
        sleep(1.25)  # Adding a slight delay for realism

# Call the function to check gas level and display alerts
gasLevelAlert()

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


