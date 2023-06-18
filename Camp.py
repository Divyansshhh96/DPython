print("Welcome To Blood Donation Camp")
Age=int(input("Age="))
Weight=int(input("Weight="))
Height=float(input("Height="))
BG=input("Blood Group is ")
if(Age>=19):
    if(Weight>=45):
        if(Height>=1.73):
            if(BG=='O+' or 'O-' or 'B+'or 'B-'):
                print("You Are Eligible For Blood Donation Camp")
            else:
                print("Blood Group is Not Matched")    
        else:
            print("Height Is Not Valid")   
    else:
        print("You are Underweight")
else:
    print("You Are UnderAge")                     