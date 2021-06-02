import pyowm #imports Python Open Weather Map to our project
import os
os.system("color") #calls color from os
# from tkinter import * #imports tkinter 
# from tkinter import ttk #


COLOR = {                     #colors
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
}
usercity = input("Enter your City Please: ")
APIKEY='a2124fb2e3e52377b9298f0e73d8274b'                  #your API Key here as string
OpenWMap=pyowm.OWM(APIKEY)                   # Use API key to get data
mgr = OpenWMap.weather_manager()
Weather=mgr.weather_at_place(usercity)  # give where you need to see the weather
w = Weather.weather  
#Data=Weather.get_weather()                   # get out data in the mentioned location
temp = w.temperature('celsius')      # get current temparature in celsius 
tempint = int(temp['temp'])
maxint = int(temp['temp_max'])
minint = int(temp['temp_min'])


# printcolor = COLOR["RED"]
if tempint  > 27:
    printcolor = COLOR["RED"]
elif tempint > 12:
    printcolor = COLOR["GREEN"]
elif tempint < 12:
    printcolor = COLOR["BLUE"]

# printcolor = COLOR["RED"]
if maxint  > 27:
    maxcolor = COLOR["RED"]
elif maxint > 12:
    maxcolor = COLOR["GREEN"]
elif maxint < 12:
    maxcolor = COLOR["BLUE"]

# printcolor = COLOR["RED"]
if minint  > 27:
    mincolor = COLOR["RED"]
elif minint > 12:
    mincolor = COLOR["GREEN"]
elif minint < 12:
    mincolor = COLOR["BLUE"]





print ("Average Temp. Currently ", printcolor,tempint,COLOR["ENDC"]) # get avg. tmp
print ("Max Temp. Currently ", maxcolor,maxint,COLOR["ENDC"]) # get max tmp
print ("Min Temp. Currently ", mincolor,minint,COLOR["ENDC"]) # get min tmp>>