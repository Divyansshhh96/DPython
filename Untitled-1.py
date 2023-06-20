def power(base, e):
    if (e==0):
        return 1
    else:
        return base*power(base, e-1)
    
v=int(input("Enter The Base")) 
u=int(input("Enter The e"))    
c=power(v,u)
print(v,"power",u , "==", c)



# before doing the arithmetic function(+ - * / ) etc what we write we get the same like here 
# base multiplied bt base not a whole function 
#if we write here e multiply then e got multiplied 