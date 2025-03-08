# S.A.Nethini Pabodhya Perera 
# Final Coursework

import random

class colors: # Class to import colors and fonts to the program
    RED = '\033[31m'
    RESET = '\033[0m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    GREEN = "\033[0;32m"
    CYAN = "\033[0;36m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"


def add_driver(details): # Function to add driver details to the database
    name = input("Enter driver's name: ")
    try:
       age = int(input("Enter driver's age: "))
    except ValueError:
       print(colors.RED + "Integer required" + colors.RESET)
       age = int(input("Enter driver's age: "))
    team = input("Enter driver's team: ")
    car = input("Enter driver's car: ")
    try:
         points = int(input("Enter the driver's points: "))
    except ValueError:
         print(colors.RED +"Integer required"+ colors.RESET)
         points = int(input("Enter the driver's points: "))
    #Using Dictionaries as the database to store driver's details
    details[name] = {'Age': age, 'Team': team, 'Car': car, 'Points': points}
    print(colors.YELLOW + "Driver details added successfully!" + colors.RESET)



def delete_driver(details): # Function to delete a driver and driver's detail from the databse
    name = input("Enter the name of the driver to delete: ")
    if name in details:
        del details[name]
        print(colors.YELLOW + "Driver details deleted successfully!" + colors.RESET )
    else: # If the Driver is not on the database
        print(colors.RED + "Driver not found!" + colors.RESET)

def update_driver(details): # Function to update details of a driver
    name = input("Enter the name of the driver to update: ")
    if name in details:
        try:
             age = int(input("Enter driver's new age: "))
        except ValueError:
             print(colors.RED +"Integer required"+ colors.RESET)
             age = int(input("Enter driver's new age: "))
        team = input("Enter driver's new team: ")
        car = input("Enter driver's new car: ")
        details[name]['Age'] = age
        details[name]['Team'] = team
        details[name]['Car'] = car
        print(colors.YELLOW + "Driver details updated successfully!" + colors.RESET)
    else: # If the Driver is not on the database
        print(colors.RED + "Driver not found!" + colors.RESET)

def simulate_race(details): # Function to simulate a Race between the drivers in the database
    race_date = input("Enter the date of the race (YYYY-MM-DD): ")
    race_location = input("Enter the location of the race: ")
    race_results = []

    for name, driver in details.items():
        # Randomly assigning a position to each player
        position = random.randint(1, len(details))
        points = 0
        if position == 1:
            points = 10
        elif position == 2:
            points = 7
        elif position == 3:
            points = 5

        race_results.append((name, position, points))
        details[name]['Points'] += points
    # Sort the drivers ny their positions
    race_results.sort(key=lambda x: x[1])

    with open('races.txt', 'a') as file: # Open the file races and append
        file.write(f"Race Date: {race_date}\n")
        file.write(f"Location: {race_location}\n")
        for result in race_results:
            file.write(f"Driver: {result[0]}, Position: {result[1]}, Points: {result[2]}\n")
        file.write("\n")

    print(colors.YELLOW + "Race simulated and results recorded!" + colors.RESET)

def display_standings(details): # Function to view the rally crossing table
    sorted_details = sorted(details.items(), key=lambda x: x[1]['Points'], reverse=True)#sorting the drivers in descending order
    print(colors.CYAN + colors.BOLD + "\n--- Championship Standings ---")
    print(colors.BLUE + colors.BLUE + "{:<15} {:<10} {:<10} {:<10} {:<10}".format("Name", "Age", "Team", "Car", "Points") +colors.RESET)
    for driver, info in sorted_details:
        print("{:<15} {:<10} {:<10} {:<10} {:<10}".format(driver, info['Age'], info['Team'], info['Car'], info['Points']))

def view_race_table(): # Funtion to view the race table sorted according to the date
    try:
        with open('races.txt', 'r') as file: # open the file races and read
            print("\n--- Race Table ---")
            print(file.read())
    except FileNotFoundError:# If the file not found
        print(colors.RED + "No race data found." + colors.RESET)

def save_data(details): # Function to save the data to a file
    with open('drivers.txt', 'w') as file:# open the file drivers and write
        for name, info in details.items():
            file.write(f"{name},{info['Age']},{info['Team']},{info['Car']},{info['Points']}\n")
    print(colors.YELLOW + "Data saved successfully!" + colors.RESET)

def load_data(details): # Function to load the data from saved file
    try:
        with open('drivers.txt', 'r') as file: # open the file drivers and read
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    name, age, team, car, points = line.split(',')
                    details[name] = {'Age': age, 'Team': team, 'Car': car, 'Points': int(points)}
                    print(colors.YELLOW + "Data has been loaded from the file" + colors.RESET)
    except FileNotFoundError:# If the file is not found
        print(colors.RED + "No previous data found." + colors.RESET)

# Main Menu
driver_details = {}

print(colors.CYAN + colors.ITALIC + colors.BOLD + "\n--- Rally Cross Management System ---" + colors.RESET)
print(colors.BLUE + "\nType ADD for adding driver details")
print(colors.BLUE +"Type " + colors.GREEN + "DDD" +colors.BLUE + " for deleting driver")
print(colors.BLUE +"Type " + colors.GREEN + "UDD" +colors.BLUE + " for updating driver details" )
print(colors.BLUE +"Type " + colors.GREEN + "VCT" +colors.BLUE + " for viewing the rally cross standings table")
print(colors.BLUE +"Type " + colors.GREEN + "SRR" +colors.BLUE + " for simulating a random race")
print(colors.BLUE +"Type " + colors.GREEN + "VRL" +colors.BLUE + " for viewing race table sorted according to the date")
print(colors.BLUE +"Type " + colors.GREEN + "STF" +colors.BLUE + " to save the current data to a text file")
print(colors.BLUE +"Type " + colors.GREEN + "RFF" +colors.BLUE + " to load data from the saved text file")
print(colors.BLUE +"Type " + colors.GREEN + "ESC" +colors.BLUE + " to exit the program" + colors.RESET)


while True: # Looping the program until manually breaks

    choice = input("\nEnter your choice: ")

    if choice == 'ADD':
        add_driver(driver_details)
    elif choice == 'DDD':
        delete_driver(driver_details)
    elif choice == 'UDD':
        update_driver(driver_details)
    elif choice == 'VCT':
        display_standings(driver_details)
    elif choice == 'SRR':
        simulate_race(driver_details)
    elif choice == 'VRL':
        view_race_table()
    elif choice == 'STF':
        save_data(driver_details)
    elif choice == 'RFF':
        load_data(driver_details)
    elif choice == 'ESC': # Manually exiting the program
        save_data(driver_details)
        print(colors.YELLOW + "Exiting the program.....")
        break
    else: # Invalid input was entered
        print(colors.RED + colors.BOLD + "Invalid choice. Please try again." + colors.RESET)


