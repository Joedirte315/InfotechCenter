print("\n*****************************************\n")

print("Weather Branch - Developer: Joseph Nuyen\n")

#Import Libraries Here!
import random
from time import sleep


# Weather Function to determine the weather
def weather():
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny", "Nagasaki"]
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

weatherAlert = weather()

def vehiclesResponseSystem():
    if weatherAlert == "snowing":
        print ("\nThe National Weather Service has updated your alarm by 30 minutes because"
            " of the forecast of the ", weatherAlert , " weather condition.")

    elif weatherAlert == "Nagasaki":
        print ("\nYour probably gonna die because it's", weatherAlert , " 2.0")

vehiclesResponseSystem()