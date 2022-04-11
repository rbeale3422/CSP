"""
'B' column only containing numbers between 1 and 15 inclusive,
the 'I' column containing only 16 through 30, 'N' containing 31
through 45, 'G' containing 46 through 60, and 'O' containing 61
through 75.
"""

import random as rand

class BingoCaller():
    def __init__(self):
        self.used_numbers = []
        self.valid_numbers = [x + 1 for x in range(76)]
    
    def is_already_used(self, number):
        if number in self.used_numbers:
            return True
        return False

    def get_number(self):
        number = rand.choice(self.valid_numbers)
        while self.is_already_used(number):
            number = rand.choice(self.valid_numbers)
        self.used_numbers.append(number) # add valid number to list so not used again
        if number >= 1 and number <= 15:
            return 'B-' + str(number)
        if number >= 16 and number <= 30:
            return 'I-' + str(number)
        if number >= 31 and number <= 45:
            return 'N-' + str(number)
        if number >= 46 and number <= 60:
            return 'G-' + str(number)
        if number >= 61 and number <= 75:
            return 'O-' + str(number)

    def show_used(self): # used for debugging, otherwise comment out
        self.used_numbers.sort()
        print(self.used_numbers)
            
def main():
    my_caller = BingoCaller()
    for x in range(75):
        print(my_caller.get_number())

    print('These numbers have already been used:')
    my_caller.show_used()

if __name__ == '__main__':
    main()
            