#import directives
import os
#global definintions
teams = ["Washington Winners",
         "Los Angeles Losers",
         "Chicago Champions",
         "Dallas Defeateds"]

def cls(): #convenience alias, simply clears terminal screen.
    os.system("cls")

def title_screen():
    print("VERY SIMPLE FOOTBALL GAME 2025\nby aidan bossle [v0.2]\n\n")
    ready_to_play = str(input("ENTER ANY INPUT TO PLAY: "))
    cls()
    
def intro(): #this section sets up the player's profile and team.
    print("Congratulations! You just got your very first job as a Head Coach in the VERY BIG FOOTBALL LEAGUE [VBFL]! Of course, as your agent, I have some boring paperwork for you to fill out. I know, I know, but it's a formality. Here, i'll help you through it.")
    anything = str(input("TYPE ANYTHING AND HIT ENTER TO CONTINUE:\n> "))
    cls()
    while True: #loops until user confirms their info
        print("First we have to do the basic I.D. stuff...")
        first_name = str(input("Your first name goes here: "))
        last_name = str(input("And your last name there: "))
        print("Mind reminding me which team you're signing with?")
        print(*teams, sep='\n')
        

#actual procedural calling of functions section
title_screen()
intro()

