# MathExpressGen
MathExpressGen is a Python-based utility designed to automatically generate a wide variety of arithmetic expressions, evaluate their results, and record them in a text file. Each operation combines random numbers (0-99) and basic arithmetic operators (+, -, *, /). The script also handles division by zero errors by skipping those operations in the output file. It's designed as a simple utility for generating and recording arithmetic expressions and their outcomes, which can be useful for educational purposes, testing, or simply to challenge oneself with random math problems.

## Prerequisites

This script requires Python 3.x. Ensure that Python 3.x is installed on your system and is accessible from your command line or terminal.

## How to Use

1. **Clone or Download the Script**
   - Clone this repository to your local machine or download the script file directly.
2. **Running the Script**
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script using Python by executing the following command:
     ```
     python mathexpressgen.py
     ```
3. **Input the Number of Operations**
   - When prompted, enter the number of arithmetic operations you wish to generate and evaluate.
4. **Check the Output**
   - Upon completion, the script will create (or overwrite) a file named `result.txt` in the same directory.
   - Open `result.txt` to view the generated arithmetic expressions and their results.

## Handling Errors

- The script catches and handles `ZeroDivisionError` by skipping the offending operation and noting it in the output file.
- If there are any issues with file operations (e.g., the output file cannot be created), the script will report an error.

## Customization

- The script can be easily modified to change the range of numbers, the set of operations, or the format of the output file.
- Modify the `numbers` range or the `operations` list as needed.

## Contribution

Contributions to enhance the functionality or efficiency of this script are welcome. Please follow the standard GitHub pull request process to submit your contributions.
