Year=int(input("Enter The Year"))
if( not(Year%100==100) and Year%4==0) or  (Year%100==100 and Year%400==0):
      print("Year is Leap Year")
else:
    print("The Year is not Leap Year")      