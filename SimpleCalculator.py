# Sarai Ayon
# 5/3/2024
# CS240 Data Structures and Algorithms
# Chapter 5: Hash Tables

# Simple Calculator: This calculator provides a simple command-line interface where the user selects an operation 
# (addition, subtraction, multiplication, or division) and enters two numbers to perform the selected operation. 

def add(x, y):
    """Addition"""
    return x + y

def subtract(x, y):
    """Subtraction"""
    return x - y

def multiply(x, y):
    """Multiplication"""
    return x * y

def divide(x, y):
    """Division"""
    if y == 0:
        return "Error! Division by zero!"
    return x / y


def horner_method(coefficients, x):
    """Horner's Method"""
    result = 0
    for coefficient in coefficients:
        result = result * x + coefficient
    return result

def main():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))

if __name__ == "__main__":
    main()
