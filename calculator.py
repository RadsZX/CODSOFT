n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
print("Select an operation you want to perform:")
operation = int(input())

if operation == 1:
    print("The sum of numbers is", n1 + n2)
elif operation == 2:
    print("Subtraction of numbers is", n1 - n2)
elif operation == 3:
    print("Product of numbers is", n1 * n2)
elif operation == 4:
    if n2 != 0:
        print("Quotient is", n1 / n2)
    else:
        print("Error: Division by zero!")
else:
    print("Invalid choice entered")
