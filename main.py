# Project by: Murtaza Badshah
# Date: 06/26/2021

#--------Big Data Programming-------

import random

import shapes_helper
from shapes_helper import Rectangle, Triangle, Circle, Square, shapePrint

user = {}
acctName = ""
shapes = ["Rectangle", "Square", "Triangle", "Circle"]



def rectangle():

    number = random.randint(1, 9)
    number2 = random.randint(1, 9)

    shape1 = shapes_helper.Rectangle(number, number2)
    print("Please guess the Area and Perimeter of the Rectangle!")
    print("Hint: The length and breadth of the rectangle is: " + str(number) + " and " + str(number2))

    while True:
        try:
            area = int(input("Area: "))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    print("Area: ", area)

    while True:
        try:
            perimeter = int(input("Perimeter: "))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    print("Perimeter: ", perimeter)

    you_right_a = (shape1.area() == area)
    you_right_p = (shape1.peri() == perimeter)

    if you_right_a:
        if acctName in user:
            user[acctName] += 1
    else:
        print("Sorry wrong area!")


    if you_right_p:
        if acctName in user:
            user[acctName] += 1
    else:
        print("Sorry wrong perimeter!")
    # if you_right_a:
    #     for k,v in user.items():
    #         if user[k] in user:
    #             user[v] += 1
    #     # user[acctName] += 1 (This piece of code does not work for some reason)
    # else:
    #     print("Sorry wrong area!")
    #
    # if you_right_p:
    #     for k, v in user.items():
    #         if user[k] in user:
    #             user[v] += 1
    # else:
    #     print("Sorry wrong perimeter!")

def square():
    number = random.randint(1, 9)

    shape1 = shapes_helper.Square(number)
    print("Please guess the Area and Perimeter of the Square!")
    print("Hint: The side of the Square is: " + str(number))

    while True:
        try:
            area = int(input("Area: "))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    print("Area: ", area)

    while True:
        try:
            perimeter = int(input("Perimeter: "))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    print("Perimeter: ", perimeter)

    you_right_a = (shape1.area() == area)
    you_right_p = (shape1.peri() == perimeter)

    if you_right_a:
        if acctName in user:
            user[acctName] += 1
    else:
        print("Sorry wrong area!")

    if you_right_p:
        if acctName in user:
            user[acctName] += 1
    else:
        print("Sorry wrong perimeter!")

def circle():
    number = random.randint(1, 9)

    shape1 = shapes_helper.Circle(number)
    print("Please guess the Area and Circumference of the Circle!")
    print("Hint: The Radius of the circle is: " + str(number))

    while True:
        try:
            area = float(input("Area: "))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    print("Area: ", area)

    while True:
        try:
            perimeter = float(input("Perimeter: "))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    print("Perimeter: ", perimeter)

    you_right_a = (shape1.area() == area)
    you_right_p = (shape1.peri() == perimeter)

    if you_right_a:
        if acctName in user:
            user[acctName] += 1
    else:
        print("Sorry wrong area!")

    if you_right_p:
        if acctName in user:
            user[acctName] += 1
    else:
        print("Sorry wrong perimeter!")

def triangle():
    number = random.randint(1, 9)
    number2 = random.randint(1, 9)
    number3 = random.randint(1, 9)
    number4 = random.randint(1, 9)

    shape1 = shapes_helper.Triangle(number, number2, number3, number4)
    print("Please guess the Area and perimeter of the Triangle!")
    print("Hint: The dimensions of the Triangle (a, b, c) are: " + str(number) + ", " + str(number3) + ", " + str(number4) +".")
    print("Hint: The height of the triangle is " + str(number2))

    while True:
        try:
            area = float(input("Area: "))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    print("Area: ", area)

    while True:
        try:
            perimeter = float(input("Perimeter: "))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    print("Perimeter: ", perimeter)

    you_right_a = (shape1.area() == area)
    you_right_p = (shape1.peri() == perimeter)

    if you_right_a:
        if acctName in user:
            user[acctName] += 1
    else:
        print("Sorry wrong area!")

    if you_right_p:
        if acctName in user:
            user[acctName] += 1
    else:
        print("Sorry wrong perimeter!")

