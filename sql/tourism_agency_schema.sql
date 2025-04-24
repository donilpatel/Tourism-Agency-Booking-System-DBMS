
-- MySQL Schema for Tourism Agency Booking System (BCNF)

CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    address VARCHAR(200)
);

CREATE TABLE Customer_Phone (
    phone VARCHAR(15) PRIMARY KEY,
    customer_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Tour_Package (
    package_id INT PRIMARY KEY,
    package_name VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL,
    price_per_person DECIMAL(10,2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

CREATE TABLE Booking (
    booking_id INT PRIMARY KEY,
    booking_date DATE NOT NULL,
    customer_id INT NOT NULL,
    package_id INT NOT NULL,
    number_of_people INT NOT NULL,
    total_cost DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (package_id) REFERENCES Tour_Package(package_id)
);

CREATE TABLE Payment (
    booking_id INT PRIMARY KEY,
    payment_date DATE NOT NULL,
    payment_amount DECIMAL(10,2) NOT NULL,
    payment_mode VARCHAR(20),
    FOREIGN KEY (booking_id) REFERENCES Booking(booking_id)
);

CREATE TABLE Guide (
    guide_id INT PRIMARY KEY,
    guide_name VARCHAR(50) NOT NULL,
    language VARCHAR(50) NOT NULL,
    availability_status VARCHAR(20)
);

CREATE TABLE Guide_Contact (
    contact_number VARCHAR(15) PRIMARY KEY,
    guide_id INT NOT NULL,
    FOREIGN KEY (guide_id) REFERENCES Guide(guide_id)
);

-- ====================================
-- SQL Queries from Assignment 4
-- ====================================

-- 1. Retrieve all bookings for a specific customer
SELECT * FROM Booking WHERE customer_id = 1001;

-- 2. Find customers who have spent more than $2000 on bookings
SELECT customer_id
FROM Booking
GROUP BY customer_id
HAVING SUM(total_cost) > 2000;

-- 3. Find the tour packages that have bookings with more than 2 people
SELECT DISTINCT package_id
FROM Booking
WHERE number_of_people > 2;

-- 4. List the total number of bookings made per customer
SELECT customer_id, COUNT(*) AS total_bookings
FROM Booking
GROUP BY customer_id;

-- 5. Find the total revenue generated from each tour package
SELECT package_id, SUM(total_cost) AS total_revenue
FROM Booking
GROUP BY package_id;

-- 6. Rank customers by their total spending
SELECT customer_id, SUM(total_cost) AS total_spending,
       RANK() OVER (ORDER BY SUM(total_cost) DESC) AS spending_rank
FROM Booking
GROUP BY customer_id;

-- 7. Assign a row number to each booking
SELECT *, ROW_NUMBER() OVER (ORDER BY booking_id) AS row_num
FROM Booking;

-- 8. Divide customers into 3 spending tiers based on total spending
SELECT customer_id, SUM(total_cost) AS total_spending,
       NTILE(3) OVER (ORDER BY SUM(total_cost) DESC) AS spending_tier
FROM Booking
GROUP BY customer_id;

-- 9. Find the most expensive tour package and its destination
SELECT package_id, destination, price_per_person
FROM Tour_Package
WHERE price_per_person = (
    SELECT MAX(price_per_person)
    FROM Tour_Package
);

-- 10. Find the total amount paid by each customer along with their payment mode
SELECT B.customer_id, P.payment_mode, SUM(P.payment_amount) AS total_paid
FROM Booking B
JOIN Payment P ON B.booking_id = P.booking_id
GROUP BY B.customer_id, P.payment_mode;

-- ====================================
-- Views
-- ====================================

-- View for Customer Spending Summary
CREATE VIEW Customer_Spending_Summary AS
SELECT customer_id, SUM(total_cost) AS total_spent
FROM Booking
GROUP BY customer_id;

-- View for Tour Package Popularity
CREATE VIEW Tour_Package_Popularity AS
SELECT package_id, COUNT(*) AS total_bookings
FROM Booking
GROUP BY package_id;

-- View for Payment Summary
CREATE VIEW Payment_Summary AS
SELECT DISTINCT B.customer_id, P.payment_mode, P.payment_amount
FROM Booking B
JOIN Payment P ON B.booking_id = P.booking_id;
