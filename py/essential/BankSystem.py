from collections import defaultdict
from enum import Enum

from sortedcontainers import SortedList


class TransactionType(Enum):
    DEPOSIT = "deposit"
    PAY = "PAY"
    TRANSFER = "TRANSFER"


class Account:
    def __init__(self, accountId: str, createdTime: int):
        self.accountId: str = accountId
        self.createdTime: int = createdTime
        self.balance: int = 0
        self.txHistory: list = []  # (timestamp, type, amount)

    def __str__(self):
        return f"Account(id: {self.accountId}, balance: {self.balance})"


class Banking:
    def __init__(self):
        self.accounts = defaultdict(Account)
        self.cashbackDelay = 24
        self.cashbackRate = 0.1

    def createAccount(self, accountId: str, timestamp: int) -> bool:
        if accountId in self.accounts:
            return False
        newAccount = Account(accountId, timestamp)
        self.accounts[accountId] = newAccount
        return True

    def deposit(self, timestamp: int, accountId: str, amount: int):
        if accountId not in self.accounts:
            raise ValueError(f"accountid {accountId} is invalid")
        account: Account = self.accounts[accountId]
        account.balance += amount
        account.txHistory.append((timestamp, TransactionType.DEPOSIT, amount))
        return account.balance

    def transfer(
        self, timestamp: int, accountIdFrom: str, accountIdTo: str, amount: int
    ):
        if (
            accountIdFrom == accountIdTo
            or accountIdTo not in self.accounts
            or accountIdFrom not in self.accounts
            or amount <= 0
        ):
            raise ValueError(f"input is invalid")

        accountFrom: Account = self.accounts[accountIdFrom]
        accountTo: Account = self.accounts[accountIdTo]

        if accountFrom.balance < amount:
            raise Exception("insufficient balance")

        accountFrom.balance -= amount
        accountTo.balance += amount
        accountFrom.txHistory.append((timestamp, TransactionType.TRANSFER, -amount))
        accountTo.txHistory.append((timestamp, TransactionType.TRANSFER, amount))

        return accountFrom.balance

    def pay(self, timestamp: int, accountId: str, amount: int):
        if accountId not in self.accounts or self.accounts[accountId].balance < amount:
            raise ValueError("invalid input")

        account: Account = self.accounts[accountId]
        account.balance -= amount
        account.txHistory.append((timestamp, TransactionType.PAY, -amount))
        return account.balance

    def getCashbackAt(self, timestamp: int, accountId: str):
        if accountId not in self.accounts:
            raise ValueError(f"accountid {accountId} is invalid")
        account = self.accounts[accountId]
        return round(
            -self.cashbackRate
            * sum(
                history[2]
                for history in account.txHistory
                if history[1] == TransactionType.PAY
                and history[0] + self.cashbackDelay <= timestamp
            ),
            2,
        )

    def topSpenders(self, k: int):
        accountSpending = []
        for accountId, account in self.accounts.items():
            accountSpending.append(
                (
                    sum(
                        history[2]
                        for history in account.txHistory
                        if history[1] == TransactionType.TRANSFER
                    ),
                    accountId,
                )
            )
        accountSpending.sort(reverse=False)
        return accountSpending[:k]

    def viewAccount(self, accountId: str) -> Account:
        return self.accounts[accountId]


if __name__ == "__main__":
    banking = Banking()
    banking.createAccount(1, 1)
    banking.createAccount(2, 2)
    banking.createAccount(3, 3)
    banking.deposit(3, 1, 100)
    banking.deposit(4, 2, 100)
    banking.deposit(4, 3, 100)
    banking.transfer(5, 1, 2, 50)
    banking.transfer(5, 3, 2, 20)
    banking.pay(6, 2, 10)
    banking.pay(10, 2, 10)
    banking.pay(20, 2, 3)
    banking.pay(30, 2, 10)
    banking.pay(40, 2, 10)
    banking.pay(50, 2, 10)
    banking.pay(60, 2, 100)
    print(banking.viewAccount(1))
    print(banking.viewAccount(2))
    print(banking.viewAccount(3))
    print(banking.topSpenders(2))
    print(banking.getCashbackAt(40, 2))
    print(banking.getCashbackAt(50, 2))
    print(banking.getCashbackAt(100, 2))
    print(banking.getCashbackAt(100, 1))
