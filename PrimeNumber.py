N=int(input("Enter The Number "))
if N>1:
  for i in range(2,N):  
    if(N%i==0):
      print(N,"is not a prime a number ")
      break
  else :
    print(N, "is a prime number ")
else:
  print(N,"is not a prime number ")      