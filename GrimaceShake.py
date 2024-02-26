print("\n***********************************************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

#Create a function that randomly chooses the weather from a list
def weather():
    weatherForecast = ["snowy", "blizzard", "rainy", "foggy", "windy", "icy", "sunny"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

#Variable to call the weather() once VRS(Vehicle Response System) is determined.
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        print("VRS has been emgaged only allowing you to drive 50mps")
    elif weatherAlert == "blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        print("VRS has been emgaged only allowing you to drive 40mps")
    elif weatherAlert == "rainy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        print("VRS has been emgaged only allowing you to drive 60mps")
    elif weatherAlert == "foggy":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        print("VRS has been emgaged only allowing you to drive 40mps")
    elif weatherAlert == "windy":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        print("VRS has been emgaged only allowing you to drive 40mps")
    elif weatherAlert == "icy":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        print("VRS has been emgaged only allowing you to drive 40mps")
    else:
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        print("VRS has been emgaged only allowing you to drive 40mps")


vehicleResponseSystem()