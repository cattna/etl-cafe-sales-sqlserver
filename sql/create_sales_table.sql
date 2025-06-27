USE DB_CafeSales;
GO

CREATE TABLE SalesTransactions (
    transaction_id VARCHAR(20) PRIMARY KEY,
    item VARCHAR(100),
    quantity INT,
    price_per_unit FLOAT,
    total_spent FLOAT,
    payment_method VARCHAR(50),
    location VARCHAR(50),
    transaction_date DATE
);
GO
