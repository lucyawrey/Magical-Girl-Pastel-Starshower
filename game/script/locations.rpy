label home:
    menu:
        stellan "Should I really just go back home and sleep?"
        "Yes":
            $ day_1_stay_home = True
            jump stay_home
        "No":
            call world_map
    return

    label stay_home:
        stellan "Yeah, the fall was nice, but I don't actually feel like going anywhere. I'll call off."

        scene black

        n "Stella reenters her apartment building from the main entrance and takes an elevator back to the 50th floor."

        scene bg bedroom
        show stella at head

        stella "Goodnight, me."
    return

label riverwalk:
    stellan "I could take a stroll down the riverwalk, maybe even go finishing?"

    menu:
        stellan "Is that worth skipping work for?"

        "Yes":
            jump riverwalk_walk
        "No":
            call world_map
    return

    label riverwalk_walk:
        show stella happy

        stellan "Ah what the heck, I'll call off."

        scene bg riverwalk
        show stella at head

        n "Stella begins her walk down the Neo Detroit riverwalk, enjoying the early autumn sun and the gentle breeze."
        
        stellan "It really is a nice day out, especially when no one is trying to talk to me."

        n "Stella continues her walk until reaching her usual pier."    
    
    return

label street:
    stellan "I would feel bad skipping work only hang out on the street right next to the café where someone could see me. I don't think anyone would really care, but still. No way."

    call world_map
    return

label park:
    stellan "I don't really feel like hanging out at the park today. Plus, I really should just go to work."

    call world_map
    return

label cafe:
    scene bg cafe

    n "Stella heads to work for the day..."

    return

label therapy:
    stellan "I don't have therapy today."

    call world_map
    return
