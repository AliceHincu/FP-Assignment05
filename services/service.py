"""
    Service class includes functionalities for implementing program features
"""

from copy import deepcopy
from domain.entity import Complex, RealPartException, ImagPartException

# ---- classes for exceptions ----


class FilterStartPoint(Exception):
    def __init__(self, msg):
        self._msg = msg


class FilterEndPoint(Exception):
    def __init__(self, msg):
        self._msg = msg


# ---- class for the list of complex numbers ----


class ListComplexNr:
    """
    List's functionalities
    """

    def __init__(self):
        '''
        It contains the list of all complex numbers and the history list
        '''
        self._numbers = []
        self._history = []

    def count(self):
        """
        Count the numbers
        @return: the number of numbers (type: int)
        """
        return len(self._numbers)

    def __len__(self):
        '''
        :return: the length of the list of all complex numbers (type: int)
        '''
        return self.count()

    def __str__(self):
        '''
        Readable content for ui
        :return: the list of complex numbers (type: <class 'str'>)
        '''
        return str(self._numbers)

    def __eq__(self, other):
        '''
        For comparisons
        :param other: the other element we are comparing to
        :return: if they are equal or not (type: bool)
        '''
        if isinstance(other, ListComplexNr):
            return self._numbers == other._numbers
        return False

    def add_number(self, nr):
        """
        Add a complex number to the list of all complex numbers and then saves the list to the history list
        @param nr: the number (type: class)
        @return: -

        Raises from entity.py 3 errors:
        -RealPartException if:
            - the real part of the complex number isn't a valid number
        -SignException if:
            - the sign isn't a valid symbol (+ or -)
        -ImagPartException if:
            - the imaginary part of the complex number isn't a valid number
        """
        self._numbers.append(nr)
        copy = deepcopy(self._numbers)
        self._history.append(copy)

    def add_to_history(self):
        copy = deepcopy(self._numbers)
        self._history.append(copy)

    def add_random_number(self, nr):
        """
        Add the complex number to the list of all complex numbers and doesn't save the list to the history list
        @param nr: the number (type: class)
        @return: -
        """
        self._numbers.append(nr)

    def get_all(self):
        '''
        :return: the list of complex numbers to display (type: list)
        '''
        return self._numbers

    def filterr(self, start, end):
        '''
        Filter the list so that it contains only the numbers between indices start and end
        :param start: the start of the new list (type: int)
        :param end: the end of the new list (type: int)

        Raises 2types of errors:
        -FilterStartPoint if the start point:
            - isn't a number
            - is lower than 0
            - is higher than the end point
            - is higher than the number of elements
        -FilterEndPoint if the end point:
            - isn't a number
            - is higher than the number of elements

        '''
        try:
            start = int(start)
            if start < 0:
                raise FilterStartPoint("start point should start from 0")
            if start > int(len(self._numbers)):
                raise FilterStartPoint("start point should be lower than the length of the list")
        except ValueError:
            raise FilterStartPoint("start point isn't a number")

        try:
            end = int(end)
            if end >= int(len(self._numbers)):
                raise FilterEndPoint("end point should be lower than the length of the list")
            if start > end:
                raise FilterStartPoint("start point should be lower than the end point")
            self._numbers = [number for index, number in enumerate(self._numbers) if start <= index <= end]
            copy = deepcopy(self._numbers)
            self._history.append(copy)
        except ValueError:
            raise FilterEndPoint("end point isn't a number")

    def undo(self):
        '''
        Undo the last change
        '''
        length = len(self._history)
        if length == 1:
            print("No more undo!")
        else:
            self._history.pop(length-1)
            copy_list = deepcopy(self._history[length-2])
            self._numbers = copy_list.copy()


def test_counting():
    '''
    Test if len function works properly
    '''
    n1 = Complex('3', '7')

    l = ListComplexNr()
    assert len(l) == 0
    l.add_number(n1)
    assert len(l) == 1


def test_display():
    '''
    Test display function
    '''
    numbers = ListComplexNr()
    n1 = Complex('3', '7')
    n2 = Complex('6', '-2')
    n3 = Complex('4', '5')
    n4 = Complex('4', '9')

    numbers.add_number(n1)
    numbers.add_number(n2)
    numbers.add_number(n3)
    numbers.add_number(n4)

    # display_list = numbers.get_all()
    # expected_list = ['3+7i', '6-2i', '4+5i', '4+9i']
    # print(display_list)
    # wprint(expected_list)
    # assert display_list == expected_list


def test_add():
    '''
    Test add function
    :return:
    '''
    l = ListComplexNr()
    n1 = Complex('3', '7')
    l.add_number(n1)


def test_complex():
    '''
    Test init from entity.py -> init
    '''
    # the first is good, the others are not
    try:
        _n1 = Complex('3', '7')
        assert True
    except ValueError:
        assert False

    try:
        _n2 = Complex('gr', '-2')
        assert False
    except RealPartException:
        assert True

    try:
        _n4 = Complex('4', '-')
        assert False
    except ImagPartException:
        assert True


def test_filter():
    '''
    We test all the content from filter function
    '''

    numbers = ListComplexNr()
    n1 = Complex('3', '7')
    n2 = Complex('6', '-2')
    n3 = Complex('4', '5')
    n4 = Complex('4', '9')

    numbers.add_number(n1)
    numbers.add_number(n2)
    numbers.add_number(n3)
    numbers.add_number(n4)

    expected_list = ListComplexNr()
    expected_list.add_number(n2)
    expected_list.add_number(n3)
    expected_list.add_number(n4)
    numbers.filterr(1, 3)

    assert expected_list == numbers

    try:
        numbers.filterr('beab', 3)
        assert False
    except FilterStartPoint:
        assert True

    try:
        numbers.filterr(-3, 3)
        assert False
    except FilterStartPoint:
        assert True

    try:
        numbers.filterr(6, 3)
        assert False
    except FilterStartPoint:
        assert True

    try:
        numbers.filterr(2, 1)
        assert False
    except FilterStartPoint:
        assert True

    try:
        numbers.filterr(2, 'beab')
        assert False
    except FilterEndPoint:
        assert True

    try:
        numbers.filterr(2, 4)
        assert False
    except FilterEndPoint:
        assert True


def test_undo():
    '''
    Test the undo function
    '''
    numbers = ListComplexNr()
    n1 = Complex('3', '7')
    n2 = Complex('6', '-2')
    n3 = Complex('4', '5')
    n4 = Complex('4', '9')

    numbers.add_number(n1)
    numbers.add_number(n2)
    numbers.add_number(n3)
    numbers.add_number(n4)

    numbers.undo()

    result = ListComplexNr()
    result.add_number(n1)
    result.add_number(n2)
    result.add_number(n3)

    assert result == numbers

    numbers2 = ListComplexNr()
    numbers2.add_number(n1)
    numbers2.add_number(n2)

    numbers2.undo()

    result2 = ListComplexNr()
    result2.add_number(n1)

    assert result2 == numbers2


def start_tests():
    '''
    Start the tests
    '''
    test_counting()
    test_complex()
    test_add()
    test_display()
    test_filter()
    test_undo()
