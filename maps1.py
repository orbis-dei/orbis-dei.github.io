# coding: utf-8
# %load maps.py
import requests


def get_country(data):
    for entry in data['address_components']:
        if 'country' in entry['types']:
            return entry['long_name']

def get_place_info(place_name):
    # Replace '<API_KEY>' with a valid Google Maps API key
    api_key = '<API_KEY>'
    base_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={place_name}&key={api_key}"
    # print(base_url)

    # Send request to geocoding API (replace with a more reliable source if needed)
    response = requests.get(base_url)
    data = response.json()

    # # Check for successful response and extract coordinates
    # if data['status'] == 'OK':
    #     location = data['results'][0]['geometry']['location']
    #     info['latitude'] = location['lat']
    #     info['longitude'] = location['lng']
    
    try:
        place_id = data['results'][0]['place_id']
    except Exception:
        print(data)
        raise
    place_url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={api_key}'
    place_data = requests.get(place_url).json()['result']


    rv = [
        get_country(place_data),
        '',
        place_data['geometry']['location']['lat'],
        place_data['geometry']['location']['lng'],
        place_data['name'],
        place_data['name'],
        place_data.get('editorial_summary', {}).get('overview', ''),
        place_data.get('website', ''),
        ]
    print('|'.join(str(x) for x in rv))

