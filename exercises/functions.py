def discounted_price(originl_price, discount):
    final_price = original_price * (1 - discount)

def profit(fund, profit_ratio):
    pure_profit = fund * profit_ratio
    return pure_profit
  
def temprature_calculator(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def income_calculator(num_hours, hourly_wage):
   daily_wage = hourly_wage * num_hours 
   income = daily_wage * 26
   return income

def after_tax_price_calculator(pre_tax_price, product_tax_ratio):
    final_price = pre_tax_price + (pre_tax_price * product_tax_ratio)
    return final_price

def time_exchange(secs):
    num_mins = secs // 60
    num_secs = secs % 60
    return num_mins, num_secs
