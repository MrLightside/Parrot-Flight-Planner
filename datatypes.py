class Longitude:
    def __init__(self, longitude=0):
        self.longitude = longitude

    @property
    def longitude(self):
        return float(self._longitude)

    @longitude.setter
    def longitude(self, x):
        x = float(x)
        if not -180 <= x <= 180:
            raise ValueError("Longitude value must be equal to or between -180 and 180.")
        self._longitude = x

    def __repr__(self):
        return str(self._longitude)


class Latitude:
    def __init__(self, latitude=0):
        self.latitude = latitude

    @property
    def latitude(self):
        return float(self._latitude)

    @latitude.setter
    def latitude(self, x):
        x = float(x)
        if not -90 <= x <= 90:
            raise ValueError("Latitude value must be equal to or between -90 and 90.")
        self._latitude = x

    def __repr__(self):
        return str(self._latitude)

    def __call__(self):
        return float(self._latitude)