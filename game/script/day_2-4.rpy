label day_2:

    show screen calendar_overlay
    play music "morning.mp3"
    scene bg bedroom

    stella "A new day already, huh. I don't really feel like going anywhere..."
    
    $ calendar.advance(2)

    stella "Oh, it's already night..."
    
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

    stella "Maybe it's time for a change."

    jump next_day
    