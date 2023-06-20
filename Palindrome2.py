def string(variable):
    if (len(variable)==1):
        return True
    else:
        if(variable[0]==variable[-1]):
            return string(variable[1:-1])
        else:
            return False
v=input("Enter The Variable")        
result=string(v)
if (result):     #if we write only result it means that it is true
    print("Palindrome")
else :
    print("not")    