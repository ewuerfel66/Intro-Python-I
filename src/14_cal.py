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

# Get vars from the command line if there are any
try:
  month = sys.argv[1]
  year = sys.argv[2][1:-1]
except IndexError:
  try:
    month = sys.argv[1]
    year = datetime.now().year
  except IndexError:
    month = datetime.now().month
    year = datetime.now().year
except ValueError:
  print("Program expects input in the form of: `14_cal.py month [year]`")
  sys.exit(0)

# Convert to integers if not already
if not isinstance(month, int):
  month = int(month)

if not isinstance(year, int):
  year = int(year)

cal = calendar.TextCalendar().formatmonth(year, month)
print(cal)

sys.exit(0)