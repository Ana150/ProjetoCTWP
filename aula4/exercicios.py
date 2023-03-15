'''#INSS EXERCISE

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


#CHECK IF THE NUMBER IS POSITIVE, NEGATIVE OR NULL
number = int(input("Insert a number: "))

if number > 0:
    print(f"The number {number} is positive")

elif number < 0:
    print(f"The number {number} is negative")

else:
    print("Null")

#CHECK THE AGE
age = int(input("Insert tour age: "))

if age > 18:
    print("Congrats, you're over 18")

elif age == 18:
    print("Congrats, you're exactly 18")

elif age == 17:
    print("Sorry, almost there")

else:
    print("Sorry, you're under 18")

#CHECK IF THE NUMBER IS EVEN OR ODD
number = int(input("Insert a number: "))

if number%2 == 0:
    print("Even")
else:
    print("Odd")

#CHECK WHAT'S THE BIGGER NUMBER
number1 = int(input("Insert the first number: "))
number2 = int(input("Insert the second number: "))

if number1 > number2:
    print(f"{number1} is bigger than {number2}")
elif number1 == number2:
    print(f"{number2} and {number1} are equal")
else:
    print(f"{number2} is bigger than {number1}")

#CHECK THE AVERAGE
value1 = int(input("Insert the first value: "))
value2 = int(input("Insert the second value: "))
average = (value1 + value2) / 2

if average > 5:
 situation = "approved"
else:
    situation = "disapproved"


print(f"The media is {int(average)} and the student is {situation}")

#CHECK IF THE NUMBER IS VALID
number = int(input("Insert the number: "))

if (number >= 0) and (number <= 10):
    print(f"{number} is valid")
else:
    print(f"{number} is not valid")

#TWO LAST EXERCISES TOGETHER

value1 = int(input("Insert the first value: "))
value2 = int(input("Insert the second value: "))
average = (value1 + value2) / 2

if (value1 and value2 >= 0) and (value1 and value2 <= 10):
    if average > 5:
        situation = "approved"
        print(f"The media is {int(average)} and the student is {situation}")
    else:
        situation = "disapproved"
        print(f"The media is {int(average)} and the student is {situation}")

else:
    print(f"{value1} and/or {value2} is not valid, try again!")

#AVAREGE WITH 3 NUMBERS AND ONE OF THEM WILL BE DELETED

value1 = int(input("Insert the first value: "))
value2 = int(input("Insert the second value: "))
value3 = int(input("Insert the third value: "))

if (value1 < value2) and (value1 < value3):
    average = (value2 + value3) / 2
    if average > 5:
        situation = "approved"
        print(f"The media is {int(average)} and the student is {situation}")
    else:
        situation = "disapproved"
        print(f"The media is {int(average)} and the student is {situation}")

elif (value2 < value3) and (value2 < value1):
    average = (value1 + value3) / 2
    if average > 5:
        situation = "approved"
        print(f"The media is {int(average)} and the student is {situation}")
    else:
        situation = "disapproved"
        print(f"The media is {int(average)} and the student is {situation}")

else:
    average = (value1 + value2) / 2
    if average > 5:
        situation = "approved"
        print(f"The media is {int(average)} and the student is {situation}")
    else:
        situation = "disapproved"
        print(f"The media is {int(average)} and the student is {situation}")'''

#FINDING THE BIGGEST NUMBER

value1 = int(input("Insert the first value: "))
value2 = int(input("Insert the second value: "))
value3 = int(input("Insert the third value: "))

if (value1 > value2) and (value1 > value3):
    print(f"The biggest numeber is: first one {value1}")

elif (value2 > value1) and (value2 > value3):
    print(f"The biggest numeber is: second one {value2}")

else:
    print(f"The biggest numeber is: third one {value3}")