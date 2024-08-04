try:
    user_input = input(" Enter a score:")
    int_input = int(user_input)
    if int_input < 0 or int_input > 100: 
        #using if, elif, else in this way can exclude the input being evaluated once
        print("That is not valid input.")
    elif int_input < 60:
        print("You received an F!")
    elif int_input < 70:
        print("You received an D!")
    elif int_input < 80:
        print("You received an C!")
    elif int_input < 90:
        print("You received an B!")
    else:
        print("You received an A!")

except ValueError: 
    #if user input is not a interger, then interger convert will lead to a ValueError
    print("That is not valid input.")
