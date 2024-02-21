print("******************************************")
print("Gasoline Branch\n\n")

#Import Libararies Here
import random
from time import sleep      



#Function that list Gas Levels, randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Function that lists Gas Stations, randomly choosing one and returning its value
def listOfGasStations():
    gasStations = ["Shell", "Speedway", "Marathon", "Moble", "Cosco", "Meijer", "7Eleven"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby

'''Function will call the gasLevelGauge ti determine our gas level and then find a close gas station
if we are on low or Quarter Tank by calling the listOfGasStations function if we are on Low or Quarter Tank'''
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1, 25), 1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1, 50), 1)
    gasLevelIndicator = gasLevelGauge()
    if  gasLevelIndicator == "Empty":
        print("***Warning - YOU ARE ON EMPTY***")
        sleep(1.25)
        print("\n     ***Call Triple AAA***")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station")
        sleep(2.5)
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationsLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter tank, checking Google Maps for the closest gas station")
        sleep(2.5)
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationsQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is a half of a tank full, which is plenty to get to your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is at Three Quarter Tank.")
     else:
        print("Your gas tank is Full.")
    
        



gasLevelAlert()
