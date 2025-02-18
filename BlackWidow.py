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
