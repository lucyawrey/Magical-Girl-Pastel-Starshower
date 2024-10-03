image bg bedroom dark:
  "bg bedroom.jpg"
  matrixcolor BrightnessMatrix(-0.5)

label day_2:

    show screen calendar_overlay
    play music "morning.mp3"
    scene bg bedroom
    show stella at head

    stellan "A new day already, huh. I don't really feel like going anywhere..."
    
    $ calendar.advance(2)
    scene bg bedroom dark
    show stella at head

    stellan "Oh, it's already night..."
    stellan "I guess I'll just go back to sleep."
    
    jump next_day
    
label day_3:

    show screen calendar_overlay
    play music "morning.mp3"
    scene bg bedroom
    show stella at head

    stellan "..."

    jump next_day

label day_4:

    show screen calendar_overlay
    play music "morning.mp3"
    scene bg bedroom
    show stella surprise at head

    stellan "Maybe it's time for a change."

    jump next_day
    