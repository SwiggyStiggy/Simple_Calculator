#---------------------------------------------------------------------


VE = ValueError

#Class with adding, subtracting, multiplying, dividing

class calculator:
    def add(self, num1, num2):
        if isinstance(num1, float) or isinstance(num2, float):
            return float(num1 + num2)
        else:
            return int(num1 + num2)

    def sub(self, num1, num2):
        if isinstance(num1, float) or isinstance(num2, float):
            return float(num1 - num2)
        else:
            return int(num1 - num2)

    def multi(self, num1, num2):
        if isinstance(num1, float) or isinstance(num2, float):
            return float(num1 * num2)
        else:
            return int(num1 * num2)

    def div(self, num1, num2):
        if num2 == 0:
            raise VE("Division by zero is not allowed")
        elif isinstance(num1, float) or isinstance(num2, float):
            return float(num1 / num2)
        else:
            return int(num1 / num2)



#making sure that only a number is used in the input-----------------------------------

while True:
    try:
        first_num = float(input("Enter the first number: "))
        break
    except VE:
        print("Invalid input. Please enter a valid number.")



while True:
    try:
        second_num = float(input("Enter the second number: "))
        break
    except VE:
        print("Invalid input. Please enter a valid number for the second number.")


#input to choose the operation----------------------------------------------------------
valid_operations = ["add", "sub", "multi", "div"]
operation = input("Enter the operation number (add/sub/multi/div): ")
while operation not in valid_operations:
    print("Invalid operation, please choose a correct one.")
    operation = input("Enter the operation number (add/sub/multi/div): ")



#instance-------------------------------------------------------------------------------
calculate = calculator()


if operation == "add":
    result = calculate.add(first_num, second_num)
elif operation == "sub":
    result = calculate.sub(first_num, second_num)
elif operation == "multi":
    result = calculate.multi(first_num, second_num)
elif operation == "div":
    try:
        result = calculate.div(first_num, second_num)
    except VE:
        print("Error: cannot divide by zero")
        result = None
else:
    print("Invalid operation.")

if first_num.is_integer() and second_num.is_integer():
    result = int(result)
    print(f"The result is: {result}")
else:
    result = result
    print(f"The result is: {result}")
