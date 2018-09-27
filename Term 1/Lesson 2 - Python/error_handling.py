while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError:
        print("Not a valid number!")
    finally:
        print("\nAttempted Input")

#you can also handle all errors like this
try:
    #some code
except Exception as e:
    #some code
    print("Exception occured: {}".format(e))
#handles all built-in exceptions
