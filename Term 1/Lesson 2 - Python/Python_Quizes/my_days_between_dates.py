###
### Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    global days_in_month

    #Check for days in month on if statement
    if day < days_in_month[month-1]:
        day += 1
    else:
        day = 1
        if month != 12:
            month += 1
        else:
            month = 1
            year +=1

    year_month_day = year, month, day
    return year_month_day

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    # YOUR CODE HERE!
    days_between_count = 0
    #check for leap year
    while (year1,month1,day1) < (year2,month2,day2):
        if year1 % 400 == 0:
            days_in_month[1] = 29
        elif year1 % 100 == 0:
            days_in_month[1] = 28
        elif year1 % 4 == 0:
            days_in_month[1] = 29
        else:
            days_in_month[1] = 28
        #send to nextDay function
        year1, month1, day1 = nextDay(year1,month1,day1)
        days_between_count += 1
    return days_between_count

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed", result
        else:
            print "Test case passed!"

test()
