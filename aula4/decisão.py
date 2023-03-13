#POSITIVO, NEGATIVO OU NULO
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
        print("Null")

