print("******************************************")
print("Gasoline Branch\n\n")

#Import Libararies Here
import random
from time import sleep      



#Function that list Gas Levels, randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Three Quarter Tank", "Full Tank"]
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




gasLevelAlert()