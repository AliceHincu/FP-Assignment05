"""
    UI class.

    Calls between program modules
    ui -> service -> entity
    ui -> entity

"""

from services.service import ListComplexNr, FilterEndPoint, FilterStartPoint, start_tests
from domain.entity import Complex, RealPartException, ImagPartException
import random
from termcolor import colored


class UI:
    def __init__(self):
        self._commands = {'+': self.add_number_ui}
        self._list = ListComplexNr()

    @property
    def complex_list(self):
        return self._list

    def add_number_ui(self):
        real = input("Insert real unit: ")
        imaginary = input("Insert imaginary unit: ")
        try:
            number = Complex(real, imaginary)
            self._list.add_number(number)
        except RealPartException or ImagPartException as val_error:
            print(val_error)

    def show_ui(self):
        comp_list = self._list.get_all()
        for number in comp_list:
            print(number)

    def filter_ui(self):
        start = input("Insert start point: ")
        end = input("Insert end point: ")

        try:
            self._list.filterr(start, end)
        except FilterStartPoint or FilterEndPoint as val_error:
            print(val_error)

    def undo_ui(self):
        self._list.undo()

    def random_number(self):
        for i in range(10):
            real = random.randint(-20, 20)
            imaginary = random.randint(-20, 20)
            number = Complex(real, imaginary)
            self._list.add_random_number(number)
        self._list.add_to_history()

    @staticmethod
    def print_menu():
        """
        Print out the menu
        """
        print("\nMenu:")
        print("\t" + colored('+', 'red') + " for adding a complex number")
        print("\t" + colored('s', 'red') + " for showing the list of all complex numbers")
        print("\t" + colored('f', 'red') + " for filtering the list")
        print("\t\t-the new list will contain only the numbers between indices `start` and `end`")
        print("\t" + colored('u', 'red') + " to undo the last operation")
        print("\t" + colored('x', 'red') + " to close the calculator")

    def start(self):
        done = True
        self.print_menu()
        self.random_number()
        start_tests()
        while done:
            _command = input("\n>Command: ").strip().lower()
            if _command == "+":
                self.add_number_ui()
            elif _command == "s":
                self.show_ui()
            elif _command == "f":
                self.filter_ui()
            elif _command == "u":
                self.undo_ui()
            elif _command == "x":
                print("Goodbye!")
                done = False
            else:
                print("Bad command!")


if __name__ == '__main__':
    ui = UI()
    ui.start()
