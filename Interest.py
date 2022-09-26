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
            start_year = int(input("What year you want to start savings ?: "))
            if 2021<=start_year<=2050:
                flag=0
            else:
                print("Re-enter valid value")
        except:
            print("Re-enter valid value ")
            continue
    
#end year
flag = 1
while(flag != 0):
        try:
            stop_year = int(input("What year do you want to stop savings ?: "))
            if 2021<=stop_year<=2100 and stop_year>=start_year:
                flag=0
            else:
                print("Re-enter valid value")
        except:
            print("Re-enter valid value ")
            continue
    
#Retirement year
flag = 1
while(flag != 0):
        try:
            ret_year = int(input("What year do you want to retire ?: "))
            if 2021<=ret_year<=2100 and ret_year>=stop_year:
                flag=0
            else:
                print("Re-enter valid value")
        except:
            print("Re-enter valid value ")
            continue


#Interest rate
flag = 1
while(flag != 0):
        try:
            rate = float(input("What is the Interest rate ?: "))
            if 0.5<=rate<=15:
                flag=0
            else:
                print("Re-enter valid value")
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
    
total = 0
print("year   Savings   Interest     Total")
print("_"*30)
while(start_year<=ret_year):
    if (start_year<=stop_year):
        annual_savings
    
    else:
        annual_savings= 0

    interest = (annual_savings + total) *(rate/100)
    interest = round(interest)
    total += annual_savings + interest
    print(str(start_year)+"    "+str(annual_savings)+"    "+str(interest)+"    "+str(total))
    start_year+=1


    
  
    
    

    

