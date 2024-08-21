import string, random

#Password creator

letters = list(string.ascii_letters)
numbers = list(string.digits)
special = list(string.punctuation)

print("Write the length of the password: ")
length = int(input())
password = ""

for i in range(length):
    election = random.randint(0, 2)
    if election == 0:
        rand = random.randint(0, 51)
        password = password + letters[rand]

    elif election == 1:
        rand = random.randint(0,9)
        password = password + numbers[rand]

    elif election == 2:
        rand = random.randint(0,31)
        password = password + special[rand]

print("The final password with " + str(length) + " characters long is: " + password)
        

    
