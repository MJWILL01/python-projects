import random
import time


randomNumber = 0
testIfExit = ""


def randBall():

    while True:
        randomNumber = random.randint(1,6)
        testExit = input("Please ask a yes or no question! To exit type 'e': ")
        if testExit == "e":
            break
        
        else:
            waitTime(1)    
            outputUser = outputBall[randomNumber-1]
            print(outputUser)


def waitTime(x):
    print("... \n")
    print("Calculating...")
    time.sleep(x)
    print(".. \n")


print("   ___    ____            _   _ ")
print("  ( _ )  | __ )    __ _  | | | |")
print("  / _ \  |  _ \   / _` | | | | |")
print(" | (_) | | |_) | | (_| | | | | |")
print("  \___/  |____/   \__,_| |_| |_|              title taken from messletters.com")

time.sleep(1)
print("\n")
name = input("What is your name? ")
outputBall = ["Maybe next time %s" % name,
              "Never, %s" % name,
              "Definitely, %s" % name,
              "Mmm... Idk, %s..." % name,
              "Actualy possible, %s." % name,
              "Maybe not, %s" % name]

randBall()
