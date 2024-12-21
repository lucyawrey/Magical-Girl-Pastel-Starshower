label name_input:
    python:
        entered_name = renpy.input("Give your name.", length=32)
        persistent.real_player_name = entered_name.strip()
    return

label dream_2:
    stellad "......"
    if persistent.real_player_name == "":
        stellad "I'm realizing I never asked you what I should call you."
        stellad "So... what's going to be your name?"
        call name_input
        stellad "[persistent.real_player_name]. I like it, and I'll be sure to remember that. Not that I wouldn't remember it if I like hated it or something."
    else:
        stellad "It's good to see you again, [persistent.real_player_name]."
        stellad "Oh! Now that I think about it, is that something you'd still like me to call you?"
        menu:
            stellad "Oh! Now that I think about it, is that something you'd still like me to call you?{fast}"
            "Yes":
                stellad "Awesome, I guess that's it."
            "No":
                stellad "Oh, uh, I hope I didn't use a name you don't like to hear."
                stellad "What name should I use instead?"
                call name_input
    scene black
    stop music fadeout 1.0
    pause 1.0
    return

label day_2:
    "It's half past ten in the morning and the most dangerous being on planet Earth is quite late for work."

    scene bg bathroom
    
    n "The being in question is a girl named Stella—short for either \“Estelle\” or \“Pastel Starshower\” depending on who you ask—who is currently standing in her bathroom trying to get her perpetually messy, platinum blonde hair into some sense of order."

    show bg bedroom

    n "Once she is confident she's done the best she can without resorting to magic, she brushes her teeth, walks to her bedroom, changes into an outfit looted from the floor, slips through the sliding door across from her bed, and jumps off the balcony."

    show bg fall
    play music "woosh.mp3"

    n "She smiles as she feels the near weightlessness of freefall and the wind rushing towards and past her, ruining any progress she'd made on her hair in the process."
   
    n "Halfway down—only around three seconds of falling—there is a flash of light and Stella is wearing a dress of radiant white, blue and yellow."

    stop music fadeout 1.0
    play sound "sfx-land.mp3"
    scene black

    n "In three more seconds she slams into the ground with a heavy crunch, having landed in a slight crouch completely unharmed. Her dress disappears into tiny motes of light that mix with the dust kicked up by her landing."

    scene bg street
    show screen calendar_overlay
    play music "power-of-the-wind.mp3"
    show stella joy at head

    stella "A 50-story fall always wakes me up in the morning."

    show stella at head

    stellan "I really should head to the café, don't want to be any later than I already am. Again."

    n "Select a destination from the city map."

    call world_map
    if calendar.time != Time.NIGHT:
        call pass_time(time=Time.NIGHT)

    n "Before Stella knows it, it's already time to head home."
    
    jump next_day
