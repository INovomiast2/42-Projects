# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ivnovomi <ivnovomi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/27 20:08:20 by ivnovomi          #+#    #+#              #
#    Updated: 2023/09/27 20:50:53 by ivnovomi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
    Welcome to mainer.py, this is the tool that will help you test the
    libft project.

    Paco is not avaliable for corrections, so my idea is to develop a tool
    that will help you to pass the corrections.

    To use this tool, you need to pass the path of your libft project in the
    mainer.conf file.

    DEFAULT_PATH = SAME AS USERS PATH
    CUSTOM_PATH = mainer -config-path /path/to/your/libft

    Mainer will compile your libft and run the tests.

    Mainer - Developed by INovomiast2 (ivnovomi <Intra42>) - (c) 2023
"""

# Main Modules (This will make the app work totally).
import os
import sys
import subprocess
import configparser
import colorama as cl
import time
import platform

# Check init file.
def check_files():
    if os.path.exists("$HOME/mainer"):
        print(cl.Fore.GREEN + "[OK] " + cl.Fore.RESET + "Mainer is SettedUp!")
        return (True)
    else:
        print(cl.Fore.RED + "[ERROR] " + cl.Fore.RESET + "Mainer is not installed.")
        time.sleep(1)
        print(cl.Fore.YELLOW + "[INFO] " + cl.Fore.RESET + "Setting Up Mainer...")
        # Check the OS. (We wan't max compatibility).
        if platform.system() == "Windows":
            os.mkdir("C:\\Users\\%USERNAME%/mainer")
        elif platform.system() == "Linux":
            os.mkdir("$HOME/mainer")
        elif platform.system() == "Darwin":
            os.mkdir("$HOME/mainer")
        else:
            print(cl.Fore.RED + "[ERROR] " + cl.Fore.RESET + "Your OS is not supported.")
            sys.exit(1)
        time.sleep(2)
        print(cl.Fore.YELLOW + "[INFO] " + cl.Fore.RESET + "Mainer folder created.")
        # Create the config folder and files.
        if platform.system() == "Windows":
            os.mkdir("C:\\Users\\%USERNAME%\\mainer/config")
            # Create the general.ini file.
            config = configparser.ConfigParser()
            config["DEFAULT"] = {"DEFAULT_PATH": f"{os.getcwd()}/libft"}
            config["CUSTOM"] = {"CUSTOM_PATH": "mainer -config-path /path/to/your/libft"}
            config["TESTS"] = {"TESTS_PATH": "mainer -config-path /path/to/your/tests"}
            config["NORMINETTE"] = {"NORMINETTE_PATH": "mainer -config-path /path/to/your/norminette"}
            with open("C:\\Users\\%USERNAME%\\mainer\\config/general.ini", "w") as configfile:
                config.write(configfile)
        elif platform.system() == "Linux":
            os.mkdir("$HOME/mainer/config")
            # Create the general.conf file.
            config = configparser.ConfigParser()
            config["DEFAULT"] = {"DEFAULT_PATH": f"{os.getcwd()}/libft"}
            config["CUSTOM"] = {"CUSTOM_PATH": "mainer -config-path /path/to/your/libft"}
            config["TESTS"] = {"TESTS_PATH": "mainer -config-path /path/to/your/tests"}
            config["NORMINETTE"] = {"NORMINETTE_PATH": "mainer -config-path /path/to/your/norminette"}
            with open("$HOME/mainer/config/general.conf", "w") as configfile:
                config.write(configfile)
        elif platform.system() == "Darwin":
            os.mkdir("$HOME/mainer/config")
            # Create the general.conf file.
            config = configparser.ConfigParser()
            config["DEFAULT"] = {"DEFAULT_PATH": f"{os.getcwd()}/libft"}
            config["CUSTOM"] = {"CUSTOM_PATH": "mainer -config-path /path/to/your/libft"}
            config["TESTS"] = {"TESTS_PATH": "mainer -config-path /path/to/your/tests"}
            config["NORMINETTE"] = {"NORMINETTE_PATH": "mainer -config-path /path/to/your/norminette"}
            with open("$HOME/mainer/config/general.conf", "w") as configfile:
                config.write(configfile)
        elif platform.system() != ["Windows", "Linux", "Darwin"]:
            print(cl.Fore.RED + "[ERROR] " + cl.Fore.RESET + "Your OS is not supported.")
            sys.exit(1)

if __name__ == "__main__":
    # Always clear the console before running the app.
    os.system("clear")
    # Check if the user has mainer config folders and files created (Runned only once or more than once).
    check_files()
    if check_files:
        # Parse the config file.
        pass