"""
Created on Sep 19, 2021

Note: Requires files Housing.CSV and PopChange.csv!

Program purpose: Use pandas to read data about housing and population from CSV files.
Perform data analysis on selected columns and display histograms.
"""

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('float_format', '{:.2f}'.format)


def population_data():
    """ menu to analyze population data """
    try:
        population = pd.read_csv('PopChange.csv')  # read data from population file
    except FileNotFoundError:
        print("\nFile not found.")  # message if file not found
    else:
        print("\nReading population data.")  # message if file read
    dataframe = population.describe()  # create a dataframe for pandas analysis
    while True:  # display menu
        print("\n1. Pop Apr 1 \
          \n2. Pop Jul 1 \
          \n3. Change Pop \
          \n4. Return to main menu")
        try:  # prompt user to input column selection and call functions
            selection = int(input("\nSelect the column you want to analyze: "))
            if selection == 1:
                display_data(dataframe, 'Pop Apr 1')  # analyze selected column
                display_histogram(population, 'Pop Apr 1')  # display histogram
            elif selection == 2:
                display_data(dataframe, 'Pop Jul 1')  # analyze selected column
                display_histogram(population, 'Pop Jul 1')  # display histogram
            elif selection == 3:
                display_data(dataframe, 'Change Pop')  # analyze selected column
                display_histogram(population, 'Change Pop')  # display histogram
            elif selection == 4:
                break  # return to main menu
            else:
                print("\nInvalid selection.")  # message if invalid selection
        except ValueError:
            print("\nInvalid selection.")  # message if invalid input


def housing_data():
    """ menu to analyze housing data """
    try:
        housing = pd.read_csv('Housing.csv')  # read housing data from file
    except FileNotFoundError:
        print("\nFile not found.")  # message if file not found
    else:
        print("\nReading housing data.")  # message if file read
    dataframe = housing.describe()  # create dataframe for housing analysis
    while True:  # display menu to analyze housing data
        print("\n1. Age \
          \n2. Bedrooms \
          \n3. Built \
          \n4. Rooms \
          \n5. Utility \
          \n6. Return to main menu")
        try:  # prompt user to input column selection and call functions
            selection = int(input("\nSelect the column you want to analyze: "))
            if selection == 1:
                display_data(dataframe, 'AGE')  # analyze selected column
                display_histogram(housing, 'AGE')  # display histogram
            elif selection == 2:
                display_data(dataframe, 'BEDRMS')  # analyze selected column
                display_histogram(housing, 'BEDRMS')  # display histogram
            elif selection == 3:
                display_data(dataframe, 'BUILT')  # analyze selected column
                display_histogram(housing, 'BUILT')  # display histogram
            elif selection == 4:
                display_data(dataframe, 'ROOMS')  # analyze selected column
                display_histogram(housing, 'ROOMS')  # display histogram
            elif selection == 5:
                display_data(dataframe, 'UTILITY')  # analyze selected column
                display_histogram(housing, 'UTILITY')  # display histogram
            elif selection == 6:
                break  # return to main menu
            else:
                print("\nInvalid selection.")  # message if invalid selection
        except ValueError:
            print("\nInvalid selection.")  # message if invalid input


def display_data(dataset, column):
    """ display data from csv files """
    print(f'\nYou selected {column}')  # display data analysis for each column
    print(f"\nThe statistics for this column are: \
        \nCount = {dataset[column]['count']:.0f} \
        \nMean = {dataset[column]['mean']:,.2f} \
        \nStandard Deviation = {dataset[column]['std']:,.1f} \
        \nMin = {dataset[column]['min']:,.0f} \
        \nMax = {dataset[column]['max']:,.0f}")


def display_histogram(dataset, column):
    """ display histogram for selected column """
    print("\nThe histogram for this dataset is: ")
    # format histogram excluding extreme outliers
    dataset[column][dataset[column] < 3.1e6][dataset[column] > -5.3e5].hist()
    plt.suptitle(column)  # add super title to histogram
    plt.show()  # show histogram


def menu():
    """ display user menu """
    print("\nMenu: ")
    while True:
        try:  # select population or housing data
            print(("\n1. Population Data \
                    \n2. Housing Data \
                    \n3. Exit program"))
            selection = int(input("\nSelect the file you want to analyze: "))
            if selection == 1:
                population_data()  # call function to read population file
            elif selection == 2:
                housing_data()  # call function to read housing file
            elif selection == 3:
                print("\nThank you for using the program. Have a nice day!")
                break  # exit program
            else:
                print("\nInvalid selection.")  # message if invalid selection
        except ValueError:
            print("\nInvalid selection.")  # message if invalid input


# display welcome message
print("************ Welcome to the Python Data Analysis App ***********")
menu()  # display menu
