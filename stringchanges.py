import random

flag = 0
random_choice = [1,2,3]
n = "yes"

while(True):
    if (flag > 0 ):
        print("Continue? ('yes' to continue) : ", end="")
        #converting all kind of input to lower case "Yes", "yEs", .....
        n= input().lower()
        if n=="yes" or n == "no":
            if n == "no":
                break
        else:
            print("Invalid entery ,please Enter yes or no ")
            continue


    if n =="yes":  
        str_len = random.choice(random_choice)
        print(f"Enter the string with {str_len} character :", end="")
        user_input = input()
        if len(user_input) != str_len:
            print("Invalid string character, enter the string with proper character length")
            continue

        else:
            if user_input == 'e':
                print('t')
            
            elif user_input == 'tRZ':
                print("ERROR")

            elif user_input == "os":
                print("so")

            elif user_input == "et":
                print("te")

            elif user_input == "oso":
                print("sos")
            
            flag = 1
        
