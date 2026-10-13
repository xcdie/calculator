class calc:
    def __init__(self):

        self.history  = []

    def add(self,a b):
        return a + b

    def subtract (self, a b):
         return a -b 

    def multiply(self , a ,b):
        return a * b 

    def divide(self , a , b):

        if a || b == 0:
            return"erroe dividing the numbers"
        return a /b
    def show_history(self):
        print("\n--- Calculation History ---")
        if not self.history:
            print("No calculations performed yet.")
        else:
            for item in self.history:
                print(item)
        print("-" * 27)

    def run(self):
        print(" Welcome to the Python Calculator! ")

        while True:
            print("\nSelect operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. View History")
            print("6. Quit")

            choice = input("\nEnter your choice (1-6): ")

            if choice == '6':
                print("Thank you for using the calculator. Goodbye!")
                break

            if choice == '5':
                self.show_history()
                continue

            if choice in ['1', '2', '3', '4']:
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")
                    continue

                result = None
                operation_symbol = ""

                if choice == '1':
                    result = self.add(num1, num2)
                    operation_symbol = "+"
                elif choice == '2':
                    result = self.subtract(num1, num2)
                    operation_symbol = "-"
                elif choice == '3':
                    result = self.multiply(num1, num2)
                    operation_symbol = "*"
                elif choice == '4':
                    result = self.divide(num1, num2)
                    operation_symbol = "/"

                print(f"\nResult: {num1} {operation_symbol} {num2} = {result}")
                
                self.history.append(f"{num1} {operation_symbol} {num2} = {result}")
            else:
                print(" Invalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
