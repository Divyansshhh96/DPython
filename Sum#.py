def sumofdigit(num):
    if(num==0):
        return 0
    else:
        return num%10+sumofdigit(num//10)
v=int(input("Enter The Number "))    
print(sumofdigit(v))