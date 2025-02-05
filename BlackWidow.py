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

print (weather())