fvalue=0
fsuit=""
vtrans={"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
        "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11,
        "Queen": 12, "King": 13}
# split and find the suit then send it over to find the value
def get_suit(card):
    csplit=card.split(" of ")
    cvalue=csplit[0].title()
    csuit=csplit[1]
    return get_value(cvalue, csuit)
# change srting into number
def get_value(gvalue, gsuit):
    global vtrans
    global fvalue
    global fsuit

    for key, value in vtrans.items():
        if key == gvalue:
            fvalue = value

    fsuit=gsuit
    return
# combine the value in string form and suit back together again
def cat_them_back(c, s):
    for key, value in vtrans.items():
        if int(c) == value:
            cat_val = "{} of {}".format(key, s)
            break
    cat_val = cat_val + ", "
    return(cat_val)

inp_cards = input("Enter your cards here (ace of hearts, ten of clubs, etc.): ")
zip_value = []
zip_suit = []
#first we need to split the inputed cards
cards=inp_cards.split(", ")

#run loop to go through all cards, pass through functions and append into arrays
for card in cards:
    suit=get_suit(card)
    #print(str(fvalue) + " and " + fsuit)
    zip_value.append(fvalue)
    zip_suit.append(fsuit)
# zip the arrays into a sorted by card number zipped list
my_card_list = sorted(list(zip(zip_value, zip_suit)))

#print out the sorted cards
uval, usuit = zip(*my_card_list)
x=0
for uv in uval:
    final=cat_them_back(uv,usuit[x])
    x += 1

    print(final)
