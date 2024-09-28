image selector = Transform("images/selector.svg", size=(50, 50))
define location_list = world_map.get_location_list()

screen world_map():
    style_prefix "world_map"
    tag map
    for i, location in enumerate(location_list):
        add "selector" at transform:
            align location.position

    vbox:
        for location in location_list:
            textbutton location.name action i.action

style world_map_vbox is vbox
style world_map_button is button
style world_map_button_text is button_text

style world_map_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.world_map_spacing

style world_map_button is default:
    properties gui.button_properties("choice_button")

style world_map_button_text is default:
    properties gui.text_properties("choice_button")

init python:
    class WorldMap(object):
        def __init__(self, start_location: Location):
            self.location = start_location
        
        def get_location_data(self):
            return LOCATION_DATA[self.location]

        def get_location_list(self):
            return [v for k, v in LOCATION_DATA.items() if v.on_map == True]
