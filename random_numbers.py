#Name:         Roger Silva Santos Aguiar
#Function:     This class generates and returns an array or random numbers
#Initial date: June 21, 2020
#Last update:  July 8, 2020

import random

class RandomNumbers:
    def generate_integer_list(self):
        quantity = int(input("Enter the quantity of numbers you want to generate: "))
        min = int(input("Enter the initial number: "))
        max = int(input("Enter the last number: "))

        integer_list = RandomNumbers.generateRandomNumbers(self, quantity, min, max)
        integer_list.sort()
        return integer_list

    def generateRandomNumbers(self, quantity, min, max):
        count = 0
        random_numbers = []

        while count < quantity:
            random_numbers.append(random.randint(min, max))
            count = count + 1

        return random_numbers