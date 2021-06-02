import requests
import configparser

userzip = input("Enter your Zip Code Please: ")


def get_api_key():
	config = configparser.ConfigParser()
	config.read('config.ini')
	print(config.get('openweathermap', 'api'))
    # return config['openweathermap']['api']
    # return config.get('ope')

def get_weather_results(zip_code, api_key):
	api_url = "https://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}".format(zip_code, api_key)
	r = requests.get(api_url)
	return r.json()
	
print(get_weather_results(userzip, get_api_key())