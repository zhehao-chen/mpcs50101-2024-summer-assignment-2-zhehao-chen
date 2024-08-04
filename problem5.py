try:
    user_input = input("Enter a number: ")

    i = 0
    sum = 0
    int_input = int(user_input)

    #while loop to get the sum
    while i < len(user_input):
        if (i % 2 == 0):
            sum += int(user_input[i])
        else:
            sum -= int(user_input[i])
        i += 1
    
    if (sum % 11 == 0):
        print("This is divisible by 11.")
    else:
        print("This is not divisible by 11. ")
 
except ValueError:
    print("Integer only")
    

