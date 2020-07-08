# Name:         Roger Silva Santos Aguiar
# Function:     This is the menu file, all other files will be executed from here
# Initial date: June 20, 2020
# Last update:  July 8, 2020

import random_numbers
import linear_search_algorithm

class Menu:
    def __init__(self, integer_numbers = []):
        self.integer_numbers = integer_numbers

    def options(self):
        print("\n************************************************************Menu************************************************************")
        print("1 - Generate Random numbers")
        print("2 - Display numbers")
        print("3 - Run linear search algorithm")
        print("4 - Exit")
        print("****************************************************************************************************************************")

    def runOption(self, option):
        if option == 1:
            print("Generate random numbers.\n")
            self.integer_numbers = random_numbers.RandomNumbers.generate_integer_list(self)
        elif option == 2:
            print("Display numbers.")
            print("\nInteger array: {}" .format(self.integer_numbers))
        elif option == 3:
            print("Run linear search algorithm.")
            searched_number = int(input("\nEnter the number you want to search in the list: "))
            result = linear_search_algorithm.LinearSearch.linear_search(self, self.integer_numbers, searched_number)
            print(result)

if __name__ == '__main__':
    menu = Menu()
    menu.options()
    option = int(input("Choose an option: "))
    print("****************************************************************************************************************************")

    while option != 4:
        menu.runOption(option)
        menu.options()
        option = int(input("Choose an option: "))
        print("****************************************************************************************************************************")



