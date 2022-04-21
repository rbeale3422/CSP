"""
'B' column only containing numbers between 1 and 15 inclusive,
the 'I' column containing only 16 through 30, 'N' containing 31
through 45, 'G' containing 46 through 60, and 'O' containing 61
through 75.
"""

import random as rand
from cli_menu import Menu

class BingoCaller():
    def __init__(self):
        self.used_numbers = []
        self.valid_numbers = [x + 1 for x in range(75)]
    
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


class BingoCardMaker():

    def __init__(self):
        self.b_list = [x+1 for x in range(15)]
        self.i_list = [x+1 for x in range(15,30)]
        self.n_list = [x+1 for x in range(30,45)]
        self. g_list = [x+1 for x in range(45,60)]
        self.o_list = [x+1 for x in range(60,75)]
        self.card = self.__setup_card()

    def display_card(self):
        for row in self.card:
            for element in row:
                print(element, end='\t')
            print()

    def __setup_card(self):
        # init and set all values to 0
        temp_card = [[0 for y in range(6)] for x in range(5)]
        # set first item in each column to the letters "BINGO"
        for row in range(5):
            for column in range(6):
                if row == 0:
                    if column == 0:
                        temp_card[row][column] = 'B'
                    else:
                        temp_card[row][column] = rand.choice(self.b_list)
                        # take out of appropriate list so not used again
                        self.b_list.remove(temp_card[row][column])
                if row == 1:
                    if column == 0:
                        temp_card[row][column] = 'I'
                    else:
                        temp_card[row][column] = rand.choice(self.i_list)
                        # take out of appropriate list so not used again
                        self.i_list.remove(temp_card[row][column])
                if row == 2:
                    if column == 0:
                        temp_card[row][column] = 'N'
                    elif column == 3: # every Bingo card has a free spot in middle
                        temp_card[row][column] = '*'
                    else:
                        temp_card[row][column] = rand.choice(self.n_list)
                        # take out of appropriate list so not used again
                        self.n_list.remove(temp_card[row][column])
                if row == 3:
                    if column == 0:
                        temp_card[row][column] = 'G'
                    else:
                        temp_card[row][column] = rand.choice(self.g_list)
                        # take out of appropriate list so not used again
                        self.g_list.remove(temp_card[row][column])
                if row == 4:
                    if column == 0:
                        temp_card[row][column] = 'O'
                    else:
                        temp_card[row][column] = rand.choice(self.o_list)
                        # take out of appropriate list so not used again
                        self.o_list.remove(temp_card[row][column])
        return temp_card


def main():
    
    # Ask user how many players and create the appropriate
    # number of bingo cards and store them in a list
    my_caller = BingoCaller()
    user_choice = ['Get Number', 'Quit']
    my_menu = Menu(user_choice)

    while True:
        try:
            num_players = int(input('Please enter the number of players (1 to 6): '))
        except ValueError:
            print('Not a number, please try again')
            continue
        if num_players < 1:
            print('You must have at least one player')
            continue
        elif num_players > 6:
            print('You cannot have more than six players')
            continue
        else:
            # validated answer
            break

    players = []
    for x in range(num_players):
        my_card = BingoCardMaker()
        players.append(my_card)

    for card in players:
        print(f'Bingo card for player {players.index(card)+1}')
        card.display_card()
        print()

    # To-Do: Create a loop that gets a number from the caller or quits the game
    while True:
        my_menu.print_menu()
        my_menu.get_selection()
        choice = my_menu.selection
        if choice == 1:
            print(my_caller.get_number())
            continue
        if choice == 2:
            break


if __name__ == '__main__':
    main()
            