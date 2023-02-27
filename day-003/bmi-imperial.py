height_feet = int(input('Please enter your height input feet(whole number): '))
height_inches = int(input('Please enter your height input feet(whole number): '))
weight = int(input('Please enter your weight input pounds(whole number): '))
height = height_feet * 12 + height_inches

bmi = (weight*703)/(height*height)

if bmi <= 18.5:
    print('Your BMI is', bmi,'which means you are underweight.')
elif bmi > 18.5 and bmi < 25:
    print('Your BMI is', bmi,'which means you are normal.')
elif bmi > 25 and bmi < 30:
    print('Your BMI is', bmi,'which means you are slightly overweight')
elif bmi > 30:
    print('Your BMI is', round(bmi, 2),'which means you are obese.')
else:
    print('There is an error with your input')
    print('Please check you have entered whole numbers\n'
          'and decimals were asked.')

