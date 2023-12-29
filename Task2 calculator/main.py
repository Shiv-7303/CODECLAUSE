from logic import *

while True:
    num1 = float(input("Enter the first number:- "))
    num2 = float(input("Enter the second number:- "))
    while True:
        print("Select the Operation to perform..")
        user = input("1.Add\n2.Subtract\n3.Multiply\n4.Division\n5.Exit\n")
        if user == "1":
            print(f"{num1} + {num2} = {add(num1,num2)}")
            break
        elif user == "2":
            print(f"{num1} - {num2} = {sub(num1,num2)}")
            break

        elif user == "3":
            print(f"{num1} * {num2} = {mul(num1,num2)}")
            break

        elif user == "4":
            print(f"{num1} / {num2} = {div(num1,num2)}")
            break

        elif user == "5":
            print("Exiting..!")
            break
    user = input("Want to continues (Y/N) ").lower()
    if user == 'n':
        print("Exiting..!")
        break
    else:
        continue