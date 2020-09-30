# Basic Decryption Program
# Version 1.0
# Created by Han
# Finished on 14/4/2020


# import ast and textwrap module
import ast
import textwrap


# function to introduce the program
def intro():
    print("Basic Decryption Program\nVersion 1.0\n")


# function to decrypt the encrypted key
def decryption():

    created_file = open("experiment.txt", "r")
    encryption_dic = created_file.read()
    dictionary = ast.literal_eval(encryption_dic)

    password = input("Please enter your encrypted password:")

    # split the encrypted password into a list with each three letter:
    # example: 'aaabbb' --> ['aaa','bbb']
    password_list = textwrap.wrap(password, 3)

    decrypted = ""

    # reverse lookup in the encryption_dic
    for i in range(len(password_list)):
        for key, value in dictionary.items():
            if password_list[i] == value:
                decrypted += key

    print(decrypted)

    created_file.close()


intro()
decryption()
