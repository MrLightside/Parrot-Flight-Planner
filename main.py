import json
import datatypes as dt


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
        self.continue_way_point = continue_way_point
        self.follow_poi = follow_poi
        self.follow = follow
        self.last_yaw = last_yaw
        self.actions = actions

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
    t = dt.Latitude(76.43926926794)
    FlightPlan("Base Flight Plan")