def registration():
    print("Welcome to the shape game! Here we test your guessing skills")
    print("Please create a new account and read the following instructions carefully!")

    global acctName
    acctName = input("First Name Only: ")
    user[acctName] = 0


    print("Congratulations! Your new account has been created!")
    print("==================================================")
    gamestart2()

def score():
    print("View all scores!")
    print("================")
    print("Name Scores")
    for key, value in user.items():
        print(key, ' : ', value)

    input("Press enter to go back to main menu!")

def exit():
    print("Thanks for playing good bye!")

# def gamestart():
#     print("Welcome to shape size guesser!")
#     response = 0
#
#     while 1 > response or 4 < response:
#         try:
#             response = int(input("Please enter the amount of shapes you would like to play with (1 - 4): "))
#         except ValueError:
#             print("That's not an integer! Please try again!")
#
#     if response == 1:
#         print("You have selected 1 shape")
#         selection1()
#     elif response == 2:
#         print("You have selected 2 shapes")
#         selection2()
#     elif response == 3:
#         print("You have selected 3 shapes")
#         selection3()
#     else:
#         print("You have selected 4 shapes")
#         selection4()

def gamestart2():
    print("Lets play the shapes game! How many shapes would you like to guess the area and perimeter off?")
    response = 0

    while 1 > response or 1000 < response:
        try:
            response = int(input("Please enter the amount of shapes you would like to play with: "))
        except ValueError:
            print("That's not an integer! Please try again!")

    selectionPlay(response)


def selectionPlay(response):

    print("++++++++++++++++++++++++++++++")
    print("You have selected to guess " + str(response) + " random shape's area and perimeter!")

    count = 0

    while count < response:
        shape = random.choice(shapes)

        print("Your randomly generated shape is: " + shape + "! ")
        shapes_helper.shapePrint(shape)

        if shape == "Rectangle":
            rectangle()
        elif shape == "Triangle":
            triangle()
        elif shape == "Circle":
            circle()
        else:
            square()

        count += 1

        if count == response:
            pass
        else:
            input("Press enter to guess the next shape!")


    playAgain = input("Great try!!! Would you like to continue playing? (1 = Yes, 2 = No): " )


    if playAgain == "1":
        gamestart2()

