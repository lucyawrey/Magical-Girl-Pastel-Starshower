# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Stella", color="#fff704")
define l = Character("Lucy", color="#292ce6")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

#    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

#    show eileen happy

    # These display lines of dialogue.

    s "Wow, It's really really dark in here."

    l "Yeah, we don't have any assets yet so everything has to take place in the dark."

    s "Wow that sucks."

    l "Sorry... I'm trying my best okay."

    s "Wasn't blaming you, just expressing a sentiment."

    l "That's fair haha, sorry for being a bit insecure."

    s "It's okay! I like you as you are."

    l "Isn't my girlfriend really cute by the way?"

    s "Yeah she totes is."

    # This ends the game.

    return
