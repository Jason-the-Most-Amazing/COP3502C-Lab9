#Password encoder and decoder

#encoder
def encode(password):
    #Jason Schott's function, adds 3 to each digit
    while True:
        try:
            newpassword = ''.join(str((int(char)+3)%10) for char in password)
            break
        except:
            print("Password must consist of only numbers")
            password = input("Please enter the password to encode:")
    return newpassword
    

#decoder
def decode(newpassword):
    original_password = ''.join(str((int(char)+7)%10) for char in newpassword)
    return original_password

#menu
def printmenu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")

#gets choice
def getchoice():
    while True:
        try:
            choice = int(input("Please enter an option: "))
            break
        except:
            printmenu()
            print("Choice must be a number between 1 and 3")
    return choice


def main():
    #runs print menu then either calls encode or decode, or quits
    while True:
        printmenu()
        choice = getchoice()
        if choice == 1:
            password = input("Please enter the password to encode: ")
            newpassword = encode(password)
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            original_password = decode(newpassword)
            print(f"The encoded password is {newpassword}, and the original password is {original_password}.\n")
        elif choice == 3:
            break
        else:
            print("Choice must be a number between 1 and 3\n")


        
            

if __name__ == "__main__":
    main()