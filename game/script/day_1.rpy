label dream_1:
    scene black
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

label day_1:
    scene black
    show bg cafe
    show stella at head_left
    gio "Stella, I'm closing up and you probably don't want to sleep there all night."
    stella "Oh! Uh, I'm awake. Was just resting my head a bit."
    stella "I should probably head home and go to bed though."
    gio "Right. Just stay safe okay?"
    call void_heart_story
    stella "Well, I'm gonna head home. Thanks for listening."

    $ start_music = "morning.mp3"
    $ start_time = Time.MORNING
    jump next_day
