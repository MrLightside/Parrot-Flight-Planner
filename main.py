import json


def _auto_indict(key, x):
    if len(x) != 0 or not None:
        y = []
        for a in x:
            y.append(a.indict())
        y = {key: y}
    else:
        y = {}
    return y


def _combine_dicts(*args):
    o = {}
    for k in args:
        o = o | k
    return o


def json_export(x):
    return json.dumps(x.indict())


class Plan:
    def __init__(self,
                 takeoff=None,
                 poi=None,
                 way_points=None
                 ):

        if takeoff is None:
            takeoff = []
        if poi is None:
            poi = []
        if way_points is None:
            way_points = []

        self.takeoff = takeoff
        self.poi = poi
        self.way_points = way_points

    def indict(self):
        a = _auto_indict("takeoff", self.takeoff)
        b = _auto_indict("poi", self.poi)
        c = _auto_indict("wayPoints", self.way_points)
        o = _combine_dicts(a, b, c)

        return o


class WayPoint:
    def __init__(self,
                 latitude,
                 longitude,
                 altitude,
                 yaw,
                 speed=5,
                 poi=0,
                 continue_way_point=True,
                 follow_poi=False,
                 follow=0,
                 last_yaw=0,
                 actions=None
                 ):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.yaw = yaw
        self.speed = speed
        self.poi = poi
        self.continue_way_point = continue_way_point
        self.follow_poi = follow_poi
        self.follow = follow
        self.last_yaw = last_yaw
        self.actions = actions

    @property
    def longitude(self):
        return float(self._longitude)

    @longitude.setter
    def longitude(self, x):
        x = float(x)
        if not -180 <= x <= 180:
            raise ValueError("Longitude value must be equal to or between -180 and 180.")
        self._longitude = x

    @property
    def latitude(self):
        return float(self._latitude)

    @latitude.setter
    def latitude(self, x):
        x = float(x)
        if not -90 <= x <= 90:
            raise ValueError("Latitude value must be equal to or between -90 and 90.")
        self._latitude = x

    @property
    def altitude(self):
        return float(self._latitude)

    @altitude.setter
    def altitude(self, x):
        if isinstance(x, int):
            if 0 <= x:
                self._altitude = x
            else:
                raise ValueError("Altitude value must be more than 0.")
        else:
            raise ValueError("Altitude value must be an integer data type.")

    @property
    def yaw(self):
        return float(self._yaw)

    @yaw.setter
    def yaw(self, x):
        if isinstance(x, int):
            self._yaw = x
        else:
            raise ValueError("Yaw value must be an integer data type.")

    @property
    def speed(self):
        return float(self._speed)

    @speed.setter
    def speed(self, x):
        if isinstance(x, int):
            self._speed = x
        else:
            raise ValueError("Speed value must be an integer data type.")

    @property
    def poi(self):
        return float(self._poi)

    @poi.setter  # TODO: Add check for poi existing.
    def poi(self, x):
        if isinstance(x, int):
            self._poi = x
        else:
            raise ValueError("POI value must be an integer data type.")

    @property
    def continue_way_point(self):
        return float(self._continue_way_point)

    @continue_way_point.setter
    def continue_way_point(self, x):
        if isinstance(x, bool):
            self._continue_way_point = x
        elif isinstance(x, int):
            self._continue_way_point = bool(x)
        else:
            raise ValueError("Continue Way Point value must be a valid boolean.")

    @property
    def follow_poi(self):
        return float(self._follow_poi)

    @follow_poi.setter
    def follow_poi(self, x):
        if isinstance(x, bool):
            self._follow_poi = x
        elif isinstance(x, int):
            self._follow_poi = bool(x)
        else:
            raise ValueError("Follow POI value must be a valid boolean.")

    @property
    def follow(self):
        return float(self._follow)

    @follow.setter
    def follow(self, x):
        if isinstance(x, int):
            self._follow = x
        else:
            raise ValueError("Follow value must be an integer data type.")

    @property
    def last_yaw(self):
        return float(self._last_yaw)

    @last_yaw.setter
    def last_yaw(self, x):
        if isinstance(x, int):
            self._last_yaw = x
        else:
            raise ValueError("Last Yaw value must be an integer data type.")

    def indict(self):
        x = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "altitude": self.altitude,
            "yaw": self.yaw,
            "speed": self.speed,
            "continue": self.continue_way_point,
            "followPOI": self.follow_poi,
            "follow": self.follow,
            "lastYaw": self.last_yaw,
        }

        y = _auto_indict("actions", self.actions)
        o = _combine_dicts(x, y)

        return o


class Action:
    def __init__(self,
                 event_type,
                 **kwargs,
                 ):
        self.event_type = event_type
        self.arguments = kwargs  # Potential placeholder solution until all action classes created?

    def indict(self):
        x = {"event_type": self.event_type}
        y = self.arguments
        o = x | y
        return o


