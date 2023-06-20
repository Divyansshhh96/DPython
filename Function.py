'''def demo():
    print("Welcome")

demo()  #calling a function  

def demo(name):  #name is the parameter
    print(name)

demo('John')  #calling a function  


def demo(msg,name):
    print(msg,",",name)

demo("hello","john")  #calling a function  


#taking input as functiom
def demo(name):
    print(name)
n=input("Name=")    #take a new variable

demo(n)  #calling a function'''

'''def swap(n1,n2):
    print(n1,n2)
v=input("n1=")
u=input("n2=")

swap(u,v)'''


def demo(a,b):
    a,b=b,a
    print(a,b)

p=int(input("Enter First Number"))
q=int(input("Enter Second Number"))    
demo(p,q)