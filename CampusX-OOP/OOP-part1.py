class Atm:

    # Constructor
    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.menu()

        print("mai to execute ho gaya")

    # Menu
    def menu(self):
        user_input = input("""
        Hi, how can I help you today?

        1. Press 1 to create your PIN
        2. Press 2 to change your PIN
        3. Press 3 to check your balance
        4. Press 4 to withdraw your balance
        5. Any other key to exit
        """)

        if user_input == "1":
            self.create_pin()

        elif user_input == "2":
            self.change_pin()

        elif user_input == "3":
            self.check_balance()

        elif user_input == "4":
            self.withdraw_balance()

        else:
            exit()

    # Create PIN
    def create_pin(self):
        user_pin = input("Enter your pin: ")
        self.pin = user_pin

        user_balance = int(input("Enter balance: "))
        self.balance = user_balance

        print("PIN created successfully")

        self.menu()

    # Change PIN
    def change_pin(self):
        old_pin = input("Enter your old pin: ")

        if old_pin == self.pin:
            new_pin = input("Enter new pin: ")
            self.pin = new_pin

            print("PIN changed successfully")

            self.menu()

        else:
            print("Wrong PIN")

            self.menu()

    # Check Balance
    def check_balance(self):
        user_pin = input("Enter your pin: ")

        if user_pin == self.pin:
            print("Your balance is:", self.balance)

            self.menu()

        else:
            print("Wrong PIN")

            self.menu()

    # Withdraw Balance
    def withdraw_balance(self):
        user_pin = input("Enter your pin: ")

        if user_pin == self.pin:

            amount = int(
                input("Enter the amount you want to withdraw: ")
            )

            if amount <= self.balance:
                self.balance = self.balance - amount

                print(
                    "Withdrawal successful, "
                    "your new balance is:",
                    self.balance
                )

            else:
                print("Insufficient balance")

        else:
            print("Wrong PIN")

        self.menu()


# Creating an object
obj = Atm()