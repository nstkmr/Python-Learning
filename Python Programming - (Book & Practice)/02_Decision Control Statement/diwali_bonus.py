salary = float(input("Enter your salary: "))
sex = input("Enter your sex(m or f): ")

if (sex == 'm'):
    bonus_salary = (salary * 0.05) + (salary * 0.02)
    bonus_salary1 = salary * 0.05

    if (salary < 10000):
        salary += bonus_salary
        print("Your salary with bonus "+ str(bonus_salary) +" is "+ str(salary))
    
    else :
        salary += bonus_salary1
        print("Your salary with bonus "+ str(bonus_salary1) +" is "+ str(salary))

else :
    bonus_salary = (salary * 0.1) + (salary * 0.02)
    bonus_salary1 = salary * 0.1

    if (salary < 10000):
        salary += bonus_salary
        print("Your salary with bonus "+ str(bonus_salary) +" is "+ str(salary))
    
    else :
        salary += bonus_salary1
        print("Your salary with bonus "+ str(bonus_salary1) +" is "+ str(salary))
