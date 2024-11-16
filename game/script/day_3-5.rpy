image bg bedroom dark:
  "bg bedroom.jpg"
  matrixcolor BrightnessMatrix(-0.5)

label day_3:
    show screen calendar_overlay
    scene bg bedroom
    show stella at head

    stellan "A new day already, huh. I don't really feel like going anywhere..."
    
    show bg bedroom dark
    call pass_time(2)

    stellan "Oh, it's already night..."
    stellan "I guess I'll just go back to sleep."
    
    jump next_day
    
label day_4:

    show screen calendar_overlay
    scene bg bedroom
    show stella at head

    stellan "..."

    jump next_day

label day_5:

    show screen calendar_overlay
    scene bg bedroom
    show stella surprised at head

    stellan "Maybe it's time for a change."

    jump next_day
    