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

def horner_method(poly, x):
    result = poly[0]
    for i in range(1, len(poly)):
        result = result * x + poly[i]
    return result

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_coefficients(prompt):
    while True:
        try:
            return list(map(float, input(prompt).split()))
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")


def main():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Polynomial Evaluation")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice")
        return


choice = input("Enter choice (1/2/3/4/5): ")

if choice == '5':
    poly = get_coefficients("Enter the coefficients of the polynomial (from highest degree to lowest), separated by spaces (e.g. '2 3 4' for 2x^2 + 3x + 4): ")
    x = get_float("Enter the value of x (e.g. '5'): ")
    print("Result:", horner_method(poly, x))
else:
    num1 = get_float("Enter first number (e.g. '10'): ")
    num2 = get_float("Enter second number (e.g. '5'): ")

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