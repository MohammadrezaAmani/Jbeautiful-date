# Beautiful Date

> This project is inspired by [beautiful-date](https://github.com/kuzmoyev/beautiful-date) and is only its Persian version.


Simple and beautiful way to create date and datetime objects in Python.

**UNDER DEVELOPMENT** 


**Before**:

```python3
from jdatetime import date, datetime

d = date(year=1382, month=3, day=12)
t = datetime(year=1382, month=3, day=12, hour=23, minute=45)
```
    
**After**:

```python3
from jbeautiful_date import *

d = 12/Khr/1382
t = (12/Khr/1382)[23:45]
```

## Installation

```bash
pip install jbeautiful-date
```

## Examples

### Create Date

Using months names:

```python3
>>> from jbeautiful_date import *

>>> 2/Sha/1356  # European format
JBeautifulDate(1356, 6, 2)
>>> Sha/2/1356  # US format
JBeautifulDate(1356, 6, 2)
```
    
Using months numbers:
    
```python3
>>> 24/M[12]/1387  # European format
JBeautifulDate(1387, 12, 24)
>>> M[12]/24/1387  # US format
JBeautifulDate(1387, 12, 24)
```

Or alternatively:

```python3
>>> D @ 12/3/1382  # European format (default)
JBeautifulDate(1382, 3, 12)

>>> D = MDY()  # Add this at the top of your script to use US format. 
>>> d = D @ 3/12/1382  # US format
JBeautifulDate(1382, 3, 12)
```

Available formats (needed only if you create dates using `D@`):

```python3
class DMY(BaseDateFormat):
    _format = 'day', 'month', 'year'

class MDY(BaseDateFormat):
    _format = 'month', 'day', 'year'

class YMD(BaseDateFormat):
    _format = 'year', 'month', 'day'

class YDM(BaseDateFormat):
    _format = 'year', 'day', 'month'
``` 

You can also easily retrieve current date as a `JBeautifulDate` object and current time using:

```python3
>>> D.today()
JBeautifulDate(1399, 8, 24)

>>> D.now()
jdatetime.datetime(1399, 8, 24, 3, 58, 11, 451333)
```

### Create Datetime

Previous methods create `JBeautifulDate` objects which are inherited from `date` but can be 
easily extended to `jdatetime` using indexing/slicing:
 
```python3
>>> (Oct/16/1995)[:]
datetime.datetime(1995, 10, 16, 0, 0)

>>> (Oct/16/1995)[23]
datetime.datetime(1995, 10, 16, 23, 0)

>>> (Oct/16/1995)[23:14]
datetime.datetime(1995, 10, 16, 23, 14)

>>> (Oct/16/1995)[23:14:10]
datetime.datetime(1995, 10, 16, 23, 14, 10)
```

You can also use prefix `D @` if you need months by their numbers:    
    
```python3
>>> (D @ 16/10/1995)[:]
datetime.datetime(1995, 10, 16, 0, 0)

>>> (D @ 16/10/1995)[23]
datetime.datetime(1995, 10, 16, 23, 0)

>>> (D @ 16/10/1995)[23:14]
datetime.datetime(1995, 10, 16, 23, 14)

>>> (D @ 16/10/1995)[23:14:10]
datetime.datetime(1995, 10, 16, 23, 14, 10)
```
    
### Date/Datetime manipulations:

This library also provides simple interface for 
[relativedelta](http://dateutil.readthedocs.io/en/stable/relativedelta.html) from 
[dateutil](http://dateutil.readthedocs.io/en/stable/index.html)

#### Adding/Subtracting/Setting timedeltas:

Notice that singular time unit (year, month, ...) sets given value, plural (years, months,) adds it.


```python3
>>> d = 26/Mar/2018
>>> t = d[12:23:15]

>>> d + 2 * years
BeautifulDate(2020, 3, 26)
>>> d - 2 * days
BeautifulDate(2018, 3, 24)

>>> t + 25 * hours
datetime.datetime(2018, 3, 27, 13, 23, 15)
```
    
Available deltas: `years`, `months`, `weeks`, `days`, `hours`, `minutes`, 
`seconds`, `microseconds`, `leapdays`
(see [relativedelta](http://dateutil.readthedocs.io/en/stable/relativedelta.html)).

```python3
>>> d = 26/Mar/2018
>>> t = d[12:23:15]

>>> d + 2022 * year
BeautifulDate(2022, 3, 26)
>>> d += 2 * day
>>> d
BeautifulDate(2018, 3, 2)

>>> t + 22 * hour
datetime.datetime(2018, 3, 26, 22, 23, 15)
>>> t += 22 * hour
>>> t
datetime.datetime(2018, 3, 26, 22, 23, 15)
```

Available setters: `year`, `month`, `day`, `hour`, `minute`, `second`, `microsecond`,
`yearday` and `nlyearday`
(see [relativedelta](http://dateutil.readthedocs.io/en/stable/relativedelta.html)).

#### Weekdays:

Get next Monday:

```python3
>>> d = 29/Mar/2018  # Thursday
>>> d + MO  # Equivalent to MO(1)
BeautifulDate(2018, 4, 2)
```

Get second to next Monday:

```python3
>>> d = 29/Mar/2018
>>> d + MO(2)
BeautifulDate(2018, 4, 9)
```

Get last Saturday:

```python3
>>> d = 29/Mar/2018
>>> d - SA
BeautifulDate(2018, 3, 24)
```

Get second to last Saturday:

```python3
>>> d = 29/Mar/2018
>>> d - SA(2)
BeautifulDate(2018, 3, 17)
```

Get second to last Saturday (same as previous):

```python3
>>> d = 29/Mar/2018
>>> d + SA(-2)
BeautifulDate(2018, 3, 17)
```
    
### Util

#### drange:

You can use `drange` to generate ranges of dates:

```python3
>>> for d in drange(17/Dey/1380, 12/Khr/1382):
...     print(d)
1994-03-27
1994-03-28
1994-03-29
1994-03-30
1994-03-31
1994-04-01
1994-04-02
1994-04-03
1994-04-04

>>> for d in drange(27/Mar/1994, 5/Apr/1994, 2*days):
...     print(d)
1994-03-27
1994-03-29
1994-03-31
1994-04-02
1994-04-04
```
    
and datetimes:

```python3
>>> for dt in drange((27/Mar/1994)[10:25], (4/Apr/1994)[10:10]):
...     print(dt)
1994-03-27 10:25:00
1994-03-28 10:25:00
1994-03-29 10:25:00
1994-03-30 10:25:00
1994-03-31 10:25:00
1994-04-01 10:25:00
1994-04-02 10:25:00
1994-04-03 10:25:00

>>> for dt in drange((27/Mar/1994)[10:25], (4/Apr/1994)[10:10], 20*hours):
...     print(dt)
1994-03-27 10:25:00
1994-03-28 06:25:00
1994-03-29 02:25:00
1994-03-29 22:25:00
1994-03-30 18:25:00
1994-03-31 14:25:00
1994-04-01 10:25:00
1994-04-02 06:25:00
1994-04-03 02:25:00
1994-04-03 22:25:00
```
