init python:
    from enum import Enum

    class Location(str, Enum):
        HOME = "Home"
        RIVERWALK = "Riverwalk"
        STREET = "Downtown Streets"
        PARK = "Park"
        CAFE = "Cafe"
        THERAPY = "Therapy Office"
        OTHER = "Other"

    class LocationData():
        def __init__(self, name: str, on_map = False, position: (float, float) = None):
            self.name = name
            self.on_map = on_map
            self.position = position

    LOCATION_DATA = {
        Location.HOME: LocationData(name=Location.HOME.value, on_map=True, position=(0.67, 0.63)),
        Location.RIVERWALK: LocationData(name=Location.RIVERWALK.value, on_map=True, position=(0.648, 0.708)),
        Location.STREET: LocationData(name=Location.STREET.value, on_map=True, position=(0.555, 0.49)),
        Location.PARK: LocationData(name=Location.PARK.value, on_map=True, position=(0.585, 0.565)),
        Location.CAFE: LocationData(name=Location.CAFE.value, on_map=True, position=(0.525, 0.575)),
        Location.THERAPY: LocationData(name=Location.THERAPY.value, on_map=True, position=(0.5, 0.645)),
        Location.OTHER: LocationData(name=Location.OTHER.value),
    }
