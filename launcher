#this is a quick launcher script I wrote that automatically runs the project in a new terminal. it was more neccessary with my old draft of the game, but now is just convenient.
import os
import subprocess

def launch_game():
    dir = os.path.dirname(os.path.abspath(__file__)) # defines folder game is stored in, neccessary since this could be installend anywhere on host machine.
    game = os.path.join(dir, "game.py") #defines actual game file location
    if os.name == 'nt':  # apparently nt is windows' identifier here, and refers to Windows NT from the 90s.
        subprocess.run(["start", "cmd", "/k", "python", game], shell=True, cwd=dir) # most options here self-explanatory, but /k required to pass commands to new terminal proccess.
    else:
        print("[FATAL ERROR]: This game only supports Windows-based machines.")
launch_game()