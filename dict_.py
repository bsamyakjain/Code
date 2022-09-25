windows_attributes = {}

window_attributes= """
Window Administartion Application

a: Exit Application
b: Enter an attribute
c: Calculate and display the aspect ratio
d: Display the window attributes and values
"""

done = False


while not done:
    
    print(window_attributes)
    
    selection = input("Please choose a, b, c, or d: ")
    
    if selection == "a":
        print("Done!")
        break
    
    elif selection == "b":
        print("Entering an attribute selected")
        
        name = input("Enter attribute name: ")
        
        val = input("Enter attribute value: ")
        
        windows_attributes[name] = val
        
        print(name + ":" + val + "  have been added to the dictionary.")
        
    elif selection == "c":
        # if "width " or "height " is not available then loop will continue to menu
        if ("width" not in windows_attributes) or ("heigth" not in windows_attributes):
            print("The attribute needs to be added it is not in the attribute list, please enter the value by going back to option b")
            continue
        else: 
            try:
                w = int(windows_attributes['width'])
                h = int(windows_attributes['heigth'])
                print(f"Calculate aspect ratio selected : {round(w/h,2)}")
            except ValueError:
                print("ValueError exceptions which will be caused by a non-numeric width attribute, please re-enter the numeric value")
                continue

            except ZeroDivisionError:
                print("ZeroDivision Error, the height attribute has to be re-entered with a positive non-zero number.")
                continue

        
    elif selection == "d":
        print("Displaying all the attributes and values : ")
        
        for key,value in windows_attributes.items():
            print(key + ":" + value)
        
    else:
        print("Invalid choice. Please enter a, b, c, or d.")