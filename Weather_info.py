import requests
# to request weather information
from pprint import pprint
# pretty print allows the json to be viewed in a tree format

API_Key = 'cb771e45ac79a4e8e2205c0ce66ff633'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid={}&q={}".format(
    API_Key, city)
# we send requests to this url

weather_data = requests.get(base_url).json()
# we get the data from the url which has to be in json format

pprint(weather_data)
# pretty printing the weather data
