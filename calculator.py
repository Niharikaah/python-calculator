num1 = float(input("Enter your first digit: "))
num2 = float(input("Enter your second digit: "))
print("Choose your operator: + ,- ,* ,/ ")
operator= input()
if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Invalid operator selected!")        
