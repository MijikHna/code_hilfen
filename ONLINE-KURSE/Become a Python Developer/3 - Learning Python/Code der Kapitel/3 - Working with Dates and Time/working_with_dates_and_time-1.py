#Klassen aus datetime importieren
from datetime import date
from datetime import time
from datetime import datetime


# 1 - The date, time, and datetime classes

today = date.today()
print("Today's datei is ", today)

print("Date components: ", today.day, today.month, today.year)

#Wochentag beginnt mit 0 für Montag
print("Todays weekday # is: ", today.weekday())
days=["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
print("Which is a: ", days[today.weekday()])

today = datetime.now()
print("The current date and time is: ", today)

#nur Zeit ausgegeben
t=datetime.time(datetime.now())
print(t)


# 2 - Formatting time output
#### Date Formatting ####

now = datetime.now()

# %y/%Y - Year
# %a/%A - weekday 
# %b/%B - month 
# %d - day of month
print(now.strftime("The current year is: %Y"))
print(now.strftime("%a, %d %B, %y"))

# %c - locale's date and time
# %x - locale's date
# %X - locale's time
#<- hängt von den Einstellungen der Maschine
print(now.strftime("Local date and time %c"))
print(now.strftime("Local date and time %x"))
print(now.strftime("Local date and time %X"))



  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour
  # %M - minute, %S - second
  # %p - locale's AM/PM
print(now.strftime("Current time: %I:%M:%S %p"))
print(now.strftime("24-hour time: %H:%M"))


# 3 - Using timedelta objects
from datetime import timedelta

# construct a basic timedelta and print it
#Timedelta von einem Jahr 5 Stunden und 1 Minute produzieren
print(timedelta(days=365, hours=5, minutes=1)) 

# print today's date
now = datetime.now()
print("today is: " + str(now))

# print today's date one year from now
print("one year from now: " + str( now + timedelta(days=365) ))

# create a timedelta that uses more than one argument
print ("In 2 days and 3 weeks it will be", ( now + timedelta(days=2, weeks=3) ))

# calculate the date 1 week ago, formatted as a string
t = datetime.now()-timedelta(weeks=1)
s = t.strftime("%A %B %d %Y")
print("One week ago it was: "+s)

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)

if ( afd < today ):
    print("April Fool's day already went by %d days ago " % ((today-afd).day) )
    afd=afd.replace(year=today.year+1)

time_to_afd = afd-today
print("It's just ", time_to_afd.days, "days until April Fool's Day")

# 4 - Working with calendars

# import the calendar module
import calendar

# create a plain text calendar
#c ist Kalendar-Var, beginn der Woche ist Sonntag
c = calendar.TextCalendar(calendar.SUNDAY)
#c in String formatieren <- bestimmten Monat formatieren Hier 1=Januar, 2017=Jahr 2017
st = c.formatmonth(2017, 1, 0, 0)
print(st)

c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2017, 1, 0, 0)
print(st)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2017, 1)
print(st)



# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2017, 8):
    print(i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team meetings will be on:")
for m in range(1,13):
    cal = calendar.monthcalendar(2018, m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %d" % (calendar.month_name[m], meetday) )