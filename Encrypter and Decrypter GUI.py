# Encryption and Decrpytion Tool GUI
# Version 1.0
# Created by Han
# Finished on 23/4/2020


import tkinter as tk
import random
import ast
import textwrap

def encrypted(entry):

    created_file = open("key.txt", "r")
    encryption_dic = created_file.read()
    dictionary = ast.literal_eval(encryption_dic)
    encrypted = ""

    for characters in entry:
        encrypted += dictionary[characters]

    password2_label['text'] = encrypted

    created_file.close()

def decrypted(entry):

    created_file = open("key.txt", "r")
    encryption_dic = created_file.read()
    dictionary = ast.literal_eval(encryption_dic)


    # split the encrypted password into a list with each three letter:
    # example: 'aaabbb' --> ['aaa','bbb']
    password_list = textwrap.wrap(entry, 3)

    decrypted = ""

    # reverse lookup in the encryption_dic
    for i in range(len(password_list)):
        for key, value in dictionary.items():
            if password_list[i] == value:
                decrypted += key

    password2_label['text'] = decrypted


# Graphical Code Starts
root =tk.Tk()
root.title("Encrypter and Decrypter Tool Version 1.0")

# code to set initial size of tkinter window
canvas = tk.Canvas(root, height = 650, width = 900)
canvas.pack()

frame = tk.Frame(root, bg = '#2E4053')
frame.place(relheight = 1, relwidth =1)

name_label = tk.Label(root, bg='#2E4053', fg = '#7D87A6', text ='Version 1.0, created by Han, 22/4/2020', font = 'Consolas 9')
name_label.place(relx = 0.7, rely = 0.972)

# code for upper section of the app starts

title_frame = tk.Frame(root, bg = 'blue')
title_frame.place(anchor = 'n', relx = 0.478 , rely = 0.09, relheight = 0.1, relwidth = 0.815)

label2 = tk.Label(title_frame, text = 'Encrypter and Decrypter Tool', font = 'Consolas 35', bg = '#2E4053', fg = 'white', anchor = 'w' )
label2.place(relheight = 1, relwidth = 1)

subtext2_frame = tk.Frame(root, bg = 'blue')
subtext2_frame.place(anchor ='n', relx = 0.45, rely = 0.19, relheight = '0.05', relwidth = '0.75')

label3 = tk.Label(subtext2_frame, text = 'Version 1.0',
                  font = 'Consolas 12', bg ='#2E4053', fg ='white', anchor = 'w')
label3.place(relheight = 1, relwidth = 1)
# code for upper section of the app ends

result_frame = tk.Frame(root, bg = '#212F3D')
result_frame.place(anchor = 'n', relx =0.5, rely = 0.29, relheight = 0.12, relwidth = 0.85)

entry = tk.Entry(result_frame, bg = '#212F3D', fg='white',  font = 'Consolas 25', relief = 'flat')
entry.place(anchor ='n',relx = 0.5, rely = 0.005, relheight = 0.9, relwidth = 1)

green_stripe = tk.Label(result_frame, bg = '#45B39D',)
green_stripe.place(anchor = 'n', relx = 0.5, rely = 0.9, relheight = 0.1, relwidth = 1.1)

result2_frame = tk.Frame(root, bg = '#212F3D')
result2_frame.place(anchor = 'n', relx =0.5, rely = 0.642, relheight = 0.12, relwidth = 0.85)

password2_label = tk.Label(result2_frame, bg = '#212F3D', fg='white',  font = 'Consolas 25', relief = 'flat', anchor='w')
password2_label.place(anchor = 'n', relx = 0.5, rely = 0.005, relheight = 0.9, relwidth = 1)

green2_stripe = tk.Label(result2_frame, bg = '#85C1E9',)
green2_stripe.place(anchor = 'n', relx = 0.5, rely = 0.9, relheight = 0.1, relwidth = 1.1)

result3_frame = tk.Frame(root, bg = '#2E4053')
result3_frame.place(anchor = 'n', relx =0.5, rely = 0.82, relheight = 0.12, relwidth = 0.85)

password3_label = tk.Label(result3_frame, text= 'Note: This program is made for demonstration purposes only.\n'
                                                'Encryption made by this program are not up to date to '
                                                'current encrytion standards.\nUsers be advised.'
                           , bg = '#2E4053', fg='#7D87A6',  font = 'Consolas 10', relief = 'flat', justify = 'left')
password3_label.place(anchor = 'n', relx = 0.375, rely = 0.1, relheight = 0.85, relwidth = 1.1)

line = tk.Label(result3_frame, bg='grey')
line.place(relx =0.5, rely = 0.12, relwidth = 1, relheight = 0.001, anchor ='n')


# code for the button in the app
button = tk.Button(root, text= 'Encrypt',font='Consolas 20', relief = 'flat', bg ='#45B39D', fg = '#FDFEFE',
                   command=lambda: encrypted(entry.get()))
button.place(relx = 0.075, rely = 0.48, relheight = 0.09, relwidth = 0.18)

d_button = tk.Button(root, text= 'Decrypt',font='Consolas 20', relief = 'flat', bg ='#85C1E9', fg = '#FDFEFE',
                   command=lambda: decrypted(entry.get()))
d_button.place(relx = 0.745, rely = 0.48, relheight = 0.09, relwidth = 0.18)

root.mainloop()
# Graphical Code ends
