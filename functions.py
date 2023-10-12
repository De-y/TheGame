"""
Functions file for "THE GAME".

Made by de-y originally for AP Computer Science Principles.
"""

import os, time, subprocess
from sys import platform
import subprocess

def death():
    # For safety, I don't have any idea what to put here.
    pass
    
def clear():
    if platform == "win32":
        os.system('cls')
    else:
        os.system('clear')

def wait(secs):
    time.sleep(secs)

def ans_math(answer):
    if answer == str(round(3.1415926535, 6)):
        return True
    else:
        return False
def read_character_data(file_path):
    f = open(file_path, "r")
    data = f.read()
    character_data = []
    for line in data.split("\n"):
        value = line.split(":")
        character_data.append((value))

    return character_data

    
def check_if_key_generated():
    try:
        key_manager = open('key.env', 'r')
        key_manager.read()
        return True
    except: 
        return False
logo = """
    $$$$\       $$$$$$$$\ $$\   $$\ $$$$$$$$\        $$$$$$\   $$$$$$\  $$\      $$\ $$$$$$$$\       $$$$\ 
$$  _|      \__$$  __|$$ |  $$ |$$  _____|      $$  __$$\ $$  __$$\ $$$\    $$$ |$$  _____|      \_$$ |
$$ |           $$ |   $$ |  $$ |$$ |            $$ /  \__|$$ /  $$ |$$$$\  $$$$ |$$ |              $$ |
$$ |           $$ |   $$$$$$$$ |$$$$$\          $$ |$$$$\ $$$$$$$$ |$$\$$\$$ $$ |$$$$$\            $$ |
$$ |           $$ |   $$  __$$ |$$  __|         $$ |\_$$ |$$  __$$ |$$ \$$$  $$ |$$  __|           $$ |
$$ |           $$ |   $$ |  $$ |$$ |            $$ |  $$ |$$ |  $$ |$$ |\$  /$$ |$$ |              $$ |
$$$$\          $$ |   $$ |  $$ |$$$$$$$$\       \$$$$$$  |$$ |  $$ |$$ | \_/ $$ |$$$$$$$$\       $$$$ |
\____|         \__|   \__|  \__|\________|       \______/ \__|  \__|\__|     \__|\________|      \____|
                                                                                                       
                                                                                                       
                                                                                                       
    """