label main_menu:
    if persistent.first_play:
        return
    else:
        show screen main_menu
        pause

# The game starts here.
label start:
    python:
        # The day skips dictionary allows skipping a number of calendar
        # days when reaching or passing a given set of in game days.
        # For example, `dict([(3, 2), (5, 7)])` skips an extra calendar
        # day on game day 3 and skips forward an entire week on game day 5.
        day_skips = dict([])
        # Creates the global calendar object for a given start date.
        # Changing the day number will always be relative to this start date.
        start_time = Time.MORNING
        calendar = Calendar(start_day = 8, start_month=9, start_year=2194, day_skips_dict=day_skips, start_time=start_time)
        start_music = "morning.mp3"

        world_map = WorldMap(Location.HOME)
        location_list = get_location_list()
        hovered_location = ""
        persistent.first_play = False
    
    jump first_day

label next_day:
    hide screen calendar_overlay
    $ calendar.next_day(start_time=start_time)
    $ start_time = Time.MORNING
label first_day:
    python:
        quick_menu = False
        dream_label = f"dream_{calendar.day}"
        if renpy.has_label(dream_label):
            renpy.call(dream_label)
    play music start_music
    show screen day_change
    pause
    hide screen day_change
    python:
        quick_menu = True
        day_label = f"day_{calendar.day}"
        if renpy.has_label(day_label):
            renpy.jump(day_label)
    "The [calendar.get_ordinal()] day is not ready yet."
    jump end

label pass_time(blocks=1, time=None):
    python:
        current_time = calendar.get_time()
        if time is not None:
            calendar.time = time
        else:
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
    $ renpy.choice_for_skipping()
    "Thanks for playing this early version of the game!"
    return
