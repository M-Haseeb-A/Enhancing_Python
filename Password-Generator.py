# this program will generate a random password for you

import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_characters = "!@#$%^&*._"

password = letters + numbers + special_characters

length = int(input("Enter the length of password you want :"))

newpassword = ""

for i in range(length):
    newpassword += random.choice(password)

print(f"your generated password is {newpassword} ")
