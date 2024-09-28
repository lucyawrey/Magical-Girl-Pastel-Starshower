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
        Location.HOME: LocationData(name=Location.HOME.value, on_map=True, position=(0.5, 0.51)),
        Location.STREET: LocationData(name=Location.STREET.value, on_map=True, position=(0.5, 0.52)),
        Location.PARK: LocationData(name=Location.PARK.value, on_map=True, position=(0.5, 0.53)),
        Location.CAFE: LocationData(name=Location.CAFE.value, on_map=True, position=(0.5, 0.54)),
        Location.THERAPY: LocationData(name=Location.THERAPY.value, on_map=True, position=(0.5, 0.55))
    }
