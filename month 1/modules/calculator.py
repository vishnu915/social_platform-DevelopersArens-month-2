class Calculator:
    def run(self):
        print("\n--- Calculator ---")
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            op = input("Operation (+ - * /): ")

            if op == "+":
                print("Result:", a + b)
            elif op == "-":
                print("Result:", a - b)
            elif op == "*":
                print("Result:", a * b)
            elif op == "/":
                print("Result:", a / b)
            else:
                print("Invalid operator")
        except Exception as e:
            print("Error:", e)

        input("\nPress Enter to continue...")
