from Dates import Dates

#creazione oggetto data
c = Dates.now()
d = Dates(2011,1,3)

#Print date in default mode
print "date object: %s" % (d)

#Convert date to string
print "date ISO format and time HHMM 24h: %s" % (c.format('ISO',"HM"))
print "date ISO format: %s" % (c.format_date('ISO'))
print "time HHMM 24h format: %s" % (c.format_time('HM'))
print "date DMY format and time HHMM 12h: %s" % (c.format('DMY',"hms"))
print "date DMY format and time HHMM 24h: %s" % (c.format('DMY',"HMS"))

#Convert string to date and print
print "date ISO format: %s" % (d.convert_date('2011-01-03','ISO').format_date('ISO'))
#Convert string to date, assign to a variable, then print it
e = d.convert('2013-12-31 03:43:01 PM','ISO',"hms")
print "date MDY format and time HHMMSS 24h: %s" % (e.format('MDY',"HMS"))

#short and full month name in current language
print "short month name (system lang): %s" % (c.month_name())
print "full month name (system lang): %s" % (c.month_name(short=False))

#short and full dqy name in current language
print "short month name (english): %s" % (e.weekday_name(short=True,locate='en_US'))
print "full month name (russian): %s" % (e.weekday_name(short=False,locate='ru_RU.UTF8'))
print "full month name (chinese): %s" % (e.weekday_name(short=False,locate='zh_CN.utf8'))

#adding days
print "10 days after today: %s" % (c.add_days(10).format_date("DMY"))
print "5 days before today: %s" % (c.add_days(-5).format_date("DMY"))

#adding months
print "2 months afetr today: %s" % (c.add_months(2).format_date("DMY"))
print "1 month before today: %s" % (c.add_months(-1).format_date("DMY"))

#adding years
x = Dates(2012,2,29)
print "2 years after %s: %s" % (x.format_date("DMY"),x.add_years(2).format_date("DMY"))
print "2 years before %s: %s" % (x.format_date("DMY"),x.add_years(-2).format_date("DMY"))
