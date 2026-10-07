from asyncio.windows_events import NULL
from platform import system
import random
import os
from settings import difficulty, from_to

if difficulty > 3 or difficulty < 1:
    difficulty = 1

os.system('cls')

running = True
wrong = False
answered = False

def input_control(i):
    global running
    global wrong
    global answered
    if i == "q" or i == "quit":
        running = False
        wrong = False
    elif i == "e" or i == "exit":
        wrong = False
        answered = False
        os.system('cls')
    elif i == "a" and not answered or i == "answer" and not answered:
        os.system('cls')
        answered = True
        print("the answer is: " + str(problem))
        inpt()
    else:
        problem_control(i)

def problem_control(i):
    global wrong
    if i == float(problem):
        os.system('cls')
    else:
        wrong = True
        os.system('cls')
        wrong_ans()

def wrong_ans():
    global wrong
    wrong = True
    print("Incorrect answer or invalid entry")
    print(problem_print[0], problem_print[1], problem_print[2], problem_print[3])
    inpt()

def inpt():
    get = input()
    try:
        i = float(get)
    except ValueError:
        i = str(get)
    input_control(i)

while running:
    count = 0
    ints = []
    problem_print = []
    add = 1

    while count < 4:
        count += 1
        if difficulty + add < 4 and count > 2:
            ints.append(" ")
            add += 1
        else:
            ints.append(random.randint(from_to[0], from_to[1]))

    count = 0
    problem = 0
    problem_print = []

    for a in ints:
        type = random.randint(1, 4)
        if a != " ":
            if type == 2:
                mark = "-"
                problem -= int(a)
            elif type == 3 and count > 0:
                mark = "/"
                problem = problem / int(a)
            elif type == 4 and count > 0:
                mark = "*"
                problem = problem * int(a)
            else:
                mark = "+"
                problem += int(a)
            if mark == "+" and count == 0:
                problem_print.append(str(a))
            else:
                problem_print.append(mark + " " + str(a))
            count += 1
        else:
            problem_print.append(" ")


    print(problem_print[0], problem_print[1], problem_print[2], problem_print[3])
    inpt()
