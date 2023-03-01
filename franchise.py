import os
import sys
from logger import logger
from order_factory import OrderFactory as orfact

class Franchise:
    def __init__(self, location_number) -> None:
        self. location_number = location_number

    def place_order(self):
        user_input = self.__collect_valid_input__()
        order = orfact.create_order(user_input)
        logger.log_transaction(order,self.location_number)
        Franchise.__clear_screen__()

    def __collect_valid_input__(self):
        options = ['pizza','pasta','salad']

        print(f'Your ordering options (store: {self.location_number}):')
        for option in range(len(options)):
            print(f'{option + 1}) {options[option].title()}')

        while True:
            user_input = input('Which option would you like: ').lower()
            Franchise.__clear_line__()

            if user_input in options:
                return user_input

            try:
                user_input = int(user_input)
                return options[user_input-1]
            except: pass

            print('INVALID ENTRY: enter name or number : ',end='')

    def __clear_screen__():
        # for windows
        if os.name == 'nt':
            os.system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            os.system('clear')

    def __clear_line__(lines = 1):
        for line in range(lines):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")