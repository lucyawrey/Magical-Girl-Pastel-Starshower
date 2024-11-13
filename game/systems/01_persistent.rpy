init python:
     import getpass
     player_name_guess = getpass.getuser().title()

default persistent.real_player_name = player_name_guess
default persistent.first_play = True
