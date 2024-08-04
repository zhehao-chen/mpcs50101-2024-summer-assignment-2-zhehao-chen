user_input = input("Enter a word or phrase: ")

words = user_input.split()

i = 0
sentence = ""

#remove the space
while i < len(words):
    sentence += words[i]
    i += 1


i = 0
j = int(len(sentence)) - 1

#while loop to check if it is a palindrome
while i < len(sentence):
    if (sentence[i].lower() != sentence[j].lower()):
        print("This is not a palindrome.")
        break
    #break if there is a difference
    else:
        i += 1
        j -= 1

if i > j:
    print("This is a palindrome.")

