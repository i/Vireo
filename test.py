import composer as c
import random

number = 0
moodList = [1, 0, 1, 0, 1]

def makeMelody():
    global number
    happylist = ['I love rhinos #yolo420swag #mercurialRules', 'got me on this zumba shit in my balls #yolo420swag :(', "The recommended approach to subprocesses is to use the following convenience", "Kill me now omg idk what is going on dude #wtf", 'alright here is one more just make a cool melody']
    melody = c.melodize(happylist[number], moodList[number])
    number += 1
    if (number > 4):
        number = 0
    c.midFile(melody)
