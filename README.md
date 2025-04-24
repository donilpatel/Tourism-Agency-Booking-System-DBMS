# Tourism Agency Booking System DBMS

This repository contains the complete backend and schema design of a relational database for a Tourism Agency Booking System built for CP363.

## File Structure

- `sql/`: Full MySQL schema and advanced queries with views
- `gui_app/`: Python GUI interface for interacting with the DB
- `docs/`: Assignment documentation (PDFs and system overview)
- `README.md`: Project summary and usage instructions

## MySQL Schema

All tables are normalized to BCNF. Includes:
- Customer & Phone management
- Tour Packages & Booking
- Guide and Contact info
- Payments

Advanced SQL includes:
- Window functions (RANK, ROW_NUMBER, NTILE)
- Aggregate queries and correlated subqueries
- Views for customer and payment insights

## GUI App

Python-based interface to:
- Create/drop/populate/query tables
- Interact with the database using buttons and forms

## Functional Highlights

- Enforces referential integrity with foreign keys
- Avoids redundancy via normalization
- Demonstrates query performance and real-time interaction

## How to Run

1. Import the SQL schema into your MySQL database
2. Run `tourismagency_GUI.py` from the `gui_app/` directory
3. Use the options to interact with the system

## Contributors

- Donil Patel
- Hibah Hibah

## Date

April 2025
