#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# welcome page
print('Welcome to Campusia Live Online!') 

try:
    login = open(r'.\userdata.txt', 'r')
    usr = login.readlines()
    print('Welcome back,', usr[0].strip(), '!')
    inp = input('please enter your password:')
except IOError:
    login = open(r'.\userdata.txt', 'x')# create a new file
    inp = input('Hello, freshman! Please enter your ID to sign up:')
    login.write(inp)
    login.write('\n')
    print('So your ID is', inp, '!\n')
    pss = input('Please enter your password and remember it:')
    login.write(pss)
finally:
    if login:
        login.close()

print('Here is the end of DEMO.')
