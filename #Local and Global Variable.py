#Local and Global Variable
a=10 # gloabal Variable
def demo():
    global a
    a=a+2

    print(a)
demo()

#

def demo(a=10):#Default Values
    print(a)

demo()

#    
def demo(a=10):#Default Values
    print(a)

demo(4)    

#

def demo(*args):
    print(*args)

demo(4,12,34,56,78,90)    