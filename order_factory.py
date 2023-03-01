from order import *
class OrderFactory:

    @staticmethod
    def create_order(order):
        if order == 'pizza':
            return Pizza()
        if order == 'pasta':
            return Pasta()
        if order == 'salad':
            return Salad()