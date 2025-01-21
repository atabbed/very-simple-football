#import directives
import os
#global definintions
teams = ["washington winners",
         "los angeles losers",
         "chicago champions",
         "dallas defeateds"]

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
    while True:
        while True: #loops until user confirms their info
            print("First we have to do the basic I.D. stuff...")
            first_name = str(input("Your first name goes here: "))
            last_name = str(input("And your last name there: "))
            print("Mind reminding me which team you're signing with?")
            print(*teams, sep='\n')
            team = str(input("Enter a team from the list above:"))
            if team.lower() in teams:
                cls()
                break
            else:
                cls()
                print("You filled out the form wrong - enter a valid team on the list and fill it out properly!\n")
        print("Alright, I remember now! You're " + first_name + " " + last_name + " with the " + team + "!")
        resp = str(input("Is that correct? (ENTER 'YES' OR 'NO'.)"))
        if resp.upper() == "YES":
            cls()
            print("Welcome to the, " + team + " coach! Ready for your first game?")
            #break
            #TODO: call next part of game
        elif resp.upper() == "NO":
            print("Alright, let's try this again...")

#TODO somewhere in here generate season schedule or just randomize it every game (there is only four teams after all...)

def game():
    pass #FIXME remove once pseudocode replaced
    #check: if user wants to play current game
        #display game info
        #play or quit option
            #PLAY
                #Game start
                #Coin flip!
                    #Defer/receive
                    #OR
                    #Randomize other team's choice but give defer higher chance
                #Kickoff
                    #Kick meter in here somewhere??? (MINIGAME #2)
                        #Pick Play Menu:
                            #Onside
                            #Squib??? (maybe)
                            #Boot it through back of endzone
                            #Fair catch it in endzone
                            #Boot it to one [higher risk]
                            #Boot it to reasonable [lower risk than 1 above]
                            #High kickoff [risk, higher fumble chance though?]
                    #TODO: Playcalling is (MINIGAME #1)
                    #Offense
                        #Display Down Counter & Other Relevant Info
                            #Pick Play Menu: #TODO: Options for who to throw it to? This could be (MINIGAME #3)
                                #Run
                                    #Inside Run
                                    #Outside Run
                                #Pass
                                    #Short
                                        #Short slant
                                        #Short ins
                                        #Short outs
                                        #Short curls
                                    #Mid
                                        #Mid ins
                                        #Mid outs
                                        #Mid curls
                                    #Long
                                        #Hail Mary (Four Verticals)
                                        #Deep Play Action Cross
                                        #Deep Outs
                                #Options
                                    #RPO
                                        #Chose to give it to qb or rb during play? (MINIGAME #4)
                    #OR
                    #Defense
                        #Display Down Counter & Other Relevant Info
                            #Pick Play Menu:
                                #

            #QUIT:
            #go back up in hierarchy
    #check: other stuff (recruiting if time???)

#actual procedural calling of functions section
title_screen()
intro()