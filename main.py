#Password encoder and decoder
#each instance of x=1 is a place holder

#encoder
def encode(password):
    #Jason Schott's function, adds 3 to each digit
    x=1

#decoder
def decode(password):
    #Lance's function, Subtracts 3 from each digit
    x=1

#menu
def printmenu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")

#gets choice
def getchoice():
    while True:
        try:
            choice = int(input("Please enter an option:"))
            break
        except:
            print("Choice must be a number between 1 and 3")
    return choice

#main
def main():
    #runs print menu then either calls encode or decode, or quits
    while True:
        printmenu()
        choice = getchoice()
        if choice == 1:
            password = input("Please enter the password to encode: ")
            password = encode(password)
        if choice == 2:
            decode(password)
        if choice == 3:
            break
        else:
            print("Choice must be a number between 1 and 3")

        
            

if __name__ == "__main__":
    main()