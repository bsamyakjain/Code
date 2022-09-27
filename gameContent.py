# importing the random module
import random

class MasterMind:
    maximum_number = 10
    number_of_digits = 3

    @staticmethod
    def disp():
        print("~~~ Welcome to Mastermind Game ~~~ ")
        username = input("Hi gamer, welcome to the Mastermind game  What is your name? ")
        print(f"Hello, {username}, Please follow the given instructions to play the game")

        print(""" ~~~GAME INSTRUCTION~~~ 
                I am thinking of a 3-digit number. Try to guess what it is. 
                Here are some clues: 
                When I say:       That means: 
                Yellow            One digit is correct but in the wrong position. 
                Green             One digit is correct and in the right position.      
                Red               No digit is correct. 
                For example, if the secret number was 346 and your guess was 843, the  clues would be Green Yellow.''' """)


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
        for i in user_input:
            if i in num:
                return "yellow"
        

        # guess wrong number
        else:
            return "Red"



