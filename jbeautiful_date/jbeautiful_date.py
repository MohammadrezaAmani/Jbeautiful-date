from jdatetime import date, datetime


class JBeautifulDate(date):
    """Date object that can be extended to datetime by using Python indexing/slicing:

    Examples:
        >>> (Dey / 17 / 1380)[:]
        datetime.datetime(1380, 10, 17, 0, 0)

        >>> (Dey / 17 / 1380)[23]
        datetime.datetime(1380, 10, 17, 23, 0)

        >>> (Dey / 17 / 1380)[23:14]
        datetime.datetime(1380, 10, 17, 23, 14)

        >>> (Dey / 17 / 1380)[23:14:10]
        datetime.datetime(1380, 10, 17, 23, 14, 10)
    """

    def __getitem__(self, t):
        """
        Converts date to datetime with provided time [hours[:minutes[:seconds]]]
        :return: datetime object.
        """

        if isinstance(t, slice):
            h, m, s = t.start or 0, t.stop or 0, t.step or 0
        elif isinstance(t, int):
            h, m, s = t, 0, 0
        else:
            raise TypeError("Time values must be integer or slice, not {!r}".format(t.__class__.__name__))

        return datetime(self.year, self.month, self.day, hour=h, minute=m, second=s)

    def to_date(self):
        """
        Converts JBeautifulDate to a simple Python date
        :return: date object
        """
        return date(self.year, self.month, self.day)

    def __add__(self, timedelta):
        return datetime.fromgregorian(date=self.to_date() + timedelta)

    __radd__ = __add__
# Classes to build date
#   D @ 16/10/1995 (16/Oct/1995)
#   D @ 5/19/2006 (May/19/2006)

class _PartialDate:
    """Date builder that uses operator "/" or "-" between values of day, month and year

    Examples:
        >>> D @ 17/10/1380
        JBeautifulDate(1380, 10, 17)

        >>> D @ 17-10-1380
        JBeautifulDate(1380, 10, 17)
    """

    def __init__(self, first, _format):
        self._date_values = [first]
        self._format = _format

    def __truediv__(self, value):
        self._date_values.append(value)
        if len(self._date_values) == 3:
            return JBeautifulDate(**dict(zip(self._format, self._date_values)))
        else:
            return self

    __sub__ = __truediv__


class BaseDateFormat:
    """Base class for date format.

    Used to create PartialDate with a format specified in the inherited classes.

    Examples:
        >>> D @ 11
        _PartialDate(11)

        >>> D @ 22/10
        _PartialDate(22/10)
    """

    # List of strings 'day', 'month', and 'year' in desired order.
    # Should be overridden in the inherited classes
    _format = None

    def __matmul__(self, first):
        return _PartialDate(first, self._format)

    def __repr__(self):
        return '{}{}'.format(self.__class__.__name__, self._format)

    @staticmethod
    def today():
        today = date.today()
        return JBeautifulDate(year=today.year, month=today.month, day=today.day)

    @staticmethod
    def now(tz=None):
        return datetime.now(tz=tz)


class DMY(BaseDateFormat):
    _format = 'day', 'month', 'year'


class MDY(BaseDateFormat):
    _format = 'month', 'day', 'year'


class YMD(BaseDateFormat):
    _format = 'year', 'month', 'day'


class YDM(BaseDateFormat):
    _format = 'year', 'day', 'month'


D = DMY()


# Classes to build date with month name
#   16/Oct/1995
#   May-19-2006

class _Day:
    """Second step of creating date object

    Stores month and day numbers. If applied operator '/' or '-', returns JBeautifulDate with provided value of the year

    Examples:
        >>> 12/Khr/1382
        JBeautifulDate(1382, 3, 12)

        >>> Dey-17-1380
        JBeautifulDate(1380, 10, 17)

    """

    def __init__(self, d, m):
        self.d = d
        self.m = m

    def __sub__(self, y):
        return JBeautifulDate(year=y, month=self.m, day=self.d)

    __truediv__ = __sub__


class _Month:
    """First step of creating date object

    Stores month number. If applied operator '/' or '-', returns _Day with provided value of the day.

    Examples:
        >>> 16/Oct
        _Day(16, 10)

        >>> May-19
        _Day(19, 5)
    """

    def __init__(self, m):
        self.m = m

    def __sub__(self, d):
        return _Day(d, self.m)

    __rtruediv__ = __rsub__ = __truediv__ = __sub__


M = _, Far, Ord, Khr, Tir, Mor, Sha, Mehr, Aban, Azar, Dey, Bah, Esf = [_Month(i) for i in range(13)]
