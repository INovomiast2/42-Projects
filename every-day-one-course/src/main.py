# EDOC - Every Day One Course, 2023 by INovomiast2
"""
	This is the main file for EDOC.

	EDOC is a project that will help you to learn something new every day.
	You can use it to learn new programming languages, frameworks, libraries, etc.
	You can also use it to learn new things about your current programming language.

	EDOC uses the YouTube API to get you a random video about the topic you want to learn.
	Once the course is randomly selected, automatically opens the video on a monitored browser window.
	It will also show you the title of the video and the channel that uploaded it.
	And the most important thing is that it's capable of keeping record of different stats like:
		- How many pauses you made.
		- How total time you spent watching the video.
		- How much those pauses were. (It starts a timer when you pause the video and stops it when you resume it).
		- It tracks your progress. (It will show you how much of the video you have watched).
		- It will block the video and show you a message for you to take a break after a certain amount of time.
		- It will display your stats at the end of the video.
		- It will save your stats in a file.
		- It will show you a message when you have finished the course.
		- And more...
	
	EDOC is a project that I'm doing to learn Python and to learn how to use the YouTube API.
	Feel free to use it and modify it as you want.
	You can also contribute to the project if you want to.
	You can contact me at:
		- Discord: INovomiast2#0000
		- Twitter: @INovomiast2
		- Email: idimnovdie1602@protonmail.com or contact@inovomiast.live
		- GitHub: https://github.com/INovomiast2

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
from colorama import Fore, Back, Style, init
from lib import edoc

import keyboard

# Importing EDOC modules
from lib import netpy

def main():
	# Clearing the screen
	os.system("cls" if os.name == "nt" else "clear")
	# Checkimg if the user has internet connection.
	if netpy.check.connection() == True:
		print(Fore.LIGHTYELLOW_EX + "[EDOC] " + Fore.RESET + "Internet connection: " + Fore.LIGHTGREEN_EX + "OK" + Style.RESET_ALL)
		time.sleep(1)
		print("========================================")
		print(Fore.LIGHTYELLOW_EX + "[EDOC] " + Fore.RESET + "Today is: " + Fore.LIGHTGREEN_EX + str(datetime.datetime.now().strftime("%d/%m/%Y")) + Style.RESET_ALL)
		print(Fore.LIGHTYELLOW_EX + "[EDOC] " + Fore.RESET + "Today's time is: " + Fore.LIGHTGREEN_EX + str(datetime.datetime.now().strftime("%H:%M:%S")) + Style.RESET_ALL)
		print("========================================")
		if len(sys.argv) > 1:
			if sys.argv[1] == "--dev":
				time.sleep(1)
				edoc.init()
		elif len(sys.argv) == 1 or sys.argv[1] == "":
			# Loading Screen
			for i in range(0, 101):
				time.sleep(0.05)
				sys.stdout.write("\r" + Fore.LIGHTYELLOW_EX + "[EDOC] " + Fore.RESET + "Loading EDOC... " + Fore.LIGHTGREEN_EX + str(i) + "%" + Style.RESET_ALL)
				sys.stdout.flush()
				# Running the program
				if i == 100:
					edoc.init()
			
		

	else:
		print(Fore.LIGHTYELLOW_EX + "[EDOC] " + Fore.RESET + "Internet connection: " + Fore.RED + "KO" + Style.RESET_ALL)
		sys.exit(1)


'''
def blockKeyboard():
    for i in range(150):
        keyboard.block_key(i)
    time.sleep(600)
'''


if __name__ == "__main__":
	init(autoreset=True)
	main()