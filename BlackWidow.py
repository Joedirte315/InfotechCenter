print("\n********************************************************\n")
print("Gasoline Branch - Developer: Joseph Nuyen\n")

import random
from time import sleep

def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

def gasStations():
    gasStationsList = ["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ee's"]
    return random.choice(gasStationsList)

def gasLevelAlert():
    milesToGasStationLow = random.uniform(1,25)
    milesToGasStationQuarterTank = random.uniform(25.1,50)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("You outta gas bub\n")
        sleep(1.25)
        print("Calling AAA")

    elif gasLevelIndicator == "Low":
        print("You bouta haseth zero gasoline particles in yo tank cuh, checking GPS so you can find a gas place")
        sleep(1.25)
        print("Closest gas place is", gasStations(), "which is", milesToGasStationLow, "miles away")
    
    elif gasLevelIndicator == "Quarter Tank":
        print("Gang you finna run outta 8 Carbon molecules and 18 Hydrogen molecules but you have some time to get to a petrol station")
        sleep(1.25)
        print("Closest petrol station is", gasStations(), "which is", milesToGasStationQuarterTank, "kilometers away")

    elif gasLevelIndicator == "Half Tank":
        print("You got half a tank so you chillin fr fr ong no cap")

    elif gasLevelIndicator == "Three Quarter Tank":
        print("You got three quarters of a tank so we be bussin bussin")

    else gasLevelIndicator == "Full Tank":
        print("You gasohol holder is full gang, no more petrol station for u")

gasLevelAlert()
