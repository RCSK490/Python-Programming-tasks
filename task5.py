a=input("Enter name of the month (first letter in caps)")
if(a=="January"):
 print("No of days:31 days")
elif(a=="February"):
 h=int(input("enter year"))
 if(h%4==0 and (h%100!=0 or h%400==0)):
  print("No of days:29 days")
 else:
  print("No of days:28 days")
elif(a=="March"):
 print("No of days:31 days")
elif(a=="April"): 
 print("No of days:30 days")
elif(a=="May"):
 print("No of days:31 days")
elif(a=="June"):
 print("No of days:30 days")
elif(a=="July"):
 print("No of days:31 days")
elif(a=="August"):
 print("No of days:31 days")
elif(a=="September"):
 print("No of days:30 days")
elif(a=="October"):
 print("No of days:31 days")
elif(a=="November"):
 print("No of days:30 days")
elif(a=="December"):
 print("No of days:31 days")