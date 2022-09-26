start_year = 0
ret_year = 1
total = 0
while(start_year<=ret_year):

    flag = 1
    #Annual_savings
    while(flag != 0):
        try:
            annual_savings = int(input("What is your annual savings amount ?: "))
            flag=0
        except:
            print("Re-enter valid value ")
            continue
    
    #Start year
    flag = 1
    while(flag != 0):
        try:
            start_year = int(input("What is your annual savings amount ?: "))
            if 2021<=start_year<=2050:
                flag=0
        except:
            print("Re-enter valid value ")
            continue
    
    #end year
    flag = 1
    while(flag != 0):
        try:
            stop_year = int(input("What is your annual savings amount ?: "))
            if 2021<=stop_year<=2100 and stop_year>=start_year:
                flag=0
        except:
            print("Re-enter valid value ")
            continue
    
    #Retirement year
    flag = 1
    while(flag != 0):
        try:
            ret_year = int(input("What is your annual savings amount ?: "))
            if 2021<=ret_year<=2100 and ret_year>=stop_year:
                flag=0
        except:
            print("Re-enter valid value ")
            continue


    #Interest rate
    flag = 1
    while(flag != 0):
        try:
            rate = float(input("What is your annual savings amount ?: "))
        except:
            try:
                rate = float(rate[:-1])
                if 0.5<=rate<=15:
                    flag=0
                
                else:
                    continue

            except:
                print("Re-enter valid value")
                continue

    
    
    

    if (start_year<=stop_year):
        annual_savings
    
    else:
        annual_savings= 0

    interest = (annual_savings + total) *(rate/100)
    total += annual_savings + interest
    print(start_year+"  "+annual_savings+"  "+interest+"  "+total)


    
  
    
    

    

