from abc import ABC, abstractmethod

class ICustomerServices(ABC):
    @abstractmethod
    def get_account(self, user_id):
        pass

    @abstractmethod
    def deposit(self, AccountNumber, Amount):
        pass
    
    @abstractmethod
    def withdrawl(self, AccountNumber, Amount):
        pass

    @abstractmethod
    def check_balance(self, AccountNumber):
        pass

    @abstractmethod
    def view_loans(self, AccountNumber):
        pass

    @abstractmethod
    def transaction_history(self, AccountNumber):
        pass