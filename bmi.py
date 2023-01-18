height = float(input("Enter your height (in inches): "))
weight = float(input("Enter your weight (in pounds): "))

calc_bmi = round((int(weight) * 703) / (height ** 2), 2)

print(f"BMI: {calc_bmi}")
if (calc_bmi < 16.0):
    print('SEVERLY Underweight')
elif (calc_bmi >= 16 and calc_bmi < 18.5):
    print('Underweight')
elif (calc_bmi >= 18.5 and calc_bmi < 25.0):
    print('Normal')
elif (calc_bmi >= 25 and calc_bmi < 30.0):
    print('Overweight')
elif (calc_bmi >= 30 and calc_bmi < 35.0):
    print('MODERATELY Obese')
elif (calc_bmi >= 35 and calc_bmi < 40):
    print('SEVERLY Obese')
else:
    print('MORBIDLY Obese')
