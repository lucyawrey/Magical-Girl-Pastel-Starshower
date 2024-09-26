init python:
    from enum import Enum

    class Location(str, Enum):
        OTHER = "Other"
        HOME = "Home"
        STREET = "Street"
        PARK = "Park"
        CAFE = "Cafe"
        THERAPY = "Therapy Office"
