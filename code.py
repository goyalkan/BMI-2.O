height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

a = round(weight/(height*height))


if float(a) <= 18.5 :
  print(f"Your BMI is {a}, you are underweight.")

elif a<= 25 :
    print(f"Your BMI is {a} , you have a normal weight.")

elif a<= 30:
    print(f"Your BMI is {a} , you are slighlty overweight.")

elif a<=35 :
    print(f"Your BMI is {a}  , you are obese.")

else  :

    print(f"Your BMI is {a} , you are clinically obese.")               

  
