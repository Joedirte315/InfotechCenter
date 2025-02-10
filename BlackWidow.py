# Print a decorative separator line
print("\n*****************************************\n")

# Print the Weather Branch developer information
print("Weather Branch - Developer: Joseph Nuyen\n")

# Import necessary libraries
import random  # For generating random weather conditions
from time import sleep  # For adding delays (though not used in this code)

# Weather function to determine the current weather condition
def weather():
    # List of possible weather conditions
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny", "Nagasaki"]
    # Randomly choose one of the weather conditions from the list
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition  # Return the randomly selected weather condition

# Store the selected weather condition into the variable `weatherAlert`
weatherAlert = weather()

# Function to handle vehicle response based on the weather condition
def vehiclesResponseSystem():
    # Check for different weather conditions and respond accordingly
    if weatherAlert == "snowing":
        print("\nThe National Weather Service has updated your alarm by 30 minutes because"
              " of the forecast of the ", weatherAlert , " weather condition.")
    
    # Special case for the "Nagasaki" condition (could be a humorous or placeholder entry)
    elif weatherAlert == "Nagasaki":
        print("\nYou're probably gonna die because it's", weatherAlert , "2.0")

    # Handle other common weather conditions in a similar manner
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated your alarm by 30 minutes because"
              " of the forecast of the ", weatherAlert , " weather condition.")
    
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated your alarm by 30 minutes because"
              " of the forecast of the ", weatherAlert , " weather condition.")
    
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated your alarm by 30 minutes because"
              " of the forecast of the ", weatherAlert , " weather condition.")
    
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated your alarm by 30 minutes because"
              " of the forecast of the ", weatherAlert , " weather condition.")
    
    elif weatherAlert == "sunny":
        print("\nThe National Weather Service has updated your alarm by 30 minutes because"
              " of the forecast of the ", weatherAlert , " weather condition.")

# Call the function to execute the vehicle response based on the weather condition
vehiclesResponseSystem()
