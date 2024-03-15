from random import randint

a = input("Enter the number of operations to generate: ")
student_id = "2256327"
def main():
    try:
        with open("result.txt", "w") as file:
            file.write(f"Student ID: {student_id}\n")
            for n in range(int(a)):
                op = randint(3, 5)
                numbers = [0]*op + [0]*(op-1)
                operations = ['+', '-', '*', '/']
                ind = 0
                for i in range(op):
                    numbers[ind] = randint(0, 99)
                    ind += 1
                    if ind < len(numbers):
                        random_operation = operations[randint(0, len(operations)-1)]
                        numbers[ind] = random_operation
                        ind += 1
                expression = ''.join(str(item) for item in numbers)
                try:
                    result = eval(expression)
                    file.write(f"{expression} = {result:.2f}\n")
                except ZeroDivisionError:
                    file.write("Division by zero in the expression. Skipping.\n")
    except OSError:
        print("Error: file ""result.txt"" not found!")
if __name__ == "__main__":
    main()
