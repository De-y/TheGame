"""
This is the CLI.

Made by de-y originally for AP Computer Science Principles.
"""

from game import run
import platform, psutil
from functions import clear

def cli(input_in_while):
    print("Welcome to the CLI! Run 'help' for some help.")
    while input_in_while:
        command = ""
        try:
            command = input("User: ")
        except:
            print("Exiting gracefully.")
            input_in_while = False
        try:
            if command == "help":
                clear()
                print("""
          Full list of commands:

          help: View the commands available.
          about: about the CLI
          run: Start [THE GAME](Note, this may destroy your computer if you lose, so be careful.)      
                """)
            if command == "about":
                clear()
                print(f"\n\nAbout the game and some system information:\n\nDeveloped by DF.\nPowered by 100% Python, No BS.\nSystem OS Type: {platform.system()}\nSystem Version: {platform.version()}\nSystem Architecture: {platform.machine()}\nProcessor Type: {platform.processor()}\nRAM: {str(round(psutil.virtual_memory().total / (1024.0 **3)))}GB.\n\n")
            if command == "run":
                clear()
                print("We will need you to validate some information before you can start playing.\n")
                agreement = input("Do you agree that your computer can be destroyed if you play this game and lose? (y/n): ")
                if agreement == 'y':
                    clear()
                    print("Confirmed. Next!")
                    agreement = input("Do you agree that you will not hold the developer responsible for any damage caused by this game? (y/n): ")
                    if agreement == 'y':
                        clear()
                        print("Getting ready to start [THE GAME].")
                        run()
                        input_in_while = False
                    else:
                        print("Close call! Exiting the CLI gracefully.")
                        input_in_while = False
                else:
                    print("Gotcha. Exiting the CLI gracefully.")
                    input_in_while = False
        except Exception as ex:
            print(ex)
            print(command + " is not a valid command.")
