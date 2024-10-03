init python:
    from enum import Enum

    class Location(str, Enum):
        HOME = "Home"
        RIVERWALK = "Riverwalk"
        STREET = "Main Street"
        PARK = "Park"
        CAFE = "Café"
        THERAPY = "Therapy"
        OTHER = "Other"

    class LocationData():
        def __init__(self, enum: Location, on_map = False, position: (float, float) = (0, 0)):
            self.enum = enum
            self.id = str(enum).replace("Location.", "").lower()
            self.name = enum.value
            self.on_map = on_map
            self.position = position

    LOCATION_DATA = {
        Location.HOME: LocationData(enum=Location.HOME, on_map=True, position=(0.67, 0.63)),
        Location.RIVERWALK: LocationData(enum=Location.RIVERWALK, on_map=True, position=(0.648, 0.708)),
        Location.STREET: LocationData(enum=Location.STREET, on_map=True, position=(0.555, 0.49)),
        Location.PARK: LocationData(enum=Location.PARK, on_map=True, position=(0.585, 0.565)),
        Location.CAFE: LocationData(enum=Location.CAFE, on_map=True, position=(0.525, 0.575)),
        Location.THERAPY: LocationData(enum=Location.THERAPY, on_map=True, position=(0.5, 0.645)),
        Location.OTHER: LocationData(enum=Location.OTHER),
    }

    def get_location_list():
        return [value for key, value in LOCATION_DATA.items() if value.on_map == True]
