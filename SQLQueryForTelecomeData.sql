-- Providers Table
CREATE TABLE Providers (
    ProvidersID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL
);

INSERT INTO Providers (ProvidersID, Name) VALUES
(1, 'SaskTel'),
(2, 'Telus'),
(3, 'Bell'),
(4, 'Rogers'),
(5, 'Freedom Mobile');


UPDATE Providers
SET Name = 'Public Mobile'
WHERE Name = 'Freedom Mobile';


CREATE TABLE telecom_plans (
    plan_id VARCHAR(10) PRIMARY KEY,
    ProvidersID INT NOT NULL,
    plan_name VARCHAR(100),
    plan_type VARCHAR(20),
    data_gb INT,
    price_cad DECIMAL(6,2),
    network VARCHAR(10),
    category VARCHAR(20),
    contract_months INT,
    FOREIGN KEY (ProvidersID) REFERENCES Providers(ProvidersID)
);

--insert csv file for data plan
BULK INSERT telecom_plans
FROM 'D:\Git\TelecomProject\saskatchewan_telecom_plans_2025_with_id.csv'
WITH (
    FIRSTROW = 2,       -- Skip header row
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',
    TABLOCK
);

select*from telecom_plans order by ProvidersID asc

--create CustomerType Table
CREATE TABLE CustomerType (
    customerTypeID INT PRIMARY KEY,
    customer_type VARCHAR(50) NOT NULL,
    age_min INT,
    age_max INT,
    usage_pattern VARCHAR(20),
    seasonal_variance DECIMAL(4,3),
    growth_rate DECIMAL(4,3),
    network_preference VARCHAR(10),
    plan_preference VARCHAR(20),
    probability DECIMAL(4,2)
);

--insert data into CustomerType
INSERT INTO CustomerType (
    customerTypeID,
    customer_type,
    age_min,
    age_max,
    usage_pattern,
    seasonal_variance,
    growth_rate,
    network_preference,
    plan_preference,
    probability
) VALUES
(1, 'Young_Professional', 22, 35, 'high', 0.15, 0.025, '5G', 'Medium', 0.30),
(2, 'Family_User', 30, 50, 'medium', 0.20, 0.015, '5G', 'High', 0.25),
(3, 'Senior', 55, 75, 'low', 0.10, 0.005, '4G', 'Low', 0.20),
(4, 'Student', 18, 25, 'medium', 0.25, 0.020, '5G', 'Medium', 0.15),
(5, 'Business_User', 25, 55, 'high', 0.12, 0.018, '5G+', 'High', 0.10);


--Create table customers
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customerTypeID INT NOT NULL,
    age INT,
    city VARCHAR(50),
    providerID INT,
    plan_id VARCHAR(10),
    plan_name VARCHAR(100),
    plan_type VARCHAR(20),
    plan_category VARCHAR(20),
    data_allowance_gb INT,
    monthly_price_cad DECIMAL(6,2),
    network_type VARCHAR(10),
    contract_months INT,
    FOREIGN KEY (customerTypeID) REFERENCES CustomerType(customerTypeID),
    FOREIGN KEY (plan_id) REFERENCES telecom_plans(plan_id)
);

--insert csv file into Customers table
BULK INSERT Customers
FROM 'D:\Git\TelecomProject\saskatchewan_customers_2025_with_plan_id.csv'
WITH (
    FIRSTROW = 2,       -- Skip header row
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',
    TABLOCK
);

select*from Customers

--create CustomerUsage Table
CREATE TABLE CustomerUsage (
    customer_id INT NOT NULL,
    usage_date DATE NOT NULL,
    usage_gb DECIMAL(6,2) NOT NULL,
    plan_allowance_gb INT NOT NULL,
    plan_id VARCHAR(10) NOT NULL,
    overage_gb DECIMAL(6,2) NOT NULL,
    month_year VARCHAR(7) NOT NULL,
    PRIMARY KEY (customer_id, usage_date),
    FOREIGN KEY (plan_id) REFERENCES telecom_plans(plan_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

--insert csv file into CustomerUsage table
BULK INSERT CustomerUsage
FROM 'D:\Git\TelecomProject\saskatchewan_usage_data_2025_with_plan_id.csv'
WITH (
    FIRSTROW = 2,       -- Skip header row
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',
    TABLOCK
);

select*from CustomerUsage where YEAR = 2024
select*from telecom_plans
select * from Providers
select*from Customers
select*from Customers where providerID = 1
select*from Customers where providerID = 2
select*from Customers where providerID = 3
select*from Customers where providerID = 4
select*from Customers where providerID = 5



-- Add two new columns first
ALTER TABLE CustomerUsage
ADD [Month] VARCHAR(3),  -- or VARCHAR(10) if you want full month names
    [Year] INT;

-- Update the new columns by splitting month_year
UPDATE CustomerUsage
SET [Month] = LEFT(month_year, 3),
    [Year] = '20' + RIGHT(month_year, 2);  -- converts '24' to 2024


-- Set all provider initially to Public Mobile
UPDATE Customers
SET providerID = 5;

-- Update first 240 customers to SaskTel
WITH CTE_SaskTel AS (
  SELECT TOP(240) customer_id
  FROM Customers
  ORDER BY customer_id
)
UPDATE c
SET providerID = 1
FROM Customers c
JOIN CTE_SaskTel s ON c.customer_id = s.customer_id;

-- Update next 188 customers to Bell
WITH CTE_Bell AS (
  SELECT TOP(188) customer_id
  FROM Customers
  WHERE providerID = 5
  ORDER BY customer_id
)
UPDATE c
SET providerID = 3
FROM Customers c
JOIN CTE_Bell b ON c.customer_id = b.customer_id;

-- Update next 165 customers to Telus
WITH CTE_Telus AS (
  SELECT TOP(165) customer_id
  FROM Customers
  WHERE providerID = 5
  ORDER BY customer_id
)
UPDATE c
SET providerID = 2
FROM Customers c
JOIN CTE_Telus t ON c.customer_id = t.customer_id;

-- Update next 98 customers to Rogers
WITH CTE_Rogers AS (
  SELECT TOP(98) customer_id
  FROM Customers
  WHERE providerID = 5
  ORDER BY customer_id
)
UPDATE c
SET providerID = 4
FROM Customers c
JOIN CTE_Rogers r ON c.customer_id = r.customer_id;



