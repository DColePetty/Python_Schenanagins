
# Python 3
# Cole Petty 

alphabet = "zabcdefghijklmnopqrstuvwxy"
for i in range(0, len(alphabet)):
    print(str(alphabet[i]) + " " + str(i))

def affine(string, x, offset):
    print(str(string))
    alphabet = "zabcdefghijklmnopqrstuvwxy"
    for letter in string:
        if(letter == ' '):
            print( " space ")
            continue
        value = alphabet.find(letter)
        print( str(letter) + " converts to "  + str(((value * x) + offset) % 26) + " = " + str(alphabet[((value * x) + offset) % 26]))

affine("input", 13, 18)
affine("alter", 13, 8)

affine("hello world", 11, 17)

def logarithmicBases(base1, base2, value):
    for i in range(0, 100):
        print(" X " + str(base1 ** i))
        print(" " + str(value % base2))
        print(" ")
        if( ((base1**i) % base2) == value % base2):
            print("log of " + str(base1) + " to the " + str(i) + " equals " + str(value) + " mod " + str(base2))
            break

logarithmicBases(5, 7, 6)
