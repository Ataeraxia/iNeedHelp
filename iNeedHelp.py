# Program that checks if you've taken care of yourself
import time

print("Just by the way, this project is unfinished.")
time.sleep(3)

print("Let's start with your physiological needs.")
time.sleep(2)

print("You need to breathe, eat, drink water, sleep, regulate temperature, and use the washroom.")
time.sleep(4)

print("Have you practiced breathing regulation yet?")

print("Please reply with a lower case y or n")

didBreathe = input()

if didBreathe == "n":
    print("Okay, let's do some breathing exercises.")
    time.sleep(2)

    print("Breathe in, breathe out.")
    time.sleep(10)

    print("Hopefully you feel at least a little better.")


elif didBreathe != "y":
    print("You responded with a character that was not y or n. I'm shutting down now.")

print("Okay, let's move on to the next activity.")
time.sleep(3)

print("Get yourself a glass of water. I'll wait here until you type some input.")

input()

print("Good job.")

print("Get some food.")
input()

print("Put on a sweater or cool down.")
input()

print("Use the washroom.")
input()

print("Take a nap.")
input()

print("You're done!")
