import os

def get_lists():
    passwords_list = open("passwords2.txt", "r").readlines()
    user_list = open("users2.txt", "r").readlines()
    if not (len(passwords_list) == len(user_list)):
        print("lengths not == error")
    return (user_list, passwords_list)

def iterate_lists(tuple_lists):
    for i in range(0, len(tuple_lists[0])):
        adduser(tuple_lists[0][i], tuple_lists[1][i])

def adduser(username, password):
    try:
        useranme = str(username)
        passwords = str(password)
        useradd_str = "net user " + str(username).strip() + " " + str(password).strip() + " /add"
        os.system(useradd_str)
        print("added: " + str(username).strip())
    except Exception as e:
        print(str(e))


#main
iterate_lists(get_lists())
