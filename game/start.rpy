define _scene_show_hide_transition = Dissolve(0.25)

# The game starts here.
label start:
    python:
        calendar = Calendar(start_day = 8, start_month=9, start_year=2194)

    jump first_day

label next_day:
    scene black
    $ calendar.next_day()
label first_day:
    show screen day_change
    ""
    hide screen day_change
    python:
        day_label = f"day_{calendar.day}"
        if renpy.has_label(day_label):
            renpy.jump(f"day_{calendar.day}")

label end:
    "—"
    "That's all for now! More coming soon."
    menu:
        "Quit?"
        "Yes":
            return
        "No":
            jump end
