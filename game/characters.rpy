# Character transforms
transform head:
    align (0.5, 0.45)

transform head_left:
    align (0.39, 0.45)

define textbox_name = Transform(Image("images/gui/textbox_name.png"), xalign=0.5, yalign=1.0, zoom=4.0, nearest=True)
define textbox = Transform(Image("images/gui/textbox.png"), xalign=0.5, yalign=1.0, zoom=4.0, nearest=True)

# Declare characters used by this game.
define name_only = Character(color="#ffffff", window_background=textbox_name) # Default named character
define narrator = Character() # Default narrator with no name provided
define n = Character(window_background=textbox) # Narrator with textbox
define stellan = Character("Stella", color="#fff704", what_color="#fdfcd2", what_prefix="(", what_suffix=")", window_background=textbox_name) # Stella narration
define stellad = Character(what_color="#fdfcd2") # Stella in a dream
define stella = Character("Stella", color="#fff704", window_background=textbox_name)
define mgps = Character("Magical Girl Pastel Starshower", color="#fffcb0")
define saoirse = Character("Saoirse", color="#890098")
define mgvh = Character("Void Heart", color="#890098", what_color="#d6d6d6", window_background=textbox_name)
define ellie = Character("Ellie", color="#16c610", window_background=textbox_name)
define gio = Character("Giovanni", color="#f264df", window_background=textbox_name)