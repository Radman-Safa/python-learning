def exam_check(score):
    if score >= 10:
        return "passed"
    else:
        return "failed"
      
def odd_or_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def health_situation(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"

def discount_calculator(price):
    if price > 1000:
        discount = 0.2
    elif price > 500:
        discount = 0.1
    else:
        discount = 0 
    return price - (price * discount)

def calculator(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "*":
        return number1 * number2
    elif operator == "-":
        return number1 - number2
    elif operator == "/":
        return number1 / number2
    else:
        return "invalid operator"
      
def biggest_number(number1, number2, number3):
    if number1 >= number2 and number1 >= number3:
        return number1
    elif number2 >= number1 and number2 >= number3:
        return number2
    else:
        return number3

def daily_wage(num_hours, hourly_wage):
    if num_hours <= 40:
        return num_hours * hourly_wage
    else:
        return 40 * hourly_wage + (num_hours - 40) * hourly_wage * 1.5
