#import directives
import os
import random
#global definintions
teams = ["washington winners",
         "los angeles losers",
         "chicago champions",
         "dallas defeateds"]

washington_winners_stats={
    "RATING [OUT OF 5 STARS]":2

}

los_angeles_losers_stats={
    "RATING [OUT OF 5 STARS]":6
}

chicago_champions_stats={
    "RATING [OUT OF 5 STARS]":1
}

dallas_defeateds_stats={
    "RATING [OUT OF 5 STARS]":4
}

def cls(): #convenience alias, simply clears terminal screen.
    os.system("cls")

def title_screen():
    print("VERY SIMPLE FOOTBALL GAME 2025\nby aidan bossle [v0.2]\n\n")
    ready_to_play = str(input("ENTER ANY INPUT TO PLAY: ")) #easy way to progress without needing to check input  or asking user to type specific answer!
    cls()
    
def intro(): #this section sets up the player's profile and team.
    print("Congratulations! You just got your very first job as a Head Coach in the VERY BIG FOOTBALL LEAGUE [VBFL]! Of course, as your agent, I have some boring paperwork for you to fill out. I know, I know, but it's a formality. Here, i'll help you through it.")
    anything = str(input("TYPE ANYTHING AND HIT ENTER TO CONTINUE:\n> ")) #used the trick again here!
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
        if resp.upper() == "YES": #makes it not case-sensitive
            cls()
            print("Welcome to the, " + team + " coach! Ready for your first game?")
            anything = str(input("TYPE ANYTHING AND HIT ENTER TO CONTINUE:\n> "))
            break
        elif resp.upper() == "NO":
            print("Alright, let's try this again...")
    return team


def homepage():
    cls()
    while True:
        print("SUPER DUPER COACHING PORTAL 9000")
        print("WELCOME, COACH! WHICH ACTION WOULD YOU LIKE TO PERFORM:\n- PLAY SEASON GAME\n- RECRUIT PLAYERS\n- CLOCK OUT (QUITS GAME)")
        resp = str(input("ENTER ACTION: > "))
        if resp.upper() == "PLAY SEASON GAME":
            opponent = random.choice(teams) #generates the opponent you will face.
            return opponent, resp.upper()
        elif resp.upper() == "RECRUIT PLAYERS":
            print("This feature has not been implemented yet.")
        elif resp.upper() == "CLOCK OUT":
            os._exit()
        else:
            cls()
            print("Invalid input. Enter an option from the list and try again.\n\n")

def game_start():
    print("THIS WEEK'S MATCHUP: THE " + players_team.upper() + " VERSUS THE " + opp.upper() + " ON PRIMETIME VBFL WEDNESDAY NIGHT FOOTBALL!") #PRINTS GAME INFO
    #TODO display stats?
    ready_to_play = str(input("ENTER ANY INPUT TO BEGIN GAME: ")) #this simple advance prompt again
    print("COIN TOSS!")
    choice = str(input("'HEADS' OR 'TAILS': ")) #player choses
    coinflip = random.randint(1,2) #coinflip result generated
    if coinflip == 1: #TODO error handling
        if choice.upper() == "HEADS":
            print("Heads! You Win!")
        else:
            print("Heads! You Lose!")
    elif coinflip == 2:
        if choice.upper() == "TAILS":
            print("Tails! You Win!")
        else:
            print("Tails! You Lose!")
    rec_def = str(input("Would you like to 'RECEIVE' the ball now or 'DEFER' and receive second half?: "))
    if rec_def.upper() == "RECEIVE":
        print("Kickoff!")
    
                      #PLAY
                    #Game start
                    #Coin flip!
                        #Defer/receive
                        #OR
                        #Randomize other team's choice but give defer higher chance
                        #LOOP KICKOFF UNTIL GAME CONCLUDES
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
                                        #TODO: AFTER EACH PLAY RANDOMIZE TIME CONSUMED (MAYBE PROPORTIONAL TO YARDAGE GAINED?)
                                #OR
                                #Defense
                                    #Display Down Counter & Other Relevant Info
                                        #Pick Play Menu:
                                            #Zone Coverage
                                                #Blitz
                                                #Cover
                                                #Prevent
                                            #Man Coverage
                                                #Blitz
                                                #Cover
                        

                #QUIT:
                #go back up in hierarchy
        #check: other stuff (recruiting if time???)

#actual procedural calling of functions section
title_screen()
players_team = intro()
opp,should_play_game = homepage()
if should_play_game.upper() == "PLAY SEASON GAME":
    game_start()