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
