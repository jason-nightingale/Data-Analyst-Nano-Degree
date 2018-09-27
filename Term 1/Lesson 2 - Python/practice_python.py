##lists - are mutable
name = ['Jason', 'Noemi', 'Chase', 'Jason', 'Chase', 'Tom']
name.append('Tom')
print(name)

## create SETS from Lists
unique_name = set(name) ##this gives a deduped set of a list
print(len(name))
print(max(name))
print(min(name))

names = "\n".join(['billy', 'like', 'mary'])
print(names)

##tuples
tuple_a = 12, 24, 36
##declaring multiple variables
length, width, height = 24, 45, 60
fname, mname, lname = "billy", "joe", "bob"
##using the format with parenthesis
print("dimensions are {}x{}x{}".format(tuple_a[0], tuple_a[1], tuple_a[2]))
print("dimensions are {}x{}x{}".format(length, width, height))
print("his name was {} {} {}".format(fname, mname, lname))

##dictionary - KEYS are NOT mutable
population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}
print("USA" in population) ##returns False
print("Shanghai" in population) ##returns True
print(population["Shanghai"]) ##returns 17.8
print(population.get("Istanbul")) ##returns 13.3
print(population.get("USA")) ##returns None
population["USA"] = 34.5 ##adds USA key and a value of 34.5 to population dictionary
n = population.get("Russia")
print(n is None) ## returns True
print(n is not None) ##returns False
print(population["Russia"]) ##KeyError occurs, use .get() for no errors
print(population.get("Russia", "There isn\'t such and element.")) ## it prints the last quotes instead of None

##Lists equality vs. identity
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == b) ## True
print(a is b) ## True
print(a == b) ## True
print(a is c) ## False - they don't identify with each other

## another dictionary
animals = {'dogs': [20, 10, 15, 8, 32, 15],
 'cats': [3,4,2,8,2,4],
 'rabbits': [2, 3, 3],
 'fish': [0.3, 0.5, 0.8, 0.3, 1]}

animals['dogs'] ## [20, 10, 15, 8, 32, 15]
animals['dogs'][3] ## 8
animals[3] ## KeyError

## Nested dictionary
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'HE'}}
helium = elements["helium"]
print(helium) ##prints the nested helium dictionary
print(elements["hydrogen"]["weight"]) ##prints hydrogen dictionary key 'weight' 1.00794
##creating a variable for nested dictionary Key
hydrogen_weight = elements["hydrogen"]["weight"]
print(hydrogen_weight)

## adding entries to nested dictionaries
elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True

## if statements
phone_balance = 8
bank_balance = 100
if phone_balance < 5:
	phone_balance += 10
	bank_balance -= 10
## else and elif
if season == "spring":
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('is their other seasons??')

##persons age
age = 15
##age limits for the bus
free_up_to_age = 4
child_up_to_age = 18
senior_up_to_age = 65
#determines bus ticket
concession_ticket = 1.25
adult_ticket = 2.50
ticket_price = 0.00

#logic for bus ticket prices
if age <= free_up_to_age:
    ticket_price = 0.00
elif age > free_up_to_age and age <= child_up_to_age:
    ticket_price = concession_ticket
elif age > child_up_to_age and age <= senior_up_to_age:
    ticket_price = concession_ticket
else:
    ticket = adult_ticket

message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)

#another practice of if...else statements
points = 174  # use this input to make your submission
prizes = ['wooden rabbit', 'no prize', 'wafer-thin mint', 'penguin']
result = "Congratulations! You won a {}!"

# write your if statement here
if points <= 50:
    the_prize = prizes[0]
elif points > 50 and points <= 150:
    the_prize = prizes[1]
elif points > 150 and points <= 180:
    the_prize = prizes[2]
elif points > 180 and points <= 200:
    the_prize = prizes[3]
else:
    the_prize = 'Oh dear, no prize this time.'

print(result.format(the_prize))

# you can set a variable to '' or 0 and the condition will always be False
is_true = ''
if is_true: # don't ever say if is_true == True
    print('True')
else:
    print('False') #this will print


# For loops
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
#iterate through lists
for city in cities:
    print(city.title()) #.title() capitalizes first letter of each word
print('Done!')

#for loop with range
for i in range(5):
    print(i+=1)

#for loop with start, stop, step
for i in range(2,6):
    print(i) # prints 2 3 4 5 on separate lines

for i in range(2, 30, 2):
    print(i) #prints 2 to 28 in two's

#you can modify lists in for loops
for index in range(len(cities)):
    cities[index] = cities[index].title()
    print(cities[index])

#iterating through dictionaries
#KEYS
cast = {"Jerry Sienfeld": "Jerry Seinfeld",
        "Julia Louis-Dreyfus": "Julia Louis-Dreyfus",
        "Jason Alexander": "Jason Alexander"
        }
for key in cast:
    print(key) # remember that key is justr a variable, it could be booger if you want

# to interate through keys and values
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))



#####################################
#checking if dictionary item is in list and count the items
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for key, value in basket_items.items():
    if key in fruits:
        result += value

print(result)
#####################################

#while loops - unknown interations until a condition is met
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

while sum(hand) <= 17:
    #pop means to pull out if the list from the end
    #if we don't pop it out it will be an endless loop
    #in this case we are appending it to hand[]
    hand.append(card_deck.pop())

print(hand)
print(card_deck)

#working with square in while loops
limit = 40
num = 0

while (num+1)**2 < limit:
    num += 1
nearest_square = num**2
print(nearest_square)

###################################
#using break and continue
# this loops through a list and builds a ticker
#up to and not exceeding 140 characters
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
headline_count = 0
# write your loop here
for headline in headlines:
    headline_count += len(headline)

    if headline_count >= 140:
        news_ticker += headline[:140 - len(news_ticker)]

        break
    else:
        news_ticker += headline + " "
        headline_count += 1

print(news_ticker)
#################################

#zip and enumerate
#below is how yuo can create a zip list
my_zip_list = list(zip(['a', 'b', 'c'], [1, 2, 3]))
print(my_zip_list)
# prints this - [('a', 1), ('b', 2), ('c', 3)]

#you can also unpack tuples, create a list
#and spit it out in a single for loop
letters = ['a', 'b', 'c', 'd']
nums = [1, 2, 3, 4]

for letter, num in zip(letters, nums):
    print("{}: {}: ".format(letter, num))

# you can also unzip a list with the *
some_list = [('a', 1), ('b', 2), ('c', 3 )]
letter, nums = zip(*some_list)
print("{}: {}".format(letters, nums))
#prints - ['a', 'b', 'c', 'd']: (1, 2, 3)

#enumerate is a built in function that
#provides indices of a tuple
letters = ['a', 'b', 'c', 'd', 'e', 'f']
for i, letter in enumerate(letters):
    print(i, letter)

#or set it to a variable for later
my_enum = enumerate(letters)
#but you can print just the variable
#you can run it through a for loop
#similar to above
for i, letter in ny_enum:
    print(i, letter)

#using zip write a for loop that combines
# the tuples into a list and formatted
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for label, x, y, z in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(label, x, y, z))

for point in points:
    print(point)


# List Comprehensions
#creating lists quickly and concisely
#instead of using a normal For loop, you can reduce it
capitalized_cities = [city.title() for city in cities]

#conditions inside of lisst Comprehensions
squares = [x**2 for x in range(9) if x % 2 == 0]
# if using an else, pu it in front the loops
squares = [x**2 if x % 2 == 0 else x +3 for x in range(9)]


#quiz
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith"]
#write list of only first names
first_names = [name.split()[0].lower() for name in names]
print first_names

#print only the first 20 multiples of 3
multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)

#create a passed list if scores are at least 65
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
