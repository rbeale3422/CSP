class Menu():

    def __init__(self, opt_list):
        self.menu_options = opt_list
        self.num_options = len(self.menu_options)
        self.selection = 0
        
    def print_menu(self):
        print()
        print('Press the appropriate menu number below:')
        for opts in self.menu_options:
            print(f'{self.menu_options.index(opts) + 1}: {opts}')
        print()

    def get_selection(self):
        while True:
            try:
                choice = int(input())
            except ValueError:
                print('Not a number, please try again')
                self.print_menu()
                continue
            if choice < 1 or choice > len(self.menu_options):
                print('Not a valid selection')
                self.print_menu()
                continue
            else:
                self.selection = choice