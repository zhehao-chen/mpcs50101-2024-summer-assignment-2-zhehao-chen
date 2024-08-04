while True: 
    #keep ask if no break
    try:
        user_input = input("Enter a temperature in Fahrenheit: ")
        int_input = int(user_input)
        if int_input <= 0:
            print ("Please enter a positive, whole number numeric temperature.")
            break 
        #end of asking
        else:
            celsius = (int_input - 32) * 5 / 9
            formatted_celsius = f"{celsius:.2f}" 
            #this is a string
            print("The temperature is %s in Celsius."%(formatted_celsius))

    except ValueError: 
        #if user input is not a interger, then interger convert will lead to a ValueError
        print ("Please enter a positive, whole number numeric temperature.")
        break 
    #end of asking
