# importing the random module
import random

class MasterMind:
    maximum_number = 10
    number_of_digits = 3

    @staticmethod
    def disp():
        print("""press the below option to play game:
        -> 'y' to play
        -> 'n' to stop
         """)


    @classmethod
    def guessCode(cls):
        num=""
        # Program to generate a random number between 0 and 9
        for i in range(cls.number_of_digits):
            num += str(random.randint(0,9))
        return num

    @staticmethod
    def guess_Flag_color(user_input,num):
        
        #guess correct then green signal
        if user_input == num:
            return "Green"
        
        #some digit is correct ie num is 123 and user guess 12 then yellow signal
        elif user_input in num or num in user_input:
            return "yellow"

        # guess wrong number
        else:
            return "Red"



