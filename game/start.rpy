define _scene_show_hide_transition = Dissolve(0.25)

# The game starts here.
label start:
    python:
        calendar = Calendar(start_time_block=1, start_day = 8, start_month=9, start_year=2194)

    jump day1

label end:

    "—"

    "That's all for now! More coming soon."

    menu:

        "Quit?"

        "Yes":

            jump quit

        "No":

            jump end    

label quit:

return
