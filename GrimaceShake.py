print("\n***********************************************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

#Create a function that randomly chooses the weather from a list
def weather():
    weatherForecast = ["Snowing", "Blizzards", "Raining", "Foggy", "Windy", "Icy", "Sunny"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

print(weather())