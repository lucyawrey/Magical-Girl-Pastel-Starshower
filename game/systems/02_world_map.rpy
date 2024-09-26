screen world_map():
    tag map
    text "Currently at: [world_map.location]. On map? [world_map.get_location_data().on_map]" at transform:
        align (0.5, 0.05)
    text "Where should Stella go?" at transform:
        align (0.5, 0.08)

init python:
    class WorldMap(object):
        def __init__(self, start_location: Location):
            self.location = start_location
        
        def get_location_data(self):
            return LOCATION_DATA[self.location] 
