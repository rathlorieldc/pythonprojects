'''
Created on Sep 3, 2021

@author: Deysha Rivera - SDEV 300, Project 3

Create a project that allows the user to display state, state capital, state flower,
and overall population for all 50 states. The program allows the user to search for a
specific state and display data and an image of the state flower. The program allows the user
to update population for a specific state, and provides an option to show a graph of the top
5 most populated states.

'''
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

states_dict = {
    'Alabama': ('Montgomery', 'Camelia', 4903000),
    'Alaska': ('Juneau', 'Alpine forget-me-not', 731545),
    'Arizona':('Phoenix', 'Saguaro cactus blossom', 7279000),
    'Arkansas':('Little Rock', 'Apple blossom', 3018000),
    'California': ('Sacramento', 'California poppy', 39510000),
    'Colorado':('Denver', 'Colorado blue columbine', 5759000),
    'Connecticut':('Hartford', 'Mountain laurel', 3565000),
    'Delaware':('Dover', 'Peach blossom', 973764),
    'Florida': ('Tallahassee', 'Orange blossom', 21480000),
    'Georgia': ('Atlanta', 'Cherokee rose', 10620000),
    'Hawaii': ('Honolulu', 'Yellow hibiscus', 1416000),
    'Idaho': ('Boise', 'Syringa', 1787000),
    'Illinois': ('Springfield', 'Common blue violet', 12670000),
    'Indiana': ('Indianapolis', 'Peony', 6732000),
    'Iowa': ('Des Moines', 'Prairie Rose', 3155000),
    'Kansas': ('Topeka', 'Wild Sunflower', 2913000),
    'Kentucky': ('Frankfort', 'Giant goldenrod', 4468000),
    'Louisiana': ('Baton Rouge', 'Magnolia', 4649000),
    'Maine': ('Augusta', 'White Pine Cone', 1344000),
    'Maryland': ('Annapolis', 'Black-eyed Susan', 6046000),
    'Massachusetts': ('Boston', 'Mayflower', 6893000),
    'Michigan': ('Lansing', 'Apple Blossom', 10077331),
    'Minnesota': ('St. Paul', 'Showy lady\'s slippers', 5640000),
    'Mississippi': ('Jackson', 'Magnolia', 2976000),
    'Missouri': ('Jefferson City', 'White Hawthorn blossom', 6154913),
    'Montana': ('Helena', 'Bitterroot', 1069000),
    'Nebraska': ('Lincoln', 'Solidago', 1934000),
    'Nevada': ('Carson City', 'Big sagebrush', 3080000),
    'New Hampshire': ('Concord', 'Purple Lilac', 1360000),
    'New Jersey': ('Trenton', 'Common blue violet', 8882000),
    'New Mexico': ('Santa Fe', 'Yucca flower', 2097000),
    'New York': ('Albany', 'Rose', 19450000),
    'North Carolina': ('Raleigh', 'Dogwood flower', 10490000),
    'North Dakota': ('Bismarck', 'Prairie rose', 10490000),
    'Ohio': ('Columbus', 'Carnation', 11690000),
    'Oklahoma': ('Oklahoma City', 'Oklahoma rose', 3957000),
    'Oregon': ('Salem', 'Oregon Grape flower', 4218000),
    'Pennsylvania': ('Harrisburg', 'Mountain laurel', 12800000),
    'Rhode Island': ('Providence', 'Common blue violet', 1059000),
    'South Carolina': ('Columbia', 'Yellow jessamine', 5149000),
    'South Dakota': ('Pierre', 'American Pasque flower', 884659),
    'Tennessee': ('Nashville', 'Iris', 6829000),
    'Texas': ('Austin', 'Bluebonnet', 29183290),
    'Utah': ('Salt Lake City', 'Sego lily', 3206000),
    'Vermont': ('Montpelier', 'Red Clover', 623989),
    'Virginia': ('Richmond', 'Dogwood flower', 8536000),
    'Washington': ('Olympia', 'Pacific rhododendron', 7615000),
    'West Virginia': ('Charleston', 'Rhododendron', 1792000),
    'Wisconsin': ('Madison', 'Common blue violet', 5822000),
    'Wyoming': ('Cheyenne', 'Indian paintbrush', 578759)
} #dictionary of states (keys) and tuple (values) of capital, state flower, and state pop

def display_all_info():
    """function to display all states and data"""
    #iterate over states dictionary display all keys and values to user
    for state, value in sorted(states_dict.items()):
        print(f'\n{state} | Capital - {value[0]} |',
              f'State flower - {value[1]} | Population - {value[2]:,}')

def display_state():
    """ function to display information about a state and show flower image """
    while True:
        try:
            #prompt user to enter state
            state = input("\nPlease enter the name of the state: ")
            state = state.title() #format user input to match dictionary format
            if state not in states_dict: #check if state in dictionary
                print("\nState not found.") #message if state not found
            else:
                #print formatted info
                print(f'\n{state.title()} | Capital - {states_dict[state][0]} |',
                      f'State flower - {states_dict[state][1]} |',
                      f' Population - {states_dict[state][2]:,}')
                #message to close window to continue running program
                print("\nClose window to continue.")
                break #break out of loop
        except ValueError:
            print("\nNot a valid entry. Please try again.") #handle valueerror exception
    try:
        image_name = 'flowers/' + state.lower() + '.jpg' #concatenate user input to make file name
        img = mpimg.imread(image_name) #set image to filename
        imgplot = plt.imshow(img) #plot the image
        imgplot.autoscale() #autoscale image
        plt.axis('off') #turn of axes
        plt.title(f'{states_dict[state][1]}') #set image title to state flower name
        plt.show() #show image
    except FileNotFoundError:
        print("Image not found.") #handle filenotfound exception

# pylint: disable=W0613
# formatter must accept two arguments
def millions(x, pos):
    """ format value and tick position """
    return '{:1.1f} M'.format(x*1e-6) #format y axis values

def display_top_five():
    """ find and display the top five populations """
    keys = [] # array for keys used in bar graph
    values = [] # array for values used in bar graph
    #sort states_dict in descending order by population using lambda formula with range of five
    sorted_states = sorted(states_dict.items(), key = lambda x : x[1][2], reverse = True)[:5]
    print() #print a carriage return
    #print the top five most populated states and sort values
    for i in sorted_states:
        print(f'{i[0]}: {i[1][2]:,}')
        keys.append(i[0]) #append to keys array
        values.append(i[1][2]) #append to values array
    print("\nClose window to continue.")
    # format the graph
    ax = plt.subplot(111) # declare subplot variable
    ax.bar(keys, values, width=0.5, color='midnightblue') #set to bar graph
    ax.yaxis.set_major_formatter(millions) #call millions function to format y axis text
    plt.suptitle('Top Five Most Populated States') #set the graph title
    plt.xlabel('States') #label the x axis
    plt.ylabel('Population (Millions)') #label the y axis
    plt.show() #show the window

def update_population():
    """ update population for a state """
    while True:
        try:
            #prompt user to enter state
            state = input("\nPlease enter the name of the state: ")
            state = state.title() #format user input to match dictionary
            if state not in states_dict:
                print("\nState not found.") #print if state not found in dicitonary
            else:
                #print current state and population info
                print(f'\nThe current population of {state} is {states_dict[state][2]:,}.')
                break #exit loop
        except ValueError:
            print("\nInvalid entry.") #handle valueerror exception
    while True:
        try:
            #prompt user to enter new state population
            population = int(input("\nPlease enter new population: "))
            if population < 0: #check for positive number
                print("\nInvalid entry.") #display message if not
            else:
                y = list(states_dict[state]) #assign values tuple to list
                y[2] = population #assign new value to population
                states_dict[state] = y #reassign values back to dictionary
                break #exit loop
        except ValueError:
            print("\nInvalid entry.") #handle valuerror exception
    #display new state population to user
    print(f'\nThe new population of {state} is {states_dict[state][2]:,}.')

def menu():
    """ display user menu and prompt for selection """
    print("\nMenu: ")

    while True:
        print("\n1. Display data for all 50 U.S. states." \
              "\n2. Search for state and display data." \
              "\n3. Create a bar graph showing top five populated states." \
              "\n4. Update population for a specific state." \
              "\n5. Exit program.")
        try:
            selection = int(input("\nPlease make a selection: "))
            if selection == 1:
                display_all_info() #call function to show all data
            elif selection == 2:
                display_state() #call function to display data for one state
            elif selection == 3:
                display_top_five() #call function to display population graph
            elif selection == 4:
                update_population() #call function to change population for a state
            elif selection == 5:
                break #exit program
            else:
                print("\nNot a valid selection.") #handle invalid input
        except ValueError:
            print("\nNot a valid selection.") #handle valueerror exception

    print("\nThank you for using the program! Have a nice day.") #bye!

print("Welcome to the Python State Capital and Flower Application!")
menu()
