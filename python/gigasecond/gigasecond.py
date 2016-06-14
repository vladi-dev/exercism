import datetime
import calendar

add_gigasecond = lambda d:datetime.datetime.utcfromtimestamp(calendar.timegm(d.utctimetuple()) + 10**9)