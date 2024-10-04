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

        "Stella reenters her apartment building from the main entrance and takes an elevator back to the 50th floor."

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

        "Stella spends the day walking down the Neo Detroit riverwalk. She enjoys the sun, snacks on street food, and gets some fishing in."
        "Before she knows it, it's time to head home for the night."
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
    scene black

    "Stella heads to work for the day..."

    return

label therapy:
    stellan "I don't have therapy today."

    call world_map
    return
