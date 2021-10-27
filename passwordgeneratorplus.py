'''
Created on Aug 27, 2021

Create a menu-driven Python application providing users with the ability to perform several math
and security related functions.

'''

import string
import secrets
from datetime import date
import math

#define functions to run program

def generate_password():
    """ prompt user to generate a secure password """
    while True:
        try:
            #prompt user to choose password complexity
            print("\n1. Generate a mixed-case alphanumeric password with symbols." \
                    "\n2. Generate a simple password using only letters.")
            complexity = int(input("\nPlease make a selection: "))
            if complexity == 2:
                simple_pass() #call simple password function
                break
            if complexity == 1:
                alphanum_pass() #call alphanumeric password function
                break
            if complexity < 1:
                print("\nPlease enter a valid selection.")
            else:
                print("\nPlease enter a valid selection.")
        except ValueError:
            print("\nPlease enter a valid selection.")
#end generate_password()

def simple_pass():
    """ generate a simple password based on user input """
    while True:
        try:
            #prompt user to choose password length
            pass_length = int(input("\nEnter number of characters: "))
            if pass_length < 1:
                print("\nPlease enter a positive number.")
            else:
                break
        except ValueError:
            print("\nPlease enter an integer value.")

    while True:
        try:
            #prompt user to choose password complexity
            print("\nPlease choose: " \
                   "\n1. Mixed case letters." \
                  "\n2. Lower case letters.")
            case_preference = int(input("\nEnter selection: "))
            if case_preference == 2:
                alphabet = string.ascii_lowercase
                password = ''.join(secrets.choice(alphabet) for i in range(pass_length))
                break
            if case_preference == 1:
                alphabet = string.ascii_letters
                password = ''.join(secrets.choice(alphabet) for i in range(pass_length))
                break
            if case_preference < 1:
                print("\nPlease make a valid selection.")
            else:
                print("\nPlease make a valid selection.")
        except ValueError:
            print("\nPlease make a valid selection.")

    print("\nYour secure password is:", password) #display password
#end simple_pass()

def alphanum_pass():
    """ generate alphanumeric password with at least one upper case,
        one lower case, one symbol, and three digits """
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        try:
            #prompt user to choose password length
            pass_length = int(input("\nEnter number of characters: "))
            if pass_length < 10:
                print("\nPassword must be at least 10 characters.")
            else:
                break
        except ValueError:
            print("\nPlease enter an integer value.")

    while True:
        #generate password
        password = ''.join(secrets.choice(alphabet) for i in range(pass_length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(not c.isalnum() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break

    print("\nYour secure password is:", password) #display password
#end alphanum_pass()

def prompt_percentage():
    """ prompt user for values to calculate a percentage """
    while True:
        try:
            #the amoun to be divided
            value = int(input("\nPlease enter an integer value to be expressed as a percent: "))
            if value < 0:
                print("\nValue must be a positive whole number.")
            else:
                break
        except ValueError:
            print("\nValue must be a positive whole number.")

    while True:
        try:
            #the total amount to divide by
            total_value = int(input("\nPlease enter the total value: "))
            if total_value < 1:
                print("\nTotal value must be greater than zero.")
            else:
                break
        except ValueError:
            print("\nPlease enter an integer value.")

    while True:
        try:
            decimal_points = int(input("\nUp to how many decimal places do you want?" \
                                       " Enter a value from 1 to 4: "))
            if decimal_points > 4 or decimal_points < 1:
                print("\nNot a valid choice.") #limit number of decimal points
            else:
                break
        except ValueError:
            print("\n Please enter a valid choice.")

    #call formula to calculate percentage passing in user values
    calc_percentage(value, total_value, decimal_points)
#end prompt_percentage()

def calc_percentage(value, total_value, decimal_points):
    """ calculate percentage with values from prompt_percentage() """
    percentage = (value/total_value) * 100 # calculate percentage
    percentage = round(percentage, decimal_points) # format number of decimal points
    print(f"\n{value} is {percentage}% of {total_value}.") # display result
#end calc_percentage()

def calculate_days_until():
    """ calculate days until July 4, 2025 """
    today = date.today() # use date class to call today's date
    projected_date = date(2025, 7, 4) # define projected date
    days_until = (projected_date - today) # subtract
    print(f"\nThere are {days_until.days} days until July 4, 2025.") # display result
#end calculate_days_until()

def prompt_triangle():
    """ prompt user for sides and angle of triangle """
    while True:
        try:
            length_a = int(input("\nEnter the length of side (a): "))
            if length_a < 1:
                print("\nValue must be greater than zero.")
            else:
                break
        except ValueError:
            print("\nPlease enter an integer value.")

    while True:
        try:
            length_b = int(input("\nEnter the length of side (b): "))
            if length_b < 1:
                print("\nValue must be greater than zero.")
            else:
                break
        except ValueError:
            print("\nPlease enter an integer value.")

    while True:
        try:
            angle_c = int(input("\nPlease enter the degrees of the opposite angle (C): "))
            if angle_c < 1:
                print("\nValue must be greater than zero.")
            else:
                break
        except ValueError:
            print("\nPlease enter an integer value.")

    #call function to calculate result passing in user values
    calc_leg_triangle(length_a, length_b, angle_c)
#end prompt_triangle()

def calc_leg_triangle(length_a, length_b, angle_c):
    """ use law of cosines to find leg of triangle """
    radians_c = math.radians(angle_c) #convert angle to radians
    length_c = (length_a**2) + (length_b**2) - (2 * (length_a * length_b)) * math.cos(radians_c)
    #law of cosines formula. value for length_c is c^2
    sqrt_c = math.sqrt(length_c) # find square root of c
    print(f"\nThe length of the leg (c) is: {sqrt_c: .2f}") # display result
#end calc_leg_triangle()

def calc_volume():
    """ prompt user to enter radius and height of cylinder """
    while True:
        try:
            height = int(input("\nPlease enter the height of the cylinder: "))
            if height < 1:
                print("\nValue must be greater than zero.")
            else:
                break
        except ValueError:
            print("\nPlease enter an integer value.")

    while True:
        try:
            radius = int(input("\nPlease enter the radius (base) of the cylinder: "))
            if radius < 1:
                print("\nValue must be greater than zero.")
            else:
                break
        except ValueError:
            print("\nPlease enter an integer value.")

    volume = (math.pi * (radius**2)) * height # formula to calculate volume

    print(f"\nThe volume of the cylinder is {volume: .2f} cubic units.") # display result

def menu():
    """ display user menu and prompt for selection """

    print("\nMenu: ")

    while True:
        print("\n1. Generate Secure Password." \
          "\n2. Calculate and Format a Percentage." \
          "\n3. How many days from today until July 4, 2025?" \
          "\n4. Use the Law of Cosines to calculate the leg of a triangle." \
          "\n5. Calculate the volume of a Right Circular Cylinder." \
          "\n6. Exit program.")
        try:
            selection = int(input("\nPlease make a selection: "))
            if selection == 1:
                generate_password()
            elif selection == 2:
                prompt_percentage()
            elif selection == 3:
                calculate_days_until()
            elif selection == 4:
                prompt_triangle()
            elif selection == 5:
                calc_volume()
            elif selection == 6:
                break
            else:
                print("\nNot a valid selection.")
        except ValueError:
            print("\nPlease enter a valid selection.")

    print("\nThank you for using the program! Have a nice day.")

print("Welcome to the Python math and security-related functions program!") #welcome message

menu() # run program by calling menu