# def selection1():
#     print("++++++++++++++++++++++++++++++")
#     print("You have selected to guess one random shape's area and perimeter!")
#
#     shape = random.choice(shapes)
#
#     print("Your randomly generated shape is: " + shape + "! ")
#     shapes_helper.shapePrint(shape)
#
#
#     if shape == "Rectangle":
#         rectangle()
#     elif shape == "Triangle":
#         triangle()
#     elif shape == "Circle":
#         circle()
#     else:
#         square()
#
#     input("Press enter to go to main menu!")
#
# def selection2():
#     print("++++++++++++++++++++++++++++++")
#     print("You have selected to guess two random shape's area and perimeter!")
#
#     shape = random.choice(shapes)
#     shape2 = random.choice(shapes)
#
#     print("Your randomly generated shape is: " + shape + " and " + shape2)
#     shapes_helper.shapePrint(shape)
#     shapes_helper.shapePrint(shape2)
#
#
#     if shape == "Rectangle":
#         rectangle()
#     elif shape == "Triangle":
#         triangle()
#     elif shape == "Circle":
#         circle()
#     else:
#         square()
#
#     input("Press enter to move to the next shape!")
#
#     if shape2 == "Rectangle":
#         rectangle()
#     elif shape2 == "Triangle":
#         triangle()
#     elif shape2 == "Circle":
#         circle()
#     else:
#         square()
#
#     input("Press enter to go to main menu!")
#
# def selection3():
#     print("++++++++++++++++++++++++++++++")
#     print("You have selected to guess three random shape's area and perimeter!")
#
#     shape = random.choice(shapes)
#     shape2 = random.choice(shapes)
#     shape3 = random.choice(shapes)
#
#     print("Your randomly generated shape is: " + shape + " and " + shape2 + " and " + shape3 + "!")
#     shapes_helper.shapePrint(shape)
#     shapes_helper.shapePrint(shape2)
#     shapes_helper.shapePrint(shape3)
#
#
#     if shape == "Rectangle":
#         rectangle()
#     elif shape == "Triangle":
#         triangle()
#     elif shape == "Circle":
#         circle()
#     else:
#         square()
#
#     input("Press enter to move to the next shape!")
#
#     if shape2 == "Rectangle":
#         rectangle()
#     elif shape2 == "Triangle":
#         triangle()
#     elif shape2 == "Circle":
#         circle()
#     else:
#         square()
#
#     input("Press enter to move to the next shape!")
#
#     if shape3 == "Rectangle":
#         rectangle()
#     elif shape3 == "Triangle":
#         triangle()
#     elif shape3 == "Circle":
#         circle()
#     else:
#         square()
#
#     input("Press enter to go to main menu!")
#
# def selection4():
#     print("++++++++++++++++++++++++++++++")
#     print("You have selected to guess four random shape's area and perimeter!")
#
#     shape = random.choice(shapes)
#     shape2 = random.choice(shapes)
#     shape3 = random.choice(shapes)
#     shape4 = random.choice(shapes)
#
#     print("Your randomly generated shape is: " + shape + ", " + shape2 + ", " + shape3 + " and " + shape4 + "!")
#     shapes_helper.shapePrint(shape)
#     shapes_helper.shapePrint(shape2)
#     shapes_helper.shapePrint(shape3)
#     shapes_helper.shapePrint(shape4)
#
#
#     if shape == "Rectangle":
#         rectangle()
#     elif shape == "Triangle":
#         triangle()
#     elif shape == "Circle":
#         circle()
#     else:
#         square()
#
#     input("Press enter to move to the next shape!")
#
#     if shape2 == "Rectangle":
#         rectangle()
#     elif shape2 == "Triangle":
#         triangle()
#     elif shape2 == "Circle":
#         circle()
#     else:
#         square()
#
#     input("Press enter to move to the next shape!")
#
#     if shape3 == "Rectangle":
#         rectangle()
#     elif shape3 == "Triangle":
#         triangle()
#     elif shape3 == "Circle":
#         circle()
#     else:
#         square()
#
#     input("Press enter to move to the next shape!")
#
#     if shape4 == "Rectangle":
#         rectangle()
#     elif shape4 == "Triangle":
#         triangle()
#     elif shape4 == "Circle":
#         circle()
#     else:
#         square()
#
#     input("Press enter to go to main menu!")

registration()
# print("===========================================")
# print("--------Welcome to Shapes Game!---------")
# print("*******************************************")
# print("  Please read the instructions carefully.  ")
# print("*****   1. Register                 *****")
# print("*****   2. View Scores                *****")
# print("*****   3. Exit                       *****")
# print("*******************************************")
#
# selection = input("Please enter the appropriate number for the option: ")
#
# if selection == "1":
#     registration()
# elif selection == "2":
#     score()
# elif selection == "3":
#     quit()
# else:
#     print("Incorrect input please try again!")

while True:
    print("===========================================")
    print("--------Welcome to Shapes Game!---------")
    print("*******************************************")
    print("  Please read the instructions carefully.  ")
    print("*****   1. Register                   *****")
    print("*****   2. View Scores                *****")
    print("*****   3. Exit                       *****")
    print("*******************************************")

    selection = input("Please enter the appropriate number for the option: ")

    if selection == "1":
        registration()
    elif selection == "2":
        score()
    elif selection == "3":
        exit()
        break
    else:
        print("Incorrect input please try again!")
