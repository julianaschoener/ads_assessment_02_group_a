"""
Simple Calculator
"""
# Provide your solution here
def calculate(operand1: int,operand2: int, string_operator: str):

    if string_operator == "+":
        sum = operand1 + operand2
        print(str(sum))
    elif string_operator == "-":
        sum = operand1 - operand2
        print(str(sum))
    elif string_operator == "*":
        sum = operand1 * operand2
        print(str(sum))
    elif string_operator == "/":
        sum = operand1 / operand2
        print(str(sum))
    elif string_operator == "?":
        sum = operand1 / operand2
        print("Invalid Operator")

calculate(1,2, "+")
calculate(1,2, "-")
calculate(1,2, "*")
calculate(1,2, "/")
calculate(0,2, "/")
calculate(0,2, "?")
"""
Reverse Word
"""
# Provide your solution here

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

def reverse_word(word: str) -> str:

    for i in range(len(word)):
        print(word.capitalize()[-1 - i])

reverse_word("hello")
reverse_word("WORLD")
reverse_word("Noel")