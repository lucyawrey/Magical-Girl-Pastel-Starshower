screen world_map():
    tag map
    text "Where should Stella go?" at transform:
        align (0.5, 0.1)

init python:
    import datetime

    class WorldMap(object):
        def __init__(self):
            self.location = 0
            self.location_names = ["Other", "Home", "Street", "Park", "Cafe", "Therapy Office"]

        def set_location(self, location: int = 0) -> None:
            self.location = location

        def get_location(self) -> str:
            return self.location_names[self.location]
