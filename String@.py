S="I have 100 Dollar($)"
#for i in S:  
 #if(i.isdigit()==True):
 #  print(i)
 #if(i.isalpha()==True):
  #  print(i)   

num1=num2=num3=0
for i in S:
  if i.isalpha():
    num1=num1+1
  elif i.isdigit():
    num2=num2+1
  else:
    num3+=1
print(num1,num2,num3)    