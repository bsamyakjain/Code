
# =============================================================================
# Imports
# =============================================================================
import smtplib
import datetime

import time
# =============================================================================
# SET EMAIL LOGIN REQUIREMENTS
# =============================================================================
gmail_user = "bsamyakjain@gmail.com"  # Enter emal here
gmail_app_password = "kpwmvwxdgjlmmsmp" # enter password here

# mainlist contains : ['s.no',firstName','LastName','address','email','phoneNumber','Lostdate','location','itemdetails','lastdate']
ll = ['firstName','LastName','address','email','phoneNumber','Lostdate','location','itemdetails']
sn = 1
mainlist = []


def send_email(gmail_user,gmail_app_password,sent_from,sent_to,email_text):
  try:
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      server.ehlo()
      server.login(gmail_user, gmail_app_password)
      server.sendmail(sent_from, sent_to, email_text)
      server.close()

      print('Email sent!')
  except Exception as exception:
      print("Error: %s!\n\n" % exception)
      print("check Email again")




message="""Press:
            1. If you want to report a new item
            2. If you already found a reported Item
            3. See all reported items
            4. to exit"""

flag=1


while (flag!=0):
  print(message)
  n = int(input("Enter your choice: "))

  if n==1:
    a = []
    a.append(sn)
    for i in ll:
      print("Enter the ",i," ",end="")
      a.append(input())
    today = datetime.date.today()
    two_week = today + datetime.timedelta(weeks = 2) # computing date after 2 weeks 
    x= str(two_week)
    a.append(x) # storing date after 2 weeks 
    sent_from = gmail_user
    sent_to = str(a[4])
    sent_subject = "Item listed!"
    sent_body = "Hey "+ str(a[1]) +" "+str(a[2])+", "+"\n\n"+"I hope you have been well!\n\n"+"your response has been recorded, we'll notify you once we retrieve your missing items."+ "\n\n"+"\nCheers,\n"+"Samyak Jain\n"
    email_text = 'Subject: {}\n\n{}'.format(sent_subject, sent_body)
    mainlist.append(a)
    sn+=1

    #sending initial email:
    send_email(gmail_user,gmail_app_password,sent_from,sent_to,email_text)

 # if the item is found then it will send email to the user if it is already exist (ie.reported for item lost) 
  if n==2:
    em = input("Enter the Email whose item was found: ")
    if len(mainlist) == 0:
        print("no record found, first enter some records")
        continue
    flag1 = 0
    #if it exist then updating the entry in list as "found "
    for i in range(len(mainlist)):
      if (em in mainlist[i]):
        mainlist[i][9] = "found"   #updating the value as found because no need to send email after 2 weeks
        j=i
        flag1 = 1
        
    if flag1 ==0:  
        print("email doesn't found in the records, please enter correct details")
        continue
        

    date = input("enter the date when the item is available to collect: ")
    loc = input("Enter the location from where the item can be collected: ")
    sent_subject = "Congrats!, your item found!"
    sent_body = "Hey "+ mainlist[j][1] +" "+mainlist[j][2]+", "+"\n\n"+"I hope you have been well!\n\n"+"Your missing item "+ mainlist[j][8] +" reported, has been found. so, please collect it from "+loc+", on date: "+ date+"."+"\n\n"+"\nCheers,\n"+"Samyak Jain\n"
    email_text = 'Subject: {}\n\n{}'.format(sent_subject, sent_body)
    #sending pickup email with location and date
    sent_to = mainlist[j][4]
    send_email(gmail_user,gmail_app_password,sent_from,sent_to,email_text)

# prints the data stored
  if n==3:
    print("Below are the all reported details: ")
    print(mainlist)

  if n==4:
    print("Thanks for using!")
    flag = 0

# It will check every times the loop runs that whether the 2 weeks has finished or not if not then do nothing
# if today is the ending of 2 weeks then send email automatically
  if len(mainlist) == 0:
    print("no record found, first enter some records")
    continue
 
  for i in range(len(mainlist)):
        today1 = datetime.date.today()
        if mainlist[i][-1] != "found":
            if mainlist[i][-1] == today1:
                sent_subject = "We're sorry!, your not item found!"
                sent_body = "Hey "+ mainlist[i][1] +" "+mainlist[i][2]+", "+"\n\n"+"I hope you have been well!\n\n"+"We're very sorry for your losses. Your missing item has not found. \n\n"+"\nCheers,\n"+"Samyak Jain\n"
                email_text = 'Subject: {}\n\n{}'.format(sent_subject, sent_body)
                listx = mainlist[i][-1]
                y, m, d = listx.split('-')
                send_time = datetime.datetime(int(y),int(m),int(d),3,0,0) # set your sending time in UTC
                time.sleep(send_time.timestamp() - time.time())
                send_email(gmail_user,gmail_app_password,sent_from,sent_to,email_text)
                print('sent email after 2 weeks')

  

  
      
 
