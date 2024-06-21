import argparse
import os
import sys
import time
import json
import datetime
import random
import requests

global level

def printStatusMessage():
    with open('config.txt', 'r') as configFile:
        # Read the entire file content
        f = configFile.read()
        # Split the file content into lines
        splitted_file = f.split('\n')
        # Initialize currentLevel and currentExercise variables
        currentLevel = None
        currentExercise = None
        # Iterate through each line to find 'currentLevel' and 'exercise'
        for line in splitted_file:
            if 'currentLevel' in line:
                # Extract the current level by splitting the line
                currentLevel = line.split(': ')[1]
            elif 'exercise' in line:
                # Extract the current exercise by splitting the line
                currentExercise = line.split(': ')[1]
            # Break the loop if both values have been found
            if currentLevel and currentExercise:
                break
    
    # Prepare the message with the extracted current level and exercise
    message = f"""
        ExamShell Redefined 1.0
        =======================
        You are now at level {currentLevel}
        Your current exercise is \033[33m{currentExercise}\033[0m
    """
    print(message)

def parseSubject(level:str = None, currentExercise:str = None):
    # Parse the subject and write it on a txt file.
    with open(f'{os.getcwd()}/core/data/rank{args.exam_rank}.json', 'r') as dataFile:
        file = json.load(dataFile)
        # With the name, find the subject
        if not level:
            pass
        else:
            return "No subject found!"

def handleFinish():
    print("Finishing the exam session!")
    time.sleep(2)
    sys.exit(0)

# First, parse the command line arguments
parser = argparse.ArgumentParser(description='Generate a new exam')
parser.add_argument('exam_rank', type=str, help='The rank of the exam')

args = parser.parse_args()

# Next, generate the exam
if args.exam_rank == '02':
    # Create a config file with the exam rank, username, and timestamp
    with open('config.txt', 'w') as f:
        f.write('exam_rank: 02\n')
        f.write('username: {}\n'.format(os.environ['USER']))
        f.write('timestamp: {}\n'.format(datetime.datetime.now()))
    
    # Now check if the config file was created
    if os.path.exists('config.txt'):
        # In this part, we will take the json file with the exam data and based on that we will generate the exam
        print("Parsing the exam rank 02 json file and generating the exam")
        with open(f'{os.getcwd()}/core/data/rank{args.exam_rank}.json') as f:
            # Print the data from the json file
            data = json.load(f)
            # Now we will set the currentLevel inside the config file to 0
            with open('config.txt', 'a') as f:
                f.write('currentLevel: 1\n')
            # Now take 4 random exercise names from the json file
            exercises = random.sample(data['exercises']['level1'], 4)
            # Now take one random exercise from the exercises
            exercise = random.choice(exercises)
            # Now write the exercise name to the config file
            with open('config.txt', 'a') as f:
                f.write('exercise: {}\n'.format(exercise['name']))
            # And finally, print the exercise name
            print("Exercise name: \033[32m{}\033[0m".format(exercise['name']))
            while True:
                print("Do you want to start the exercise? (yes/no)")
                answer = input()
                if answer == 'yes':
                    print("Starting the exercise")
                    os.makedirs(f'{os.getcwd()}/ExamRank02/level1/{exercise["name"]}')
                    break
                elif answer == 'no':
                    print("Exiting the program")
                    break
                else:
                    print("Invalid answer")
            while True:
                os.system('clear' or 'cls')
                printStatusMessage()
                parseSubject()
                prompt = input("\033[33mexamshell>\033[0m")

                if prompt == "status":
                    printStatusMessage()
                elif prompt == "finish":
                    handleFinish()
            
    else:
        print('Exam generation failed')