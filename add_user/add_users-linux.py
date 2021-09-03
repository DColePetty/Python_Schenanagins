import os
import subprocess
import sys

def get_lists():
    passwords_list = open("passwords.txt").readlines()
    user_list = open("users.txt").readlines()
    if not (len(passwords_list) == len(user_list)):
        print(str(passwords_list) + str(user_list) + "\n")
        print(str(len(passwords_list)) + "\n")
        print(str(len(user_list)) + "\n")
        raise Exception("lists_not_equal_length_error")
    return (user_list, passwords_list)

def iterate_lists(tuple_lists):
    for i in range(0, len(tuple_lists[0])):
        adduser(tuple_lists[0][i], tuple_lists[1][i])
    return 0

def create_encrypted_pass(password):
    full_str = 'echo $(printf "' + password.strip() + '" | openssl passwd -1 -stdin) > tempfile.txt'
    print(str(full_str))
    encrypted__out = os.system(full_str)

def adduser(username, password):
    try:
        username = str(username)
        password = str(password)
        create_encrypted_pass(password)
        encrypted_password = str(open('tempfile.txt').read()).strip()
        os.remove("tempfile.txt")
        print(str(encrypted_password))
        useradd_str = "useradd -m -p '" + str(encrypted_password) + "' " + str(username)
        os.system(useradd_str)
        print(str(useradd_str))
        print("Success, added user: " + str(username))
        open("userlist.txt", 'a+').write(str(username).strip() + ":" + str(password).strip() + "\n")
    except Exception as e:
        print(str(e))

#main
iterate_lists(get_lists())
