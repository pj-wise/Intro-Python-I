"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html
Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

user_input = sys.argv
default_month = datetime.now().month
default_year = datetime.now().year


def cal_prog(month=default_month, year=default_year):
  # print("year", year, "month", month)
    print(calendar.month(year, month))
  

if len(sys.argv) == 1:
    cal_prog()
elif len(sys.argv) == 2:
    if len(sys.argv[1]) <=2:
        cal_prog(int(sys.argv[1]))
    else:
        print(f'Initialize file with format: <filename> <month as a number> <full year>')
else:
    if len(sys.argv[1]) <=2 and len(sys.argv[2]) == 4:
        cal_prog(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print(f'Initialize file with format: <filename> <month as a number> <full year>')