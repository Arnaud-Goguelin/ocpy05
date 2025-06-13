class BankAccount:

    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    def __setattr__(self, name: str, value: str | int) -> None:
        """Intercepts attribute assignment for validation."""
        if name == "account_holder":
            value = self.__validate_account_holder(value)
        if name == "balance":
            value = self.__validate_balance(value)
        super().__setattr__(name, value)

    @staticmethod
    def __validate_account_holder(account_holder: str) -> str:
        """Validates that a given account holder is a non-empty string."""
        if not isinstance(account_holder, str):
            raise TypeError("Account holder must be a string")
        if account_holder.isdigit():
            raise ValueError("Account holder cannot be a number")
        if not account_holder.strip():
            raise ValueError("Account holder cannot be empty")
        return account_holder

    @staticmethod
    def __validate_balance(balance: int | float) -> int | float:
        """Validates that a given balance is a non-negative float."""
        if not isinstance(balance, int | float):
            raise TypeError("Balance must be a float")
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        return balance

    @staticmethod
    def __valide_amount(amount: int | float) -> int | float:
        """Validates that a given amount is a positive number."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        return amount

    def deposit(self, amount) -> None:
        """Deposit money into the account."""
        valid_amount = self.__valide_amount(amount)
        self.balance += valid_amount

    def withdraw(self, amount):
        """Withdraw money from the account."""
        valid_amount = self.__valide_amount(amount)
        if valid_amount > self.balance:
            raise ValueError(f"Insufficient funds to withdraw {valid_amount}.")
        self.balance -= valid_amount

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: {self.balance}"


if __name__ == "__main__":
    try:
        account = BankAccount("Bob", 100)
        print(account.__str__())
        account.deposit(50)
        print(account.__str__())
        account.withdraw(100)
        print(account.__str__())
        # account.withdraw(100)
        account.deposit(-100)

    except (ValueError, TypeError) as error:
        print("An error happened:")
        print(error)
