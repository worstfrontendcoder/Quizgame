
print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
if True:
 print("Okay! Let's play:)")
score = 0

answer = input("what does CPU stand for?")
if answer.lower() == "central processing unit":
    print("Correct!")
    print ("score = 50%")

    answer = input("What does RAM stand for?")
if answer.lower() == "random access memory":
    print("Correct!")
    print ("score = 60%")

    answer = input("what does GPU stand for?")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    print ("score = 70%")

    answer = input("what does PSU stand for?")
if answer.lower() == "power supply":
    print("Correct!")
    print ("score = 80%")
    print ("you have successfully beaten the game!")
    print ("congrats!")
    