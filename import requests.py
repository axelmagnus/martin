import requests
import json
import turtle
from datetime import datetime

# Retrieve data from the API
url = "http://api.openweathermap.org/data/2.5/forecast?q=Malmo,%20SE&appid=4acdd2457856e1ef6c064f1e928ea71e&cnt=8"
response = requests.get(url)
data = json.loads(response.text)

# Map weather conditions to corresponding icons
weather_icons = {
    "Clouds": "☁️",
    "Rain": "🌧️",
    "Overcast": "☁️",
    "Clear": "☀️",
    "Drizzle": "🌦️"
}
#print("data", data['list'])
datalist = data['list'][:]
max_temp = max(data['main']['temp']-273.15 for data in datalist)
print("max_temp", max_temp)
min_temp = min(data['main']['temp']-273.15 for data in datalist)
print("min_temp", min_temp)

#print("datalist", datalist)#[:]['main']['temp'])
# Extract relevant information from the data
current_weather = data["list"][0]["weather"][0]["main"]
#current_weather = "Drizzle"
current_time = data["list"][0]["dt_txt"][:16]
print("current_time", current_time)
temp_min = data["list"][0]["main"]["temp_min"]
temp_max = data["list"][0]["main"]["temp_max"]
sunrise_unix = data["city"]["sunrise"]
# Convert sunrise time from Unix epoch to hour:minute format
sunrise = datetime.fromtimestamp(sunrise_unix).strftime("%H:%M")
sunset_unix = data["city"]["sunset"]
# Convert sunrise time from Unix epoch to hour:minute format
sunset = datetime.fromtimestamp(sunset_unix).strftime("%H:%M")
rain_chance = data["list"][0]["pop"]

# Convert temperatures from Kelvin to Celsius
temp_min = round(temp_min - 273.15, 2)
temp_max = round(temp_max - 273.15, 2)

# Set up Turtle graphics
screen = turtle.Screen()
screen.title("Weather Information")
screen.setup(width=450, height=400)
screen.bgcolor("lightblue")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("black")
pen.speed(1)

# Display current time
pen.goto(screen.window_width()/2-10,-screen.window_height()/2+10)
pen.write("Forecast Time: {}".format(current_time), align="right", font=("Arial", 12, "normal"))

#Display city name  
pen.goto(-screen.window_width()/2+5,-screen.window_height()/2+10)
pen.write("{}".format(data["city"]["name"]), align="left", font=("Arial", 12, "normal"))

# Display current weather with icon
pen.goto(0, -90)
if current_weather in weather_icons:
    pen.write(weather_icons[current_weather],
              align="center", font=("Arial", 300, "normal"))
else:
    pen.write("Current Weather: {}".format(current_weather), align="left", font=("Arial", 16, "bold"))

pen.goto(0, 80)
icon_pos = pen.pos()
pen.write("{}".format(current_weather), align="center", font=("Arial", 26, "bold"))
# Display temperature range
pen.goto(0, 120)
pen.write("{:.1f} - {:.1f}°C".format(float(temp_min), float(temp_max)), align="center", font=("Arial", 26, "bold"))

# Display sunrise time
pen.goto(0, -40)
pen.write("Sunrise: {}  Sunset: {}".format(sunrise, sunset),
          align="center", font=("Helvetica", 16, "normal"))

# Display rain chance
pen.goto(0, 60)
rain_chance = data["list"][0]["pop"]
pen.write("PoP: {} %".format(rain_chance) , "%", align="center", font=("Arial", 16, "bold"))

#find out at what times the min and max temp will occur with .index
min_temp_time = datalist[[data['main']['temp']-273.15 for data in datalist].index(min_temp)]['dt_txt'][:16]
print("min_temp_time", min_temp_time)
max_temp_time = datalist[[data['main']['temp']-273.15 for data in datalist].index(max_temp)]['dt_txt'][:16]
print("max_temp_time", max_temp_time)
#get the hour and minute from the time
min_temp_time = min_temp_time[11:]
max_temp_time = max_temp_time[11:]

#Display max and min temp at 100,-40 with 0 decimals and at what time that temperatue will occur

pen.goto(-170, -110)
pen.write("HI:  {:.0f}°  @ {}".format(max_temp, max_temp_time), align="left", font=("Cambria", 36, "normal"))
pen.goto(-170, -145)
pen.write("LO: {:.0f}°  @ {}".format(min_temp, min_temp_time),
          align="left", font=("Cambria", 36, "normal"))

#make a line graph of the temperature

datalist = data['list'][:]
tempvals = [data['main']['temp'] - 273.15 for data in datalist]

screen.exitonclick()
#turtle.done()
