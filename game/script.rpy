# Declare characters used by this game. The color argument
# colorizes the name of the character.

define stella = Character("Stella", color="#fff704")
define mgps = Character("Magical Girl Pastel Starshower", color="#fffcb0")
define saoirse = Character("Saoirse", color="#890098")
define mgvh = Character("Magical Girl Void Heart", color="#400147")

define _scene_show_hide_transition = Dissolve(0.25)

# The game starts here.
label start:
    play music "morning.mp3"

    "It's half past ten in the morning and the most dangerous being on planet Earth is quite late for work."

    scene bg bathroom
    
    "The being in question is a girl named Stella—short for either \“Estelle\” or \“Pastel Starshower\” depending on who you ask—who is currently standing in her bathroom trying to get her perpetually messy, platinum blonde hair into some sense of order."

    scene bg bedroom

    "Once she is confident she's done the best she can without resorting to magic, she brushes her teeth, walks to her bedroom, changes into an outfit looted from the floor, slips through the sliding door across from her bed, and jumps off the balcony."

    scene bg fall

    play music "woosh.mp3"

    "She smiles as she feels the near weightlessness of freefall and the wind rushing towards and past her, ruining any progress she'd made on her hair in the process."
   
    "Halfway down—only around three seconds of falling—there is a flash of light and Stella is wearing a dress of radiant white, blue and yellow."

    play sound "sfx-land.mp3"

    scene black

    play music "power-of-the-wind.mp3"

    "In three more seconds she slams into the ground with a heavy crunch, having landing in a slight crouch completely unharmed. Her dress disappears into tiny motes of light that mix with the dust kicked up by her landing."

# This ends the game.
return
