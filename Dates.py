"""
    Dates - the 'datetime' library extension
    ========================================
    Utilities to facilitate date and time handling This is accomplished with a new Date object that inherit all of
    datetime methods and give you new methods.

    Usage
    -----
    Import the Dates.py file into your project and use the Dates object.

    Authors & Contributors
    ----------------------
        * Massimo Guidi <maxg1972@gmail.com>,

    License
    -------
    This module is free software, released under the terms of the Python
    Software Foundation License version 2, which can be found here:

        http://www.python.org/psf/license/

"""

__author__ = 'Massimo Guidi'
__author_email__ = "maxg1972@gmail.com"
__version__ = '1.1'

import datetime, locale
from datetime import timedelta

class Dates(datetime.datetime):
    def format(self,date_type,time_type=None):
        """
        Transform datetime to string format using the given type

        @param date_type: date format (DMY > dd/mm/yyyy, YMD > yyyy/mm/dd, MDY > mm/dd/yyyy, ISO > yyyy-mm-dd)
        @param time_type: time format (HMS > hh:mm:ss, HM > hh:mm, hms > hh:mm:ss am/pm, hm > hh:mm am/pm)
        @return: datetime in string format
        """

        #date conversion
        if date_type == 'DMY':
            result = self.strftime("%d/%m/%Y")
        elif date_type == 'YMD':
            result = self.strftime("%Y/%m/%d")
        elif date_type == 'MDY':
            result = self.strftime("%m/%d/%Y")
        elif date_type == 'ISO':
            result = self.strftime("%Y-%m-%d")
        else:
            result = ""

        #time conversion
        if time_type:
            if len(result) > 0:
                result += " "
            #formato 24h
            if time_type == 'HMS':
                result += self.strftime("%H:%M:%S")
            elif time_type == 'HM':
                result += self.strftime("%H:%M")
            #formato 12h
            elif time_type == 'hms':
                result += self.strftime("%I:%M:%S %p")
            elif time_type == 'mh':
                result += self.strftime("%I:%M %p")

        #return formatted string
        return result

    def format_date(self,date_type):
        """
        Transform date to string format using the given type

        @param date_type: date format (DMY > dd/mm/yyyy, YMD > yyyy/mm/dd, MDY > mm/dd/yyyy, ISO > yyyy-mm-dd)
        @return: date in string format
        """
        return self.format(date_type)

    def format_time(self,time_type):
        """
        Transform time to string format using the given type

        @param time_type: time format (HMS > hh:mm:ss, HM > hh:mm, hms > hh:mm:ss am/pm, hm > hh:mm am/pm)
        @return: time in string format
        """

        return self.format('',time_type)

    def convert(self,string_data,date_type=None,time_type=None):
        """
        Transform string (date and time) in datetime object using the given type

        @param string_data: datetime in string format
        @param date_type: date format (DMY > dd/mm/yyyy, YMD > yyyy/mm/dd, MDY > mm/dd/yyyy, ISO > yyyy-mm-dd)
        @param time_type: time format (HMS > hh:mm:ss, HM > hh:mm, hms > hh:mm:ss am/pm, hm > hh:mm am/pm)
        @return: datetime object
        """

        #date
        if date_type == 'DMY':
            string_format = "%d/%m/%Y"
        elif date_type == 'YMD':
            string_format = "%Y/%m/%d"
        elif date_type == 'MDY':
            string_format = "%m/%d/%Y"
        elif date_type == 'ISO':
            string_format = "%Y-%m-%d"
        else:
            string_format = ""

        #time
        if time_type:
            if len(string_format) > 0:
                string_format += " "
            #24h format
            if time_type == 'HMS':
                string_format += "%H:%M:%S"
            elif time_type == 'HM':
                string_format += "%H:%M"
            elif time_type == 'hms':
                string_format += "%I:%M:%S %p"
            elif time_type == 'mh':
                string_format += "%I:%M %p"

        #convert string in datetime object
        try:
            result = self.strptime(string_data, string_format)
        except ValueError:
            raise ValueError("Invalid data format!")

        #return datetime object
        return result

    def convert_date(self,string_data,date_type):
        """
        Transform string (date only) in datetime object using the given type

        @param string_data: date in string format
        @param date_type: date format (DMY > dd/mm/yyyy, YMD > yyyy/mm/dd, MDY > mm/dd/yyyy, ISO > yyyy-mm-dd)
        @return: datetime object
        """
        return self.convert(string_data,date_type)

    def convert_time(self,string_data,time_type):
        """
        Transform string (time only) in datetime object using the given type

        @param string_data: time in string format
        @param time_type: time format (HMS > hh:mm:ss, HM > hh:mm, hms > hh:mm:ss am/pm, hm > hh:mm am/pm)
        @return: datetime object
        """
        return self.convert(string_data,time_type=time_type)

    def month_name(self,short=True,locate=''):
        """
        Give back month name in given language (if omitted will be use system language)

        @param short: True for short name (default), False for full name
        @param locate: localization identifier (see system's strings, ex: it_IT, en_US, ru_RU, ecc.)
        @return: month name string
        """
        #save current localization
        current = locale.getlocale()

        #set given localization
        locale.setlocale(locale.LC_ALL,locate)

        #get month name
        if short:
            name = self.strftime('%b')
        else:
            name = self.strftime('%B')

        #reset original localization
        locale.setlocale(locale.LC_ALL,current)

        #return month name
        return name

    def weekday_name(self,short=True,locate=''):
        """
        Give back weekday name in given language (if omitted will be use system language)

        @param short: True for short name (default), False for full name
        @param locate: localization identifier (see system's strings, ex: it_IT, en_US, ru_RU, ecc.)
        @return: weekday name string
        """
        #save current localization
        current = locale.getlocale()

        #set given localization
        locale.setlocale(locale.LC_ALL,locate)

        #get weekday name
        if short:
            name = self.strftime('%a')
        else:
            name = self.strftime('%A')

        #reset original localization
        locale.setlocale(locale.LC_ALL,current)

        #return month name
        return name

    def add_days(self,days_number):
        """
        Add/subtract days to/from current datetime object

        :param days_number: Days to add/subtract
        :return: datetime object
        """
        date = self +  + timedelta(days=days_number)
        return  self.replace(day=date.day,month=date.month, year=date.year)

    def add_months(self,months_number):
        """
        Add/subtract months to/from current datetime object

        :param months_number: Months to add/subtract
        :return: datetime object
        """
        month = (self.month + months_number) % 12
        year = self.year + (self.month + months_number - 1) // 12
        if not month:
            month = 12

        day = min(self.day, [31,29 if year%4==0 and not year%400==0 else 28,31,30,31,30,31,31,30,31,30,31][month-1])
        return  self.replace(day=day,month=month, year=year)

    def add_years(self,years_number):
        """
        Add/subtract years to/from current datetime object

        :param years_number: Years to add/subtract
        :return: datetime object
        """
        return self.add_months(years_number * 12)