class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def withdraw(self, entered_pin, amount):
        if entered_pin == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal Successful")
                print("Remaining Balance:", self.__balance)
            else:
                print("Insufficient Balance")
        else:
            print("Incorrect PIN")

    def check_balance(self, entered_pin):
        if entered_pin == self.__pin:
            print("Available Balance:", self.__balance)
        else:
            print("Incorrect PIN")


atm = ATM(1234, 10000)

pin = int(input("Enter your PIN: "))
atm.check_balance(pin)

amount = int(input("Enter withdrawal amount: "))
atm.withdraw(pin, amount)
