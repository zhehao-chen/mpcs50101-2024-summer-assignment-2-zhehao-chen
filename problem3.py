
def number_and_letters(user_input): 
    number = 0
    letter = 0
    i = 0
    #compare the value of number and letters
    while (i < len(user_input)):
        if ("a" <= user_input[i]  <= "z"):
            letter += 1
        elif ("A" <= user_input[i]  <= "Z"):
            letter += 1
        elif ("0" <= user_input[i]  <= "9"):
            number += 1
        i += 1 
    if (letter == 0 or number == 0):
        return False
    else:
        return True

def special_characters(user_input): 
    count = 0
    i = 0
    speical = set("!@#$%")
    #compare the value to see if special characters exist
    while (i < len(user_input)):
        if user_input[i] in speical:
            count += 1
        i += 1
    if count == 0:
        return False
    else:
        return True

def capital_and_lower(user_input):
    capital = 0
    lower = 0
    i = 0
    #compare the value to see if both lower and capital exist
    while (i < len(user_input)):
        if ("a" <= user_input[i] <= "z"):
            lower += 1
        elif ("A" <= user_input[i] <= "Z"):
            capital += 1
        i += 1
    if (capital == 0 or lower == 0):
        return False
    else:
        return True



user_input = input("Enter a password: ")

if (len(user_input) >= 12 and number_and_letters(user_input) == True and special_characters(user_input) == True and capital_and_lower(user_input) == True):
    print("This is a strong password :)")
else:
    print("This is not a strong password :(")