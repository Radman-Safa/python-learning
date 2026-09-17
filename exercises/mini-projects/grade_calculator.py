def grade_calculator(math, physics, programming):
    gpa = (math + physics + programming) / 3
    if gpa >= 17:
        return "excellent"
    elif gpa >= 14:
        return "good"
    elif gpa >= 10:
        return "passed"
    else:
        return "failed"
