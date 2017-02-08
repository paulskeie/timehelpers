# timehelpers

Date and time is handled well by core python.  

This module offers:

1. A DateSequence class that creates a sequence of dates for you.
2. A TimeIterator class that is initialized with starttime and timedeltastep and implements a next() method.

## DateSequence

DateSequence produces the full sequence in memory upon initialization.
TimeIterator is more lightweight and only keeps track of which is the next datetime to return.

The DateSequence class is initialized with a start and end date string like so:

from timehelpers import DateSequence

ds=DateSequence('20180210','20180331')

The initialization takes an optional keyword argument datestr_format='%Y%m%d' 
where '%Y%m%d' is the default.

For convenience the class has an iterator so you can do: for d in ds: do something
After the initialization the instance has a list of dates stored in the dateseq attribute.

## TimeIterator

Usage:

from timehelpers import TimeIterator
from datetime import datetime,timedelta

datetimestart=datetime.strptime("2018010103","%Y%m%d%H")
timedeltastep=timedelta(hours=3)

ti=TimeIterator(datetimestart,timedeltastep)

nextdatetime=ti.next()
or
nextdatetime=ti()

