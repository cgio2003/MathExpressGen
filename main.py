from random import randint

op_num = input("Enter the number of operations to generate: ")
while op_num.isalpha(): # Check if the input is an integer
        op_num = input("Please enter an integer: ") # If not, ask again
student_id = "2256327"
def main():
    try:
        with open("result.txt", "w") as file:
            file.write(f"Student ID: {student_id}\n") # Write Student ID and number of expressions in result.txt
            file.write(f"Number of operations to generate: {op_num}\n")
            for n in range(int(op_num)): # Loop to generate "n" expression
                op = randint(3, 5) # Randomly generate the number of factors
                numbers = [0]*op + [0]*(op-1) # Total number of factors and operations
                operations = ['+', '-', '*', '/']
                ind = 0
                for i in range(op):
                    numbers[ind] = randint(0, 99) # Randomly generate factors
                    ind += 1
                    if ind < len(numbers):
                        random_operation = operations[randint(0, len(operations)-1)] # Randomly generate operations
                        numbers[ind] = random_operation
                        ind += 1
                expression = ''.join(str(item) for item in numbers) # Create expression from the list "numbers"
                try:
                    result = eval(expression) # Compute the result of each expression
                    file.write(f"{expression} = {result:.2f}\n") # Write each expression in result.txt
                except ZeroDivisionError:
                    file.write("Division by zero in the expression. Skipping.\n") # Handle ZeroDivisionError
    except OSError:
        print("Error: file ""result.txt"" not found!") # Handle OSError
if __name__ == "__main__":
    main()
