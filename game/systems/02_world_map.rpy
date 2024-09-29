image selector = Transform("images/selector.svg", size=(40, 40))
image selector_hover = Transform("images/selector light.svg", size=(60, 60))

screen world_map():
    tag map
    style_prefix "world_map"
    for i, location in enumerate(location_list):
        add ("selector" if hovered_location != location.name else "selector_hover") at transform:
            align location.position

    vbox:
        for location in location_list:
            textbutton location.name:
                hovered SetVariable("hovered_location", location.name)
                unhovered SetVariable("hovered_location", "")
                action [Function(world_map.set_location, new_location=location.enum), Jump("go")]

style world_map_vbox is vbox
style world_map_button is button
style world_map_button_text is button_text

style world_map_vbox:
    xalign 0.01
    ypos 860
    yanchor 0.5

    spacing 10

style world_map_button is default:
    properties gui.button_properties("choice_button")

style world_map_button_text is default:
    properties gui.text_properties("choice_button")

init python:
    class WorldMap(object):
        def __init__(self, start_location: Location):
            self.location = start_location
            self.data = LOCATION_DATA[start_location]
        
        def set_location(self, new_location: Location):
            self.location = new_location
            self.data = LOCATION_DATA[new_location]

        def get_location_list(self):
            return [v for k, v in LOCATION_DATA.items() if v.on_map == True]
