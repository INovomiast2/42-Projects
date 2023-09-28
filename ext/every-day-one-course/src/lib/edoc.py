"""
	EDOC Module

	This module will have all the functions and classes that EDOC will use.
	Some of them will be used in the main file and others will be used in other files.
	A good example of this is the "netpy" module.
	Netpy is a module that I created to help me with my network related projects.
	You can find it in the "lib" folder.

	EDOC is a project that I'm doing to learn Python and to learn how to use the YouTube API.
	Feel free to use it and modify it as you want.
	You can also contribute to the project if you want to.
	You can contact me at:
		- Discord: INovomiast2#0000
		- Twitter: @INovomiast2
		- Email:

	EDOC is licensed under the Apache License 2.0.
	You can read the license here: [https://apache.org/licenses/LICENSE-2.0]
"""

# Importing modules
import os
import sys
import time
import random
import webbrowser
import json
import datetime
import threading
import uuid
from colorama import Fore, Back, Style, init
from pyfiglet import Figlet

# Importing EDOC modules
from lib import netpy

def append_log(log):
	"""
		This function appends a log to the "logs/edoc.log" file.
		with the current date and time.
	"""
	with open("logs/edoc.log", "a") as log_file:
		log_file.write("[" + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "] " + log + "\n")
		log_file.close()


def init():
	"""
		This function initializes the EDOC program.
	"""
	os.system("cls" if os.name == "nt" else "clear")
	# Creating the "config" files
	if not os.path.exists("config"):
		os.mkdir("config")
	if not os.path.exists("config/config.json"):
		with open("config/config.json", "w") as config:
			config.write(json.dumps({
				"language": "en",
				"uuid": str(uuid.uuid4()),
				"debug": False,
				"sessions": [],
				"last_session": None,
				"api_key": None,
				"api_key_valid": False,
				"api_key_valid_date": None,
			}, indent=4))
	else:
		with open("config/config.json", "r") as config_file:
			file_contents = config_file.read()
			if file_contents:
				config_data = json.loads(file_contents)
				if config_data["sessions"] == [] or config_data["last_session"] is None or config_data["last_session"] == "":
					config_data["last_session"] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
					with open("config/config.json", "w") as config_file_write:
						config_file_write.write(json.dumps(config_data, indent=4))
			# Generating a new session object inside the sessions list.
			with open("config/config.json", "r") as config_file:
				file_contents = config_file.read()
				if file_contents:
					config_data = json.loads(file_contents)
				else:
					config_data = {
						"sessions": [],
						"last_session": None
					}

				# Append a new session every time the program starts
				config_data["sessions"].append({
					"uuid": str(uuid.uuid4()),
					"date": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
					"videos": [],
				})
				with open("config/config.json", "w") as config_file_write:
					config_file_write.write(json.dumps(config_data, indent=4))
				append_log("Created a new session with the UUID: " + config_data["sessions"][-1]["uuid"])

	# Now we check the arguments position and if the flag -cs automatically we will clean the array of sessions
	args = sys.argv
	if len(args) > 1:
		if args[1] == "-cs":
			print(Fore.LIGHTBLUE_EX + "[CLEANER]: " + Fore.RESET + "Erasing all session on config.json")
			time.sleep(3)
			with open("config/config.json", "r") as config_file:
				file_contents = config_file.read()
				if file_contents:
					config_data = json.loads(file_contents)
					config_data["sessions"] = []
					config_data["last_session"] = None
					with open("config/config.json", "w") as config_file_write:
						config_file_write.write(json.dumps(config_data, indent=4))
					append_log("Cleaned all sessions on config.json")
					os.system("cls" if os.name == "nt" else "clear")
					sys.exit(0)
	elif len(args) == 1 or args[1] == "":
		pass

	# Creating the "logs" folder
	if not os.path.exists("logs"):
		os.mkdir("logs")

	# Creating the "logs/edoc.log" file
	if not os.path.exists("logs/edoc.log"):
		with open("logs/edoc.log", "w") as log:
			log.write("")
			log.close()
	append_log("EDOC started")
	edocMenu()
	return True

def edocMenu():
    """
		This is the function that runs once created the session and all the files.
    """
    while True:
        custom_fig = Figlet(font='slant')
        print(custom_fig.renderText('EDOC'))
        print(Fore.LIGHTBLUE_EX + "EDOC - Every Day One Course" + Fore.RESET)
        print("===========================")
        print(Fore.LIGHTBLUE_EX + "1. " + Fore.RESET + "Start the lesson of the day.")
        print(Fore.LIGHTBLUE_EX + "2. " + Fore.RESET + "Open the last session.")
        print(Fore.LIGHTBLUE_EX + "3. " + Fore.RESET + "Open a session.")
        print(Fore.LIGHTBLUE_EX + "4. " + Fore.RESET + "Show the logs.")
        print(Fore.LIGHTBLUE_EX + "5. " + Fore.RESET + "Show config.json.")
        print(Fore.LIGHTBLUE_EX + "6. " + Fore.RESET + "Open the EDOC GitHub page.")
        print(Fore.LIGHTBLUE_EX + "7. " + Fore.RESET + "Exit.")
        
        menuOption = input(Fore.LIGHTBLUE_EX + "Select an option: " + Fore.RESET)
        
        if menuOption == "1":
            print(Fore.LIGHTBLUE_EX + "[EDOC]: " + Fore.RESET + "Starting the lesson of the day.")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
        elif menuOption == "2":
            print(Fore.LIGHTBLUE_EX + "[EDOC]: " + Fore.RESET + "Opening the last session.")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
        elif menuOption == "3":
            print(Fore.LIGHTBLUE_EX + "[EDOC]: " + Fore.RESET + "Opening a session.")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
        elif menuOption == "4":
            print(Fore.LIGHTBLUE_EX + "[EDOC]: " + Fore.RESET + "Opening the logs folder.")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
        elif menuOption == "5":
            print(Fore.LIGHTBLUE_EX + "[EDOC]: " + Fore.RESET + "Opening the config folder.")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
        elif menuOption == "6":
            print(Fore.LIGHTBLUE_EX + "[EDOC]: " + Fore.RESET + "Opening the EDOC GitHub page.")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
        elif menuOption == "7":
            print(Fore.LIGHTBLUE_EX + "[EDOC]: " + Fore.RESET + "Exiting the program.")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
            sys.exit(0)
        elif menuOption == "":
            os.system("cls" if os.name == "nt" else "clear")
            print(Fore.LIGHTRED_EX + "[EDOC]: " + Fore.RESET + "You didn't select any option.")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print(Fore.LIGHTRED_EX + "[EDOC]: " + Fore.RESET + "That Option does not exist!")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
            menuOption = ""

def edocStartLeason():
    """
		This is the function that runs when you select the option 1.
	"""
	# TODO: Read the config.json where the API Key is stored.
	
