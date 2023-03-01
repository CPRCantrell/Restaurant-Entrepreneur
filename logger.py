class Logger:
    def __init__(self) -> None:
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transaction(self, order, store_number):
        self.transaction_count += 1
        self.daily_sales += order.price

        file = open('log.txt', 'a')
        file.write(f'TRAN #{self.transaction_count}: \n\tOrdered: {order.dish_name}\n\tFrom: {store_number}\n\tPrice: ${order.price}\t\t\tToday\'s total: ${self.daily_sales}\n')
        file.close()

logger = Logger()