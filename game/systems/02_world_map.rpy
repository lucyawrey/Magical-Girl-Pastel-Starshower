image selector = Transform("images/selector.svg", size=(50, 50))

screen world_map():
    tag map
    for i, location in enumerate(world_map.get_all_location_data()):
        add "selector" at transform:
            align (0.5, 0.5)
        text location.name at transform:
            align (0.018, 0.97 - (0.04 * i))

init python:
    class WorldMap(object):
        def __init__(self, start_location: Location):
            self.location = start_location
        
        def get_location_data(self):
            return LOCATION_DATA[self.location]

        def get_all_location_data(self):
            return [v for k, v in LOCATION_DATA.items() if v.on_map == True]
