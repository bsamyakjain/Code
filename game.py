from gameContent import MasterMind
flag='y'
correct_guess = 0
wrong_guess = 0
game_count = 0
while(flag != 'n'):
    game_count+=1
    if game_count !=1:
        n = input("\n\nWants to play again ? (yes or no)").lower()
    else:
        n = 'yes'

    
    if n == 'y' or 'y' == n[0]:
        P1 = MasterMind()
        P1.disp()
        print("\nI have thought up a number. You have 10 guesses to get it.\nGuess #1")
        num = P1.guessCode()
        for i in range(P1.maximum_number):
            user_input= input("Enter Input: ")
            color = P1.guess_Flag_color(user_input,num)
            if color == "Green":
                print(f"Guess #{i+1}")
                print("Green")
                correct_guess+=1
                break
            elif color == "yellow":
                print(f"Guess #{i+1}")
                print("Yellow")
                wrong_guess+=1

            else:
                print(f"Guess #{i+1}")
                print("Red")
                wrong_guess+=1



    elif n== 'n' or 'n'==n[0] :
        print("Total number of games played : ",game_count-1)
        print("Total number of correct guesses made: ", correct_guess)
        print("Average number of guesses: ",(correct_guess/game_count)*100)
        print("Thanks for playing, have a great day")
        flag = 'n'

    else:
        print("Thanks for playing, you've entered wrong input")
        
    
    








