from franchise import Franchise as fran

class Simulation:
    def __init__(self) -> None:
        self.fran_one = fran(1)
        self.fran_two = fran(2)
        self.fran_three = fran(3)

    def run_simulation(self):
        fran.__clear_screen__()
        self.fran_one.place_order()
        self.fran_one.place_order()
        self.fran_three.place_order()
        self.fran_two.place_order()
        self.fran_one.place_order()
        self.fran_two.place_order()