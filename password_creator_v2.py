import string, random

#Password creator

#Letters, digits and special characters for the password
letters = list(string.ascii_letters)
numbers = list(string.digits)
special = list(string.punctuation)

#Election of the number of letters, digits and special characters
print("Write the number of letters: ")
ll = int(input())

print("Write the number of digits: ")
ld = int(input())

print("Write the number of special characters: ")
ls = int(input())

length = ll + ld + ls

password = ""

#Random password generation with randInt 
while True:
    election = random.randint(0, 2)
    if election == 0 and ll > 0:
        rand = random.randint(0, 51)
        password = password + letters[rand]
        ll = ll - 1

    elif election == 1 and ld > 0:
        rand = random.randint(0,9)
        password = password + numbers[rand]
        ld = ld - 1

    elif election == 2 and ls > 0:
        rand = random.randint(0,31)
        password = password + special[rand]
        ls = ls - 1

    if ll == 0 and ld == 0 and ls == 0:
        break

print("The final password with " + str(length) + " characters long is: " + password)
        

    
