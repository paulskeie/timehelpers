from datetime import datetime,timedelta

class DateSequence(object):
	"""
		The DateSequence class is initialized with a start and end date string like so:
		ds=DateSequence('20180210','20180331')
		The initialization takes an optional keyword argument datestr_format='%Y%m%d' 
		where '%Y%m%d' is the default.
		For convenience the class has an iterator so you can do: for d in ds: do something
		After the initialization the instance has a list of dates stored in the dateseq attribute.
	"""
	def __init__(self,datestr_start,datestr_stop,datestr_format="%Y%m%d"):
		self.datestr_start=datestr_start
		self.datestr_stop=datestr_stop
		self.datestr_format=datestr_format
		dtstart=datetime.strptime(datestr_start,datestr_format)
		dtstop=datetime.strptime(datestr_stop,datestr_format)
		td=timedelta(days=1)
		dato=dtstart
		dates=[]
		while dato <= dtstop:
			dates.append(dato)
			dato=dato+td
		self.dateseq=dates
	def __iter__(self):
		return iter(self.dateseq)

class TimeIterator(object):
	"""
		Initialize with a datetime instance and a timedelta instance
		ti=TimeIterator(datetimestart,timedeltastep)
		nextdatetime=ti.next()
		or
		nextdatetime=ti()
	"""
	def __init__(self,datetimestart,timedeltastep):
		self.datetimestart=datetimestart
		self.timedeltastep=timedeltastep
		self.nextdatetime=datetimestart
	def next(self):
		x=self.nextdatetime
		self.nextdatetime=x+self.timedeltastep
		return x
	def __call__(self):
		return self.next()
	def __repr__(self):
		return u"nextdatetime: %s, timedeltastep: %s" % (self.nextdatetime,self.timedeltastep)