class FlightPlan:
    def __init__(self,
                 title,
                 product='ANAFI_4K',
                 product_id=0,
                 date=0,
                 progressive_course_activated=True,
                 dirty=False,
                 longitude=0.0,
                 latitude=0.0,
                 longitude_delta=0.0,
                 latitude_delta=0.0,
                 zoom_level=0.0,
                 rotation=0.0,
                 tilt=0.0,
                 map_type=4,
                 plan=None
                 ):
        if plan is None:
            plan = Plan()

        self.version = 1  # Integer
        self.title = title  # String :: Flight Plan Title.
        self.product = product  # String :: Drone model.
        self.product_id = product_id  # Integer :: Product ID associated with drone model.
        self.uuid = title  # String
        self.date = date  # Integer :: Epoch time.
        self.progressive_course_activated = progressive_course_activated  # Boolean :: Calculation between way points.
        self.dirty = dirty  # Boolean :: Not a clue.
        self.longitude = longitude  # Float :: ??
        self.latitude = latitude  # Float :: ??
        self.longitude_delta = longitude_delta  # Float :: Map Zoom (Potentially).
        self.latitude_delta = latitude_delta  # Float :: Map Zoom (Potentially).
        self.zoom_level = zoom_level  # Float :: Map Zoom (Potentially).
        self.rotation = rotation  # Float :: ??
        self.tilt = tilt  # Float :: Camera Tilt.
        self.map_type = map_type  # Integer ::
        self.plan = plan  # List ::

    @property
    def version(self):
        return int(self._longitude)

    @version.setter
    def version(self, x):  # Unknown valid version range.
        x = int(x)
        if not x > 0:
            raise ValueError("Version value must be more than 0.")
        self._version = x

    @property
    def title(self):
        return int(self._title)

    @title.setter
    def title(self, x):
        x = str(x)
        self._title = x

    @property
    def product(self):
        return int(self._product)

    @product.setter
    def product(self, x):
        x = str(x)
        self._product = x

    @property
    def product_id(self):
        return int(self._product_id)

    @product_id.setter
    def product_id(self, x):
        x = int(x)
        if not x > 0:
            raise ValueError("Product ID value must be more than 0.")
        self._product_id = x

    @property
    def uuid(self):
        return int(self._uuid)

    @uuid.setter
    def uuid(self, x):
        x = str(x)
        self._uuid = x

    @property
    def date(self):
        return int(self._date)

    @date.setter
    def date(self, x):
        x = int(x)
        if not x > -1:
            raise ValueError("Date value must be a valid epoch time.")
        self._date = x

    @property
    def progressive_course_activated(self):
        return int(self._progressive_course_activated)

    @progressive_course_activated.setter
    def progressive_course_activated(self, x):
        if isinstance(x, bool):
            self._progressive_course_activated = x
        elif isinstance(x, int):
            self._progressive_course_activated = bool(x)
        else:
            raise ValueError("Progressive Course Activated value must be a valid boolean.")

    @property
    def dirty(self):
        return int(self._dirty)

    @dirty.setter
    def dirty(self, x):
        if isinstance(x, bool):
            self._dirty = x
        elif isinstance(x, int):
            self._dirty = bool(x)
        else:
            raise ValueError("Dirty value must be a valid boolean.")

    @property
    def longitude(self):
        return float(self._longitude)

    @longitude.setter
    def longitude(self, x):
        x = float(x)
        if not -180 <= x <= 180:
            raise ValueError("Longitude value must be equal to or between -180 and 180.")
        self._longitude = x

    @property
    def latitude(self):
        return float(self._latitude)

    @latitude.setter
    def latitude(self, x):
        x = float(x)
        if not -90 <= x <= 90:
            raise ValueError("Latitude value must be equal to or between -90 and 90.")
        self._latitude = x

    @property
    def longitude_delta(self):
        return float(self._longitude_delta)

    @longitude_delta.setter
    def longitude_delta(self, x):
        if isinstance(x, (int, float)):
            self._longitude_delta = float(x)
        else:
            raise ValueError("Longitude Delta value must be a float data type.")

    @property
    def latitude_delta(self):
        return float(self._latitude_delta)

    @latitude_delta.setter
    def latitude_delta(self, x):
        if isinstance(x, (int, float)):
            self._latitude_delta = float(x)
        else:
            raise ValueError("Latitude Delta value must be a float data type.")

    @property
    def zoom_level(self):
        return float(self._zoom_level)

    @zoom_level.setter
    def zoom_level(self, x):
        if isinstance(x, int):
            if x > -1:
                self._zoom_level = x
            else:
                raise ValueError("Zoom Level value must be a positive number.")
        else:
            raise ValueError("Zoom Level value must be an integer data type.")

    @property
    def rotation(self):
        return float(self._rotation)

    @rotation.setter  # Unknown valid data range.
    def rotation(self, x):
        if isinstance(x, int):
            self._rotation = x
        else:
            raise ValueError("Rotation value must be an integer data type.")

    @property
    def tilt(self):
        return float(self._tilt)

    @tilt.setter
    def tilt(self, x):
        if isinstance(x, (int, bool)):
            if -90 <= x <= 90:
                self._tilt = x
            else:
                raise ValueError("Tilt value must be between range -90 and 90.")
        else:
            raise ValueError("Tilt value must be a boolean data type.")

    @property
    def map_type(self):
        return float(self._map_type)

    @map_type.setter
    def map_type(self, x):
        if isinstance(x, int):
            if 1 <= x <= 4:
                self._map_type = x
            else:
                raise ValueError("Map Type value must be between range 1 and 4.")
        else:
            raise ValueError("Map Type value must be an integer data type.")

    def indict(self):
        x = {
            "version": self.version,
            "title": self.title,
            "product": self.product,
            "productId": self.product_id,
            "uuid": self.uuid,
            "date": self.date,
            "progressive_course_activated": self.progressive_course_activated,
            "dirty": self.dirty,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "longitudeDelta": self.longitude_delta,
            "latitudeDelta": self.latitude_delta,
            "zoomLevel": self.zoom_level,
            "rotation": self.rotation,
            "tilt": self.tilt,
            "mapType": self.map_type,
        }

        y = {"plan": self.plan.indict()}
        o = _combine_dicts(x, y)

        return o


if __name__ == '__main__':
    new_fp = FlightPlan("Base Flight Plan")

    new_fp.latitude = -90
    print(new_fp.latitude)
