N=int(input("Number="))
S=0
T=N
while(T>0):
    R=T%10
    S=S+(R**3)
    T=T//10
if (N==S):
    print(N,"is an Armstrong number")
else:
    print(N,"is not  an Armstrong number") 