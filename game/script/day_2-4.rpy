label day_2:

    show screen calendar_overlay
    play music "morning.mp3"
    scene bg bedroom

    stella "A new day already, huh. I don't really feel like going anywhere..."

    jump next_day
    
label day_3:

    show screen calendar_overlay
    play music "morning.mp3"
    scene bg bedroom

    stella "..."

    jump next_day

label day_4:

    show screen calendar_overlay
    play music "morning.mp3"
    scene bg bedroom

    "Restart."

    $ calendar.set_day(1)
    scene black
    stop music fadeout 1.0
    jump first_day
    