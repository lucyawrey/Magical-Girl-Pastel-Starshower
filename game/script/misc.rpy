define stellam = Character("Mysterious Voice", color="#fff704")
label ask_player_name:
    stellam "Before things begin, I just wanted to ask you something. Your name is [persistent.real_player_name], right?"
    menu:
        "Yes":
            stellam "I thought so. I'll make sure to remember it."
        "No":
            stellam "Oh, my bad. I hope that's not a name that you don't like to hear."
            stellam "What should I call you instead?"
            python:
                entered_name = renpy.input("What should they call you?", length=32)
                persistent.real_player_name = entered_name.strip()
            stellam "[persistent.real_player_name]. I like it, and I'll be sure to remember it. Not that I wouldn't still remember it if I like hated the name or something."
        
    stellam "Okay, lets go."
    return

label call_off:
    return
