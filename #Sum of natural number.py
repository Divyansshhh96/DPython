#Sum of a function
def sum(n):
    if (n==1):
        return 1
    else:
        return n+sum(n-1)
v=int(input("Numer="))
summation=sum(v)
print(summation)
