"""
    Entity class should be coded here
"""
# ---- classes for exceptions ----


class RealPartException(Exception):
    def __init__(self, msg):
        self._msg = msg


class ImagPartException(Exception):
    def __init__(self, msg):
        self._msg = msg


# ---- class for the complex number ----


class Complex:
    # common to all numbers

    def __init__(self, real_part, imaginary_part):
        # These don't change -> read-only attributes
        try:
            _r_part = float(real_part)
        except ValueError:
            raise RealPartException('The real part is not a number')

        try:
            _i_part = float(imaginary_part)
        except ValueError:
            raise ImagPartException("The imaginary part is not a number")

        if _i_part >= 0:
            sign = "+"
        else:
            sign = "-"
            imaginary_part = -int(imaginary_part)

        self._r = int(real_part)
        self._sign = sign
        self._i = imaginary_part

    def __str__(self):
        number = f"{self._r}{self._sign}{self._i}i"
        return number

    def __repr__(self):
        number = f"{self._r}{self._sign}{self._i}i"
        return number

    def __eq__(self, other):
        if isinstance(other, Complex):
            return self._i == other._i and self._r == other._r
        return False

    @property
    def real_part(self):
        return self._r

    @property
    def imaginary_part(self):
        return self._i
