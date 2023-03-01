from logger import logger
from order_factory import OrderFactory as orfact

class Franchise:
    def __init__(self, location_number) -> None:
        self. location_number = location_number

    def place_order(self):
        user_input = input('Order options:\n\t1) Pizza\n\t2) Pasta\n\t3) Salad\nWhat would you like to order: ')
        order = orfact.create_order(user_input)
        logger.log_transaction(order,self.location_number)