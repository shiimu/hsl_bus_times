import requests
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['hsl_bus_times']
collection = db['bus_collection']


def queryApi(stop_id):
    url = "https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"
    payload = {"query": "{\n  stop(id: \"" + stop_id +
               "\") {  name   stoptimesWithoutPatterns{realtimeDeparture    serviceDay   headsign trip{route{ shortName}}}}}"}
    headers = {"Content-Type": "application/json"}
    response = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload))

    global dumped_data
    dumped_data = response.json()
    # ADD TO DB
    busToDB()


def busToDB():
    collection.insert(dumped_data)
