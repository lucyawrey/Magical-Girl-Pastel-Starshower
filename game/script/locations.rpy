label home:
    menu:
        stella "Should I really just go back home and sleep instead?"
        "Yes":
            jump stay_home
        "No":
            call world_map
    return

    label stay_home:
        stella "Yeah, the fall was nice, but I don't actually feel like going anywhere. I'll call off."

        scene black

        "Stella reenters her apartment building from the main entrance and takes an elevator back to the 50th floor."

        scene bg bedroom

        stella "Goodnight, me."

    return

label riverwalk:
    stella "Fishing at the riverwalk sounds like fun."

    scene black

    "Stella spends the day fishing."

    return

label street:
    stella "I would feel bad skipping work only hang out on the street on right next to the café. I don't think anyone would really care, but still. Like, what if someone saw me? No way."

    call world_map
    return

label park:
    stella "Maybe I should go for a walk."

    scene black

    "Stella spends the day walking, napping, and training in the park."

    return

label cafe:
    scene black

    "Stella heads to work for the day..."

    return

label therapy:
    stella "I don't have therapy today."

    call world_map
    return