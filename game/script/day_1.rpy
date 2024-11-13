label dream_1:
    jump ask_player_name
    return

label day_1:
    "It's half past ten in the morning and the most dangerous being on planet Earth is quite late for work."

    scene bg bathroom
    
    "The being in question is a girl named Stella—short for either \“Estelle\” or \“Pastel Starshower\” depending on who you ask—who is currently standing in her bathroom trying to get her perpetually messy, platinum blonde hair into some sense of order."

    scene bg bedroom

    "Once she is confident she's done the best she can without resorting to magic, she brushes her teeth, walks to her bedroom, changes into an outfit looted from the floor, slips through the sliding door across from her bed, and jumps off the balcony."

    scene bg fall
    play music "woosh.mp3"

    "She smiles as she feels the near weightlessness of freefall and the wind rushing towards and past her, ruining any progress she'd made on her hair in the process."
   
    "Halfway down—only around three seconds of falling—there is a flash of light and Stella is wearing a dress of radiant white, blue and yellow."

    stop music fadeout 1.0
    play sound "sfx-land.mp3"
    scene black

    "In three more seconds she slams into the ground with a heavy crunch, having landed in a slight crouch completely unharmed. Her dress disappears into tiny motes of light that mix with the dust kicked up by her landing."

    scene bg street
    show screen calendar_overlay
    play music "power-of-the-wind.mp3"
    show stella joy at head

    stella "A 50-story fall always wakes me up in the morning."

    show stella at head

    stellan "I really should head to the café, don't want to be any later than I already am. Again."

    "Select a destination from the city map."

    call world_map
    if calendar.time != Time.NIGHT:
        call pass_time(time=Time.NIGHT)

    "Before Stella knows it, it's already time to head home."
    
    jump next_day
