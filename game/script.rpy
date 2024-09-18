# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Stella", color="#fff704")
define l = Character("Lucy", color="#8129e6")
define sl = Character("Stella and Lucy", color="#ffffff")
define m = Character("Miku", color="#4690ff")

# The game starts here.

label start:

#   scene bg room

    s "Wow, It's really really dark in here."

    l "Yeah, we don't have any assets yet so everything has to take place in the dark."

    s "Wow that sucks."

    l "Sorry... I'm trying my best okay."

    s "Wasn't blaming you, just expressing a sentiment."

    l "That's fair haha, sorry for being a bit insecure."

    s "It's okay! I like you as you are."

    l "Isn't my girlfriend really cute by the way?"

    s "Yeah she totes is."

    show miku

    m "Hi!"

    sl "AHHHHH!!!!"

    m "Hehe, did I scare you?"

    menu:

        "Yes!":
            jump choiceScared_yes

        "Nah.":
            jump choiceScared_no

label choiceScared_yes:

    $ scared_flag = True

    m "Good! I thought it might be fun to sneak up on you."

    jump choice1_done

label choiceScared_no:

    $ scared_flag = False

    m "Aww... I was hoping I would just a little. It's probably for the best though."

    jump choice1_done

label choice1_done:

    l "Okay."

    if scared_flag:
        l "I'm feeling pretty anxious now, but..."
    else:
        l "Anyways..."

    l "We should probably move onto the meeting."

    m "I agree--"

    s "Backup for a moment. How the heck can we see you in this darkness, Miku?"

    m "All the world is my stage, so I can be seen even in total darkness!"

    sl "..."
    
    m "And also because Lucy liberated an asset of me to use, if you'll allow me to step out of the narritive for a moment."

    s "Ahhh. So, the meeting?"

# This ends the game.

return
