Weight=float(input("Weight"))
Height=float(input("Height"))
BMI=Weight/Height**2
if (BMI<18.5):
    print("Under Weight")
elif(BMI<=24.9 and BMI>=18.5):
    print("Normal Weight")
elif(BMI<=29.9 and BMI>=25):
    print("Overweight")
else:
    print("Obese")         