label ask_player_name:
    scene black
    show stella happy at head
    stella "Before we continue, I just wanted to ask you something. You're [persistent.real_player_name] right?"
    menu:
        "Yes":
            stella "I thought so."
        "No":
            stella "Oh, my bad. I hope I didn't call you a name that you don't like. "
            stella "What should I call you instead?"
            python:
                entered_name = renpy.input("What should Stella call you?", length=32)
                persistent.real_player_name = entered_name.strip()
            stella "[persistent.real_player_name]. I like it, I'll make sure to remember it. Not that I wouldn't still remember it if I like hated the name or something."
    return
