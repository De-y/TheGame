"""
Python file for [THE GAME]

Made by de-y originally for AP Computer Science Principles.
"""

from functions import clear, logo, wait, check_if_key_generated, ans_math, read_character_data
from sys import platform
import os, pyuac, hashlib, uuid, math

def run():
    """
    Run [THE GAME]
    """

    if platform == 'win32':
        # if not pyuac.isUserAdmin():
        #     print("Requesting Administrator Permissions...")
        #     print("Please rerun your commands.")
        #     pyuac.runAsAdmin()

        print("Administrator privileges have been granted!")
        game()
    else: 
        if not os.environ.get("SUDO_UID") and os.geteuid() != 0: 
            print("Please run the game again with sudo. ")
        else:
            game()

def game():
    leverage = True
    while leverage:
        clear()
        print(logo)
        print("Welcome to [THE GAME]! This is a simple text-based game that leverages your computer against you. If you die, your computer gets its harddrive wiped(Basically malware but not really).")

        options = input("\n1. New Game\n2. Load Game\n3. Credits\n4. Exit\n\nChoose your option: ")

        if options == '1':
            clear()
            print("[AGREEMENT BETWEEN YOU AND YOURSELF AND ALSO DEVELOPER]")
            ag = input("TLDR: PLEASE USE A VIRTUAL MACHINE BEFORE PLAYING. THIS IS NOT A JOKE.\n\nDo you agree that you will be liable for your computer being destroyed by [THE GAME]?\nThere have been 2 other warnings that were provided to you. This is the final one.\nThe developer will not be help liable.\n\nDo you agree to these terms? (y/n): ")
            if ag == 'y' or ag == 'Y':
                clear()
                print("Got it.")
                wait(1)
                clear()
                # print("[GAME SAVE PROCESS]\n[THE GAME] uses encryption to save your game statistics.")
                # if check_if_key_generated() == True:
                #     print("A key has already been generated. Moving on.")
                #     wait(3)
                # else:
                #     key = hashlib.sha3_256(str(uuid.uuid4).encode('utf-8')).hexdigest()
                #     key = hashlib.sha512(str(key).encode('utf-8')).hexdigest()

                #     keywriter = open('key.env', 'w')
                #     keywriter.write(key)
                #     keywriter.close()

                #     print("A key has been generated for you. Perfect!")
                #     wait(3)
                
                save_name = input("[THE GAME SAVE MANAGER]\n\n[THE GAME] has a save system for this game.\n\nWhat would you like to call your save?: ")
                character_name = input("What would you like to call your character?: ")
                print("\nThat's a good name!")
                difficulty = input("What difficulty would you like to have? (Easy/A, Hard/B, or Asian/C): ")
                if difficulty.capitalize() == 'EASY' or 'A':
                    print("Easy. Ok!")
                    difficulty = 'Easy'
                if difficulty.capitalize() == 'HARD' or 'B':
                    print("This is sure going to be a challenge for you!")
                    difficulty = 'Easy'
                if difficulty.capitalize() == 'ASIAN' or 'C':
                    verification = input("What is the value for the following integral? Round your answer to six digits after the decimal point.\n∫∞−∞sinxxsin(x/3)x/3sin(x/5)x/5sin(x/7)x/7…sin(x/13)x/13dx\n\nAnswer: ")
                    if ans_math(verification):
                        print("Alright... You are asian.")
                        difficulty = 'Asian'
                    else:
                        print("Failure. Could't answer a simple math question. *scoff*, instead, we are giving you failure mode.")
                        difficulty = 'Failure'
                directory = os.path.join(os.getcwd(), 'saves')
                if not os.path.exists(directory):
                    os.makedirs(directory)
                file = open(f'./saves/{save_name}.tgsf', 'w')
                wait(1.5)
                file.write(f"NAME: {save_name}\nCharacterName: {character_name}\nWorld: T1\nRegion: Start\nDifficulty: {difficulty}\nHealth:100")
                file.close()

            else:
                print("Phew. You made the right choice.")
                leverage = False
        if options== '2':
            print("What is the name of the save file?: ")
            save_name = input("Name: ")
            if os.path.exists(f'./saves/{save_name}.tgsf'):
                print("Found it!")
                data = read_character_data(f'./saves/{save_name}.tgsf')
                save_name = data[0][1]
                wait(5)
            else:
                print("Sorry, we couldn't find that save file.")
                wait(3)
        if options == '3':
            clear()
            print("[THE GAME]\n\nMade by de-y originally for AP Computer Science Principles, but since I never took it, I am releasing this code here.")
        if options == '4':
            clear()
            print("See you next time!")
            leverage = False
            