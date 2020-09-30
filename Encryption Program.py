# Encryption Program
# Version 1.0
# Created by Han
# Finished on 13/4/2020
# Note: Cross-referenced encrypter.py created by Hum due to incompetence of creator
# Every single line of this program has been examined and experimented

# import random, string and ast modules
import random
import string
import ast


# function to introduce the program
def intro():
    print("Basic Encryption Program\nVersion 1.0\n")


# function to gain user input of details
def user_input():
    global file_creation

    file_creation = input("Do you want to create a new dictionary or use a previous one?\n>>>")


def encryption():

    encrypted = ""
    encryption_dic = {}
    key = []
    characters = string.ascii_letters + string.digits + string.punctuation

    if file_creation == "New" or file_creation == "new" or file_creation == "n":
        created_file = open("experiment.txt", "w+")
        created_file.truncate(0)

        # Creates a random combination containing three letters or numbers or symbols and enters
        # it into the encryption_dic
        for character in characters:
            random_key = ''.join(random.choice(characters) + random.choice(characters) + random.choice(characters))
            # adds the created combinations into the dictionary
            if random_key not in key:
                key += random_key
            encryption_dic.setdefault(character, random_key)

        # Writes the created dictionary into the experiment.txt file
        created_file.write(str(encryption_dic))

        password = input("Please enter your password:")

        # forms the encrypted password by cross-referencing the encryption_dic
        for characters in password:
            encrypted += encryption_dic[characters]

        print(encrypted)
        created_file.close()

    elif file_creation == "Previous" or file_creation == "previous" or file_creation == "p":

        created_file = open("experiment.txt", "r")
        encryption_dic = created_file.read()
        dictionary = ast.literal_eval(encryption_dic)

        password = input("Please enter your password:")

        for character in password:
            encrypted += dictionary[character]

        print(encrypted)

        created_file.close()

    else:
        print("Invalid input.")
        user_input()
        encryption()


intro()
user_input()
encryption()














