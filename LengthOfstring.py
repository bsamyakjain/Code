#Length of string without using len() function
def returnsLength(string):
    try:
        count = 0
        while(string[count]):
            count += 1
    except:
        print("Length of the String: ", count)


returnsLength("GeeksForGeeks")