from dateutil.relativedelta import relativedelta, weekdays
from jdatetime import date, datetime
from datetime import timedelta as _timedelta, date as _date, datetime as _datetime
from .jbeautiful_date import JBeautifulDate


class RelativeDelta(relativedelta):
    """Same as relativedelta, but returns JBeautifulDate in the result.

    Examples:
        >>> 17/Dey/1380 + 5*days
        JBeautifulDate(1380, 10, 22)
    """

    def __add__(self, d):
        if isinstance(d, JBeautifulDate):
            d = datetime.togregorian(d)
        print(d, type(d))
        new_date = super().__add__(d)
        if isinstance(new_date, date) and not isinstance(new_date, datetime):
            new_date = datetime.fromgregorian(date=new_date)
            return JBeautifulDate(new_date.year, new_date.month, new_date.day)
        else:
            return new_date

    __radd__ = __add__


class BeautifulTimedelta:
    """Creates timedelta with specified time unit using operator '*'

    Examples:
        >>> 3*years
        RelativeDelta(years=+3)

        >>> -5*weeks
        RelativeDelta(days=-35)
    """

    def __init__(self, name):
        self.name = name

    def __rmul__(self, n):
        return RelativeDelta(**{self.name: n})


_ = BeautifulTimedelta

years = _('years')
months = _('months')
weeks = _('weeks')
days = _('days')
hours = _('hours')
minutes = _('minutes')
seconds = _('seconds')
microseconds = _('microseconds')
leapdays = _('leapdays')
leapday = 1 * leapdays

year = _('year')
month = _('month')
day = _('day')
hour = _('hour')
minute = _('minute')
second = _('second')
microsecond = _('microsecond')

yearday = _('yearday')
nlyearday = _('nlyearday')

_weekday = _('weekday')


class BeautifulWeekday:
    """

    Examples:
        Get next Monday:
        >>> d = 29/Mar/2018  # Thursday
        >>> d + MO  # Equivalent to MO(1)
        JBeautifulDate(2018, 4, 2)

        Get second to next Monday:
        >>> d = 29/Mar/2018
        >>> d + MO(2)
        JBeautifulDate(2018, 4, 9)

        Get last Saturday:
        >>> d = 29/Mar/2018
        >>> d - SA
        JBeautifulDate(2018, 3, 24)

        Get second to last Saturday:
        >>> d = 29/Mar/2018
        >>> d - SA(2)
        JBeautifulDate(2018, 3, 17)

        Get second to last Saturday (same as previous):
        >>> d = 29/Mar/2018
        >>> d + SA(-2)
        JBeautifulDate(2018, 3, 17)
    """

    def __init__(self, wd, n=1):
        self.wd = wd
        self.n = n

    def __radd__(self, other):
        return other + self.wd(self.n) * _weekday

    def __rsub__(self, other):
        return other + self.wd(-self.n) * _weekday

    def __call__(self, n):
        return BeautifulWeekday(self.wd, n)


weekdays = DO, SE, CH, PA, JO, SH, YE = [BeautifulWeekday(weekdays[i]) for i in range(7)]
