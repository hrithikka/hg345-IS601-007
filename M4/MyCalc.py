# UCID: hg345
# Date: 10/16/2023

class MyCalc:
    def __init__(self):
        self.ans = 0

    def add(self, num):
        self.ans += num
    #hg345 10/16/23 Does Valid Addition

    def subtract(self, num):
        self.ans -= num
    #hg345 10/16/23 Does Valid Subtraction

    def multiply(self, num):
        self.ans *= num
    #hg345 10/16/23 Does Valid Multiplication

    def divide(self, num):
        if num == 0:
            print("Error: Division by zero")
        else:
            self.ans /= num
    #hg345 10/16/23 Does Valid Division while handelling errors

def main():
    calculator = MyCalc()

    while True:
        user_input = input("Enter a calculation (e.g., 2 * 2 or ans + 5):\n")

        if user_input.lower() == 'exit':
            break

        if 'ans' in user_input:
            user_input = user_input.replace('ans', str(calculator.ans))

        try:
            result = eval(user_input)
            calculator.ans = result
            print(f"Result: {result}")
        except (SyntaxError, NameError, ZeroDivisionError):
            print("Invalid input or math error. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
