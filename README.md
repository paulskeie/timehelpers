# timehelpers

Date and time is handled well by core python.  This module offers a DateSequence class that creates a sequence of dates for you.

The DateSequence class is initialized with a start and end date string like so:

from timehelpers import DateSequence

ds=DateSequence('20180210','20180331')

The initialization takes an optional keyword argument datestr_format='%Y%m%d' 
where '%Y%m%d' is the default.

For convenience the class has an iterator so you can do: for d in ds: do something
After the initialization the instance has a list of dates stored in the dateseq attribute.
