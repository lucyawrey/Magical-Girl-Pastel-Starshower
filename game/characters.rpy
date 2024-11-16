# Character transforms
transform head:
    align (0.5, 0.45)

define textbox_name = Image("images/gui/textbox_name.png", xalign=0.5, yalign=1.0)
define textbox = Image("images/gui/textbox.png", xalign=0.5, yalign=1.0)

# Declare characters used by this game.
define name_only = Character(color="#ffffff", window_background=textbox_name) # Default named character
define narrator = Character() # Default narrator with no name provided
define n = Character(window_background=textbox) # Narrator with textbox
define stellan = Character("Stella", color="#fff704", what_color="#fdfcd2", what_prefix="(", what_suffix=")", window_background=textbox_name) # Stella narration
define stellad = Character(what_color="#fdfcd2") # Stella in a dream
define stella = Character("Stella", color="#fff704", window_background=textbox_name)
define mgps = Character("Magical Girl Pastel Starshower", color="#fffcb0")
define saoirse = Character("Saoirse", color="#890098")
define mgvh = Character("Magical Girl Void Heart", color="#400147")
