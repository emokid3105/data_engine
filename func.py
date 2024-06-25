import requests
from googletrans import Translator
def get_temperature(place):

    api_key= 'zo62yqkcez0nd7rd75d0sl240916ssscwz3av20g'
    location = place.lower()

    parameters = {'key': api_key,
              'place_id': location}

    url = "https://www.meteosource.com/api/v1/free/point"
    data = requests.get(url, parameters).json()
    result = data['current']['temperature']

    return f'Temperature in {place.capitalize()} is {result} C'

