init python:
    from enum import Enum

    class Location(str, Enum):
        OTHER = "Other"
        HOME = "Home"
        STREET = "Downtown Streets"
        PARK = "Park"
        CAFE = "Cafe"
        THERAPY = "Therapy Office"

    class LocationData():
        def __init__(self, name: str, on_map = False, position: (float, float) = None):
            self.name = name
            self.on_map = on_map
            self.position = position

    LOCATION_DATA = {
        Location.OTHER: LocationData(name=Location.OTHER.value),
        Location.HOME: LocationData(name=Location.OTHER.value, on_map=True),
        Location.STREET: LocationData(name=Location.OTHER.value),
        Location.PARK: LocationData(name=Location.OTHER.value),
        Location.CAFE: LocationData(name=Location.OTHER.value),
        Location.THERAPY: LocationData(name=Location.OTHER.value)
    }
