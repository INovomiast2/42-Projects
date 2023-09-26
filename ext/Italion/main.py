# Italion, automate your life!
import sys

# Variables
args = sys.argv


# Checks
for i in args:
    if args[1] == "--help":
        print("Slack")
    elif args == "--please":
        print("Kill")
