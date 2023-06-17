num1=int(input())
num2=int(input())
num3=int(input())


if(num1>num2):
    if(num1>num3):
        print("Largest is Num1",num1)
    else:
        print("Largest is Num3",num3)  
elif (num2>num1):
    if(num2>num3):
        print("Largest Number is Num2",num2)
    else:
        print("Largest Number is Num3", num3)
elif(num3>num1):
    if(num3>num1):
        print("Largest Number is", num3)
    else:
        print("Largwst is ", num1)                       
