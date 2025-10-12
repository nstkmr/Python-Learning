salary = float(input("Enter your salary: "))
sex = input("Enter your sex(m or f): ")

if (salary < 10000):
    if (sex == 'm'):
        bonus_salary = (salary * 0.05) + (salary * 0.02)
        salary += bonus_salary
        print("Your salary with bonus "+ str(bonus_salary) +" is "+ str(salary))

    else:
        bonus_salary = (salary * 0.1) + (salary * 0.02)
        salary += bonus_salary
        print("Your salary with bonus "+ str(bonus_salary) +" is "+ str(salary))

else:
    if (sex == 'm'):
        bonus_salary = (salary * 0.05)
        salary += bonus_salary
        print("Your salary with bonus "+ str(bonus_salary) +" is "+ str(salary))

    else:
        bonus_salary = (salary * 0.1)
        salary += bonus_salary
        print("Your salary with bonus "+ str(bonus_salary) +" is "+ str(salary))