N=input("Enter a Number")
rev=reversed(N)
if list(N)==list(rev):
    print("Palindrome")
else:
    print("Not Palindrome")    
