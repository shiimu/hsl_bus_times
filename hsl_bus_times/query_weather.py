from pymongo import MongoClient
import requests
import json

client = MongoClient('localhost', 27017)
db = client['weather_info']
collection = db['weather_collection']

def queryApi():
    getSecret()

    url = "https://api.openweathermap.org/data/2.5/weather?lat=60.23787364561019&lon=25.10560957759351&appid="+ key + ""
    payload = {"query": '{\n "weather": {'}
    headers = {"Content-Type" : "application/json"}
    response = requests.get(url, headers=headers, data = json.dumps(payload))
    
    dumped_weather = response.json()

def weatherToDB():
    collection.insert(dumped_weather)

def getSecret():
    global key

    collection = db['weather_key']
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
