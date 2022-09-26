from gameContent import MasterMind
flag='y'
correct_guess = 0
wrong_guess = 0
game_count = 0
while(flag != 'n'):
    game_count+=1
    if game_count !=1:
        print("-"*20)
        print("\n\nWants to play again ?")
    
    P1 = MasterMind()
    P1.disp()
    n = input("Your input : ").lower()
    if n == 'y' or 'y' == n[0]:

        
        for i in range(P1.maximum_number):
            num = P1.guessCode()
            user_input= input("Enter the guess : ")
            color = P1.guess_Flag_color(user_input,num)
            if color == "Green":
                print("wow!!........Perfect guess, congrats!!")
                correct_guess+=1
                break
            elif color == "yellow":
                print("Aha!.........Somewhat near to the number, try again")
                wrong_guess+=1

            else:
                wrong_guess+=1
                print("------OOPs........Wrong guess, try again------")



    elif n== 'n' or 'n'==n[0] :
        print("Total number of games played : ",game_count-1)
        print("Total number of correct guesses made: ", correct_guess)
        print("Average number of guesses: ",(correct_guess/game_count)*100)
        print("Thanks for playing, have a great day")
        flag = 'n'

    else:
        print("Thanks for playing, you've entered wrong input")
        
    
    








