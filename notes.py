
import random

print(random.randint(1, 20))


tylers_age = input("how old are you? ")
tylers_age = int(tylers_age)
alexs_age = 34

# boolean

print(tylers_age > alexs_age)

if tylers_age >= alexs_age:
    print("you are older than sarah")
elif tylers_age == alexs_age:
    print("you are the same age as alex")
else:
    print("you are not older than alex")
