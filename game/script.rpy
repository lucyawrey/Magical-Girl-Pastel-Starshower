define _scene_show_hide_transition = Dissolve(0.20)
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
        start_time = Time.MORNING
        start_music = "morning.mp3"

        world_map = WorldMap(Location.HOME)
        location_list = get_location_list()
        hovered_location = ""
    
    call ask_player_name
    jump first_day

label next_day:
    hide screen calendar_overlay
    scene black
    $ calendar.next_day(start_time=start_time)
    $ start_time = Time.MORNING
label first_day:
    play music start_music
    show screen day_change
    ""
    hide screen day_change
    python:
        day_label = f"day_{calendar.day}"
        if renpy.has_label(day_label):
            renpy.jump(day_label)
    "No label for day with ID [day_label]."
    jump end

label pass_time(blocks=1):
    python:
        current_time = calendar.get_time();
        calendar.pass_time(blocks)
        next_time = calendar.get_time().lower()
    
    "[current_time] turns to [next_time]."
    return

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
