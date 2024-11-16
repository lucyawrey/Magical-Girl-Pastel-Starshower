label dream_1:
    "You float formless in the space between."
    "You look upon a speck in that void and reach out to touch it."
    "Suddenly, light. Blinding."
    "The nothingness that had surrounded you becomes everything and then—"
    stellad "Hey, it's going to be alright."
    stellad "You wont to be alone anymore."
    stellad "Living is hard, but I'd like it if you—if both of us—tried."
    stellad "So, let's go."
    scene black
    stop music fadeout 1.0
    pause 1.0
    return

image bg cafe dark:
    "bg cafe.jpg"
    matrixcolor BrightnessMatrix(-0.6)

label day_1:
    scene bg cafe dark
    show stella at head
    "Kind Girl" "Stella, you probably don't want to sleep there all night."
    stella "Oh! Uh, I'm awake. Was just resting my head a bit."
    stella "I should probably head home and go to bed though."
    "Kind Girl" "Right, hehe. Just stay safe okay?"

    $ start_music = "morning.mp3"
    $ start_time = Time.MORNING
    jump next_day
