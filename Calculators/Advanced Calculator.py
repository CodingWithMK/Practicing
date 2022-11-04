num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

operator = input("Enter the operator you want: ")

if operator == '+':
    print(num_1 + num_2)
elif operator == '-':
    print(num_1 - num_2)
elif operator == '/':
    print(num_1 / num_2)
elif operator == '*':
    print(num_1 * num_2)
else:
    print("You entered an invalid operator!")