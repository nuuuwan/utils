import os

import googlemaps


def get_api_key():
    return os.environ['GOOGLE_API_KEY']


class GoogleMaps:
    def __init__(self):
        gmaps_api_key = get_api_key()
        self.api = googlemaps.Client(key=gmaps_api_key)

    def get_latlng(self, address):
        geocode = self.api.geocode(address)
        location = geocode[0]['geometry']['location']
        return [location['lat'], location['lng']]

    def get_address(self, latlng):
        rev_geocode = self.api.reverse_geocode(latlng)
        return rev_geocode[0]['formatted_address']
