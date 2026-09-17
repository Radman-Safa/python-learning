def salary_calculator(base_salary, extra_num_hours, extra_hourly_wage, tax_rate):
    salary = (base_salary + (extra_num_hours * extra_hourly_wage)) * (1 - tax_rate)
    return salary
