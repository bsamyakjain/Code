def convert_to_Caesar(user_input,UPPERCASECHARACTERS,VALIDCHARACTERS):
    output_string = ""
    try:
        for i in user_input:

            #if entered "." then convert it to "X"
            if i == ".":
                output_string+="X"

            # if enter invalid character then skip it
            elif i not in VALIDCHARACTERS:
                continue
            
            # if entered Upper case value then add without any changes
            elif i in UPPERCASECHARACTERS:
                output_string+=i

            # converting lower case to upper case using ASCII value 
            # a has value 97 and A has value 65 
            # so subtracting every value to 32 get result as UPPERCASE
            else:
                output_string+= chr(ord(i)-32)
        
        return output_string

    except:
        print("Some Exceptions occured")
        exit()

  




UPPERCASECHARACTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
VALIDCHARACTERS = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
user_input = input("Enter string : ")
output_string = convert_to_Caesar(user_input,UPPERCASECHARACTERS,VALIDCHARACTERS)
print("Resultant string = ",output_string)
