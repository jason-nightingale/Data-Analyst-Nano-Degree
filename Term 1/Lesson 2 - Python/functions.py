# functions
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

# you can pass values in a couple different always
print(cylinder_volume(10, 5)) #passing by position
print(cylinder_volume(height=10, radius=5)) #passing by name

# write your function here ---- mine
def readable_timedelta(days_in):
    days_in_week = 7
    tot_weeks = 0
    tot_days = 0

    if days_in == days_in_week:
        tot_weeks = 1
    elif days_in > days_in_week:
        tot_weeks = int(days_in) / int(days_in_week)
        tot_days = int(days_in) - (int(tot_weeks) * int(days_in_week))
    else:
        tot_weeks = 0
        tot_days = days_in

    return("{} week(s) and {} day(s).".format(int(tot_weeks), tot_days))
# test your function
print(readable_timedelta(2221))

#theirs
def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta(10))


"""Lambda expressions are anonymous functions or short
non-reusable simple functions """
#function example
def multiply(x, y):
    return x * y

#lambda expresion
multiply = lambda x, y: x * y

#calling it
multiply(2, 3)
# returns 6
