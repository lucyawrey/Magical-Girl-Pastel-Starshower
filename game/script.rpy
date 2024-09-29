define _scene_show_hide_transition = Dissolve(0.25)
transform head:
    align (0.5, 0.45)

# The game starts here.
label start:
    python:
        # The day skips dictionary allows skipping a number of calender
        # days when reaching or passing a given set of in game days.
        # For example, `dict([(3, 2), (5, 7)])` skips an extra calender
        # day on game day 3 and skips forward an entire week on game day 5.
        day_skips = dict([])
        # Creates the global calender object for a given start date.
        # Changing the day number will always be relative to this start date.
        calendar = Calendar(start_day = 8, start_month=9, start_year=2194, day_skips_dict=day_skips)
        start = Time.MORNING

        world_map = WorldMap(Location.HOME)
        location_list = world_map.get_location_list()
        hovered_location = ""

    jump first_day

label next_day:
    hide screen calendar_overlay
    scene black
    stop music fadeout 1.0
    $ calendar.next_day(start_time=start)
    $ start = Time.MORNING
label first_day:
    show screen day_change
    ""
    hide screen day_change
    python:
        day_label = f"day_{calendar.day}"
        if renpy.has_label(day_label):
            renpy.jump(day_label)
    "No label for day with ID [day_label]."
    jump end

label world_map:
    show screen world_map
    play music "morning.mp3"
    $ renpy.choice_for_skipping()
    # Need to figure out how to stop skipping past this point.
    $ renpy.pause(hard=True)

label go:
    hide screen world_map
    python:
        loc_label = world_map.data.id
        if renpy.has_label(loc_label):
            renpy.jump(loc_label)
    "No label for location with ID [world_map.data.id]."
    return

label end:
    "—"
    $ renpy.choice_for_skipping()
    "That's all for now! More coming soon."
    return
