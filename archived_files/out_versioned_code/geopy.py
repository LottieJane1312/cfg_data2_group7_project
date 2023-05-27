# !pip install geopy

import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Create a geolocator object using Nominatim with a custom user agent
geolocator = Nominatim(user_agent='test_tk')

# Function to reverse geocode coordinates to borough
def reverse_geocode(lat, lon, geolocator):
    location = None
    while not location:
        try:
            location = geolocator.reverse(f"{lat}, {lon}", exactly_one=True)
            if location is None:
                print(f"No location found for coordinates: {lat}, {lon}")
                return None
            address = location.raw['address']
            borough = address.get('city_district') or address.get('suburb')
            if borough is not None:
                borough = borough.replace(' ', '_')  # Replace whitespaces with underscores
        except (GeocoderTimedOut, KeyError):
            continue
    return borough
