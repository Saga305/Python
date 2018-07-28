import time as tm
import pytz
import datetime as dt

istZone = 'Asia/Kolkata'
estZone = 'US/Eastern'
ausZone = 'Australia/Sydney'
fmt = '%Y-%m-%d %H:%M:%S %Z'

def getTimeStamp(timeZone):
	tz = pytz.timezone('Asia/Kolkata')
	ist_t = tm.localtime()

	ist_dt = dt.datetime(ist_t.tm_year,ist_t.tm_mon,ist_t.tm_mday,ist_t.tm_hour,ist_t.tm_min,ist_t.tm_sec, tzinfo=tz)

	if timeZone != 'Asia/Kolkata':
		dest_tz = pytz.timezone(timeZone)
		dest_dt = ist_dt.astimezone(dest_tz)
		return dest_dt.strftime(fmt)
	else:
		return ist_dt.strftime(fmt)

