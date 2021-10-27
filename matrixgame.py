'''
Created on Sep 12, 2021

Program will accept phone and zip code information from the user and verify format, then
prompt the user to play the matrix game. Program will prompt the user to input two 3 x 3 matrices,
prompt to perform different matrix operations, and display the results. Program implements numpy and
pandas to manipulate and display data.

'''
import re
import sys
import numpy as np
import pandas as pd

first_matrix = []
second_matrix = []

def print_matrix_contents(matrix):
    """ print the contents of the matrix """
    df = pd.DataFrame(matrix) #assign matrix to pandas dataframe
    print(df.to_string(header=False, index=False)) #display matrix

def input_matrix(matrix):
    """ accept user input for matrix and display """
    counter = 0
    while counter < 3: #count three rows of integers
        try:
            #for i in range(3): #for three lines
            a = [int(a) for a in input().split()] #record each number user enters as array
            if len(a) != 3: #count 3 columns of integers
                print("\nYou must enter 3 x 3 integers: ")
                print()#print empty line
            else:
                #first_matrix.append(a) #add each array to list
                matrix.append(a)
                counter += 1 #add to counter
        except ValueError: #if user enters a non integer value
            print("\nYou must enter 3 x 3 integer values:")
            print() #print empty line

def prompt_matrices():
    """ prompt user to enter matrix values """
    #first_matrix = [] #declare list to add numbers
    #second_matrix = [] #declare second matrix
    print("\nHere is an example matrix: ")
    print("\n1 2 3"
          "\n4 5 6"
          "\n7 8 9")
    print("\nEnter your first 3 x 3 matrix: ")
    print()
    #call function to create first matrix
    input_matrix(first_matrix)
    print("\nYou entered: ") #display matrix
    print() #print empty line
    print_matrix_contents(first_matrix) #display result
    print("\nEnter your second 3 x 3 matrix: ")
    print() #print empty line
    #call function to create second matrix
    input_matrix(second_matrix)
    print("\nYou entered: ") #display matrix
    print() #print empty line
    print_matrix_contents(second_matrix) #display result

def calculate_mean(matrix):
    """ calculate the mean of each row and each column of a matrix """
    rows = matrix.mean(axis=1) #calculate mean of each row
    columns = matrix.mean(axis=0) #calculate mean of each column
    #print("\nRows:", ", }".join([str(elem) for elem in rows]))
    print("\nRows:", ", ".join(["{:.2f}".format(elem) for elem in rows]))
    print("\nColumns:", ", ".join(["{:.2f}".format(elem) for elem in columns]))

def transpose_matrix(matrix):
    """ transpose the matrix """
    tranposed_matrix = matrix.T #call function to transpose matrix
    print_matrix_contents(tranposed_matrix) #display results

def add_matrices():
    """ add matrices together """
    #declare numpy matrices
    first_numpy_matrix = np.array(first_matrix)
    second_numpy_matrix = np.array(second_matrix)
    #perform matrix addition
    result = first_numpy_matrix + second_numpy_matrix
    print("\nYou chose matrix addition. The results are: ")
    print() #print empty line
    print_matrix_contents(result) #display results
    print("\nThe transpose is: ")
    print() #print empty line
    transpose_matrix(result) #display transpose results
    print("\nThe row and column mean values of the results are: ")
    calculate_mean(result) #display mean results

def subtract_matrices():
    """ subtract matrix 2 from matrix 1 """
    #declare numpy matrices
    first_numpy_matrix = np.array(first_matrix)
    second_numpy_matrix = np.array(second_matrix)
    #perform matrix subtraction
    result = second_numpy_matrix - first_numpy_matrix
    print("\nYou chose matrix subtraction. The results are: ")
    print() #print empty line
    print_matrix_contents(result)
    print("\nThe transpose is: ")
    print() #print empty line
    transpose_matrix(result) #display transpose results
    print("\nThe row and column mean values of the results are: ")
    calculate_mean(result) #display mean results

def multiply_matrices():
    """ perform matrix multiplication using matmul """
    #declare numpy matrices
    first_numpy_matrix = np.array(first_matrix)
    second_numpy_matrix = np.array(second_matrix)
    #perform matrix multiplication
    result = np.matmul(first_numpy_matrix, second_numpy_matrix)
    print("\nYou chose matrix multiplication. The results are: ")
    print() #print empty line
    print_matrix_contents(result)
    print("\nThe transpose is: ")
    print() #print empty line
    transpose_matrix(result) #display transpose results
    print("\nThe row and column mean values of the results are: ")
    calculate_mean(result) #display mean results

def multiply_elements():
    """ multiply matrices element by element """
    #declare numpy natrices
    first_numpy_matrix = np.array(first_matrix)
    second_numpy_matrix = np.array(second_matrix)
    #perform element multiplication
    result = first_numpy_matrix * second_numpy_matrix
    print("\nYou chose element by element multiplication. The results are: ")
    print() #print empty line
    print_matrix_contents(result)
    print("\nThe transpose is: ")
    print() #print empty line
    transpose_matrix(result) #display transpose results
    print("\nThe row and column mean values of the results are: ")
    calculate_mean(result) #display mean results

def enter_phone():
    """ prompt user to enter phone number and very format """
    while True:
        try:
            phone_number = input("\nPlease enter your phone number (XXX-XXX-XXXX): ")
            #declare format to match and compare user entry
            result = re.fullmatch(r'(\d{3})-(\d{3})-(\d{4})', phone_number)
            if not result: #print if not full match
                print(f"\n{phone_number} is not a valid phone number. Please try again.")
            else: #print if match
                print(f"\n{phone_number} accepted.")
                break #exit loop
        except ValueError:
            print("\nInvalid entry.") #message if wrong value

def enter_zip():
    """ prompt user to enter phone number and very format """
    while True:
        try:
            zip_code = input("\nPlease enter your zip code +4 (XXXXX-XXXX): ")
            #declare format to match and compare user entry
            result = re.fullmatch(r'(\d{5})-(\d{4})', zip_code)
            if not result: #print if not full match
                print(f"\n{zip_code} not valid. Please try again.")
            else: #print if match
                print(f"\n{zip_code} accepted.")
                break #exit loop
        except ValueError:
            print("Invalid entry.") #message if wrong value

def play_matrix_game():
    """ display game menu and prompt user for selections """
    while True:
        try:
            #display matrix game menu
            print("\nMenu: "
                  "\n1. Addition"
                  "\n2. Subtraction"
                  "\n3. Matrix multiplication"
                  "\n4. Element by element multiplication"
                  "\n5. Exit program")
            selection = int(input("\nPlease Choose: ")) #prompt user for selection input
            if selection == 1:
                add_matrices() #call addition function
            elif selection == 2:
                subtract_matrices() #call subtraction function
            elif selection == 3:
                multiply_matrices() #call multiplication function
            elif selection == 4:
                multiply_elements() #call element multiplication function
            elif selection == 5:
                print("\nThank you for playing the Python Matrix Game!")
                sys.exit() #exit program
            else: #print if invalid selection
                print("\nInvalid selection.")
        except ValueError: #print if invalid value
            print("\nInvalid selection.")

def display_menu():
    """ user menu to run application """
    enter_phone() #prompt user to enter phone number
    enter_zip() #prompt user to enter zip code
    while True: #display menu until user exits
        try: #ask user to play th ematrix game
            selection = input("\nWould you like to play the matrix game?"
                              " Please enter Y for yes or N for no: ")
            if selection.upper() == 'Y': #if yes start program
                prompt_matrices() #call function to enter matrices
                play_matrix_game() #call function to present matrix operations
            elif selection.upper() == 'N': #if no end program
                print("\nThank you for using the program! Goodbye.") #bye!
                break #exit loop
            else:
                print("\nInvalid selection.") #message if invalid choice
        except ValueError:
            print("Invalid entry.") #message if wrong value

print("********************* Welcome to the Python Matrix Application *********************")
display_menu()
