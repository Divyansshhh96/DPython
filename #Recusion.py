#Recusion
#Calculate factorial of a number using recursive function

def factorial(n):
  if (n==0):
    return 1
  else:
    return n*factorial(n-1)

v=int(input("Enter The Number"))
print(factorial(v))  