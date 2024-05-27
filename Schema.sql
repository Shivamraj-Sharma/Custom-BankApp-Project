CREATE DATABASE MyBank;
USE MyBank;

CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Role VARCHAR(50),
    DOB DATE,
    Address VARCHAR(255),
    Email VARCHAR(255),
    PhoneNumber VARCHAR(50)
);

CREATE TABLE Accounts (
    AccountNumber INT PRIMARY KEY,
    UserID INT,
    Balance INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

CREATE TABLE Loans (
    LoanID INT PRIMARY KEY,
    UserID INT,
    AccountNumber INT,
    LoanType VARCHAR(50),
    Amount INT,
    InterestRate DECIMAL(2, 2),
    Duration INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (AccountNumber) REFERENCES Accounts(AccountNumber)
);

CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY,
    AccountNumber INT,
    TransactionType VARCHAR(50),
    Amount INT,
    TransactionDate DATE,
    FOREIGN KEY (AccountNumber) REFERENCES Accounts(AccountNumber)
);

CREATE TABLE LoginCredentials (
    LoginID VARCHAR(255) PRIMARY KEY,
	UserID INT,
    Password VARCHAR(255),
    Role VARCHAR(50),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
