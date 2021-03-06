from pymongo import MongoClient
import requests
import json

client = MongoClient('localhost', 27017)
db = client['hsl_bus_times']
collection = db['weather_collection']

def queryWeatherApi():
    getSecret()

    url = "https://api.openweathermap.org/data/2.5/weather?lat=60.23787364561019&lon=25.10560957759351&appid="+ key + ""
    payload = {"query": '{\n "weather": {'}
    headers = {"Content-Type" : "application/json"}
    response = requests.get(url, headers=headers, data = json.dumps(payload))

    global dumped_weather    
    dumped_weather = response.json()
    weatherToDB()
    
def weatherToDB():
    collection.insert_one(dumped_weather)

def getSecret():
    global key

    collection = db['api_key']
    keyv = collection.find_one({})
    keyvs = keyv['secret']

    key = keyvs

def weatherFromDB():
    global lastTemp

    queryLast = collection.find_one({})
    lastMain = queryLast['main']
    lastTemp = lastMain['temp']

    toCelsius()

def toCelsius():
    global tempInInt

    convertedTemps = lastTemp -273.15
    tempInInt = int(convertedTemps)
    dropWeather()

def dropWeather():
    if collection.count() != 0:
        collection.drop()
