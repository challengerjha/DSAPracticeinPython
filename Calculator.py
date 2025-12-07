# This is a simple calculator 

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b


while True:
    print("\nEnter operation (+, -, *, /) or 'q' to quit:")
    choice = input("Choice: ")

    if choice == 'q':
        break
    
    if choice in ['+', '-', '*', '/']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '+':
                print(f"Result: {add(num1, num2)}")
            elif choice == '-':
                print(f"Result: {sub(num1, num2)}")
            elif choice == '*':
                print(f"Result: {mul(num1, num2)}")
            elif choice == '/':
                result = div(num1, num2)
                print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    else:
        print("Invalid operation. Please try again.")

print("Calculator closed.")
