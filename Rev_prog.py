#let's start building a calculator

#first we will define 3 variables

first_number = int(input("enter first number : "))
operator = input("Enter Operator(+,-,*,?) : ")
second_number = int(input("Enter Second Number : "))





def calculator(first_number,second_number,operator):
    if operator == "+":
        add = first_number + second_number
        print(add)
    elif operator == "-":
        sub = first_number - second_number
        print(sub)
    elif operator == "*":
        mul = first_number * second_number
        print(mul)
    elif operator == "/":
        div = first_number / second_number
        print(div)
    else:
        print("Please provide correct input!")



calculator(first_number,second_number,operator);