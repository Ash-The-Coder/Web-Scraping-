import requests, json
api_key = "458dfb8e4cdfbefe1b1c95aa4b565e14"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
 
# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
 
# get method of requests module
# return response object
response = requests.get(complete_url).json()
a = response.keys()
for i in a:
    print(f" {i} = {response[i]}")
    