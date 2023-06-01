# Database Management System

This code is a simple implementation of a Database Management System using SQLite and Python. It provides functionality to interact with a SQLite database named "customer.db" and perform various operations like adding records, deleting records, looking up records based on email, and displaying all records.

## Prerequisites

To run this code, you need to have the following installed:

- Python
- SQLite

## Getting Started

1. Clone the repository or download the code files.

2. Make sure you have the SQLite database file "customer.db" in the same directory as the code file.

3. Import the required modules:
    ```python
    import sqlite3
    import database
    ```

4. Start using the database functions.

## Functions

### `show_all()`

This function queries the database and returns all records. It retrieves all the records from the "customers" table and displays them.

### `add_one(id, first, last, email)`

This function adds a new record to the database. It takes four parameters: `id` (integer), `first` (string), `last` (string), and `email` (string). The function inserts a new row with the provided data into the "customers" table.

### `add_many(list)`

This function adds multiple records to the database. It takes a list of tuples as a parameter. Each tuple should contain the data for a single record (id, first name, last name, email). The function inserts multiple rows into the "customers" table using the provided data.

### `delete_one(id)`

This function deletes a record from the database based on the given `id`. It removes the row with the specified `id` from the "customers" table.

### `email_lookup(email)`

This function searches for records in the database that match the given `email`. It retrieves all the rows from the "customers" table where the email column matches the provided `email` and displays the matching records.

## Example Usage

Here's an example usage of the database functions:

```python
import database

# Add a single record
database.add_one(14, "Andrew", "Nzioki", "laura@gmail.com")

# Delete records
database.delete_one("11")
database.delete_one("5")
database.delete_one("6")

# Add multiple records
stuff = [
    (4, "Brenda", "Joshua", "brenda@"),
    (5, "Josh", "Joshua", "brenda@"),
    (6, "Alex", "Joshua", "brenda@")
]
database.add_many(stuff)

# Lookup records by email
database.email_lookup("brenda@")

# Display all records
database.show_all()
```

Feel free to modify and use the functions according to your specific requirements.

Note: Uncomment the code blocks you want to execute and comment out the rest to avoid any conflicts or unintended operations.

## Conclusion

This Database Management System provides basic functionality for interacting with the SQLite database. You can use the provided functions to add, delete, lookup, and display records in the "customer.db" database.