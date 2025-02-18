import random
from time import sleep

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
    gas_level = gasLevelGauge()
    station = gasStations()

    # Dictionary mapping gas levels to corresponding messages
    messages = {
        "Empty": ("You outta gas bub\n", "Calling AAA"),
        "Low": (f"You bouta haseth zero gasoline particles in yo tank cuh, checking GPS...",
                f"Closest gas place is {station}, which is {random.uniform(1, 25):.2f} miles away"),
        "Quarter Tank": (f"Gang you finna run outta 8 Carbon molecules and 18 Hydrogen molecules, "
                         f"but you have time to get to a petrol station.",
                         f"Closest petrol station is {station}, which is {random.uniform(25.1, 50):.2f} kilometers away"),
        "Half Tank": ("You got half a tank so you chillin fr fr ong no cap",),
        "Three Quarter Tank": ("You got three quarters of a tank so we be bussin bussin",),
        "Full Tank": ("Your gasohol holder is full gang, no more petrol station for u",)
    }

    # Print the corresponding message
    for msg in messages[gas_level]:
        print(msg)
        sleep(1.25)  # Simulate delay for realism


gasLevelAlert()
