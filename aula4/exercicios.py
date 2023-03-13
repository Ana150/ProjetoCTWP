salary = float(input("Insert your salary: "))

if (salary > 0) and (salary <= 1302):
    inss = salary * 7.5/100
    result = salary - inss
    print(result)

elif (salary > 1302) and (salary <= 2571.29):
    inss = salary * 9.0 / 100
    result = salary - inss
    print(result)

elif (salary > float(2571.29)) and (salary <= float(3856.94)):
    inss = salary * 12 / 100
    result = salary - inss
    print(result)

else:
    inss = salary * 14 / 100
    result = salary - inss
    print(result)
