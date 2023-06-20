#Function
'''def demo():
   return 2
print((demo()))         #This is also the method for return the value
result=demo()           #This is also the method for return the value
print(result)


#retuen multiple values
def demo():
   return 2,8
print((demo()))         
n1,n2=demo()           
print(n1,n2)'''


#local values

def demo():
   a=2
   print(a) #local variable

demo()   
#print(a) #canot be accesed 


##glocal variable
def demo(name):
   name='john'
   print(name)
demo("john")
