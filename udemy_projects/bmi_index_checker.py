#Body Mass Index Calculator
"""Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese."""

#Formula BMI = weight / height ^ 2

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ") 
bmi_quotient = float(weight) / pow(float(height), 2)
rounded_up_bmi_qoutient = round(bmi_quotient)

if bmi_quotient < 18.5:
    print(f"Your BMI is {rounded_up_bmi_qoutient}, you are underweight.")
elif bmi_quotient > 18.5 and bmi_quotient < 25:
    print(f"Your BMI is {rounded_up_bmi_qoutient}, you have a normal weight.")
elif bmi_quotient > 25 and bmi_quotient < 30:
    print(f"Your BMI is {rounded_up_bmi_qoutient}, you are slightly overweight.")
elif bmi_quotient > 30 and bmi_quotient < 35:
    print(f"Your BMI is {rounded_up_bmi_qoutient}, you are obese.")
else:
    print(f"Your BMI is {rounded_up_bmi_qoutient}, you are clinically obese.")
