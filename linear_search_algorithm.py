# Name:         Roger Silva Santos Aguiar
# Function:     This class implements the linear search algorithm
# Initial date: July 8, 2020
# Last update:  July 8, 2020

class LinearSearch:
    def linear_search(self, integer_numbers, searched_number):
        position = 0
        output = ""

        for integer in integer_numbers:
            if integer == searched_number:
                output = "The number {} was found in position {} of the list." .format(searched_number, position + 1)
                break
            position = position + 1

        if output == "":
            output = "Not found number."

        return output