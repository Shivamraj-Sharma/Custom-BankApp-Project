from abc import ABC, abstractmethod

class IAdminServices(ABC):
    @abstractmethod
    def create_account(self, Accounts):
        pass
    
    @abstractmethod
    def delete_account(self, AccountNumber):
        pass

    @abstractmethod
    def view_accounts(self):
        pass

    @abstractmethod
    def transaction_by_date(self, startDate, EndDate):
        pass

    @abstractmethod
    def transaction_by_account(self, AccountNumber):
        pass

    @abstractmethod
    def transaction_by_type(self, type):
        pass

    @abstractmethod
    def generate_loan(self, Loans):
        pass

    @abstractmethod
    def view_loans(self):
        pass

    @abstractmethod
    def loan_by_account(self, AccountNumber):
        pass