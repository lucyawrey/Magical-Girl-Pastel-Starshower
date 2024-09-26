screen world_map():
    tag map
    text "Currently at: [world_map.location]" at transform:
        align (0.5, 0.05)
    text "Where should Stella go?" at transform:
        align (0.5, 0.08)

init python:
    class WorldMap(object):
        def __init__(self, start_location: Location):
            self.location = start_location
