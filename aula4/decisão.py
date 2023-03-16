'''#POSITIVO, NEGATIVO OU NULO
#ENCADEADO (RAIZ)
number = int(input("Insert a number: "))

if number > 0:
    print("Positive")
else:
    if number < 0:
        print("Negative")
    else:
        print("Null")

#ENCADEADO (ELIF)
number = int(input("Insert a number: "))

if number > 0:
    print("Positive")

elif number < 0:
        print("Negative")

else:
        print("Null")'''

#INSS EXERCISE

salary = float(input("Insert your salary: "))

if (salary > 0) and (salary <= 1302):
    inss = salary * 0.07

elif (salary > 1302) and (salary <= 2571.29):
    inss = salary * 0.09

elif (salary > float(2571.29)) and (salary <= float(3856.94)):
    inss = salary * 0.12

elif (salary > float(2571.29)) and (salary < float(7507.49)):
    inss = salary * 0.14

else:
    inss = 1051.05

print(f"""
Salary.....................: R$ {salary:8.2f}
INSS.......................: R$ {inss:8.2f}""")