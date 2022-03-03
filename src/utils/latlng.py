from utils import geo


class LatLng:
    def __init__(self, lat, lng):
        self.__lat__ = lat
        self.__lng__ = lng

    @property
    def lat(self):
        return self.__lat__

    @property
    def lng(self):
        return self.__lng__

    @property
    def raw(self):
        return [self.__lat__, self.__lng__]

    def __str__(self):
        return f'({self.lat:.6f}, {self.lng:.6f})'

    def distance(self, other):
        return geo.get_distance(self.raw, other.raw)


class Polygon:
    def __init__(self, latlng_list):
        self.__latlng_list__ = latlng_list
