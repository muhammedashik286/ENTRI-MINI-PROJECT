# Inventory Management System

This Python script implements a simple inventory management system using SQLite for data storage. It allows users to register, log in, and manage inventory items.

## Prerequisites

-   Python 3.10
-   SQLite3 (usually comes pre-installed with Python)

## How to Run

1.  **Save the code:** Save the provided Python code as a '.py' file (e.g., 'inventory_manager.py').
2.  **Run the script:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script using the following command:

    '''bash
    python inventory_manager.py
    '''

## Functionality

### User Management

-   **Register User:** Allows new users to create an account with a unique username and password.
-   **Login:** Authenticates existing users using their username and password.

### Inventory Management

-   **Add Inventory:** Adds new inventory items with details such as date, item name, description, unit price, and quantity.
-   **View Inventory:** Displays a list of all inventory items with their details.
-   **Update Inventory:** Allows users to modify the details of an existing inventory item.
-   **Delete Inventory:** Removes an inventory item from the database.
-   **Logout:** Returns the user to the login menu.

## Code Explanation

### Database Setup

-   The script uses 'sqlite3' to create and manage an SQLite database named 'inventory.db'.
-   Two tables are created:
    -   'inventory': Stores inventory items with columns for ItemID, Date, ItemName, ItemDescription, UnitPrice, and Quantity.
    -   'users': Stores user credentials with columns for UserID, Username, and Password.
-   The 'connect_db()' function establishes a connection to the database and creates the tables if they don't exist.

### User Registration and Login

-   The 'register()' function prompts the user for a username and password and inserts the data into the 'users' table. It handles 'sqlite3.IntegrityError' to prevent duplicate usernames.
-   The 'login()' function verifies the user's credentials against the 'users' table and returns 'True' if the login is successful, 'False' otherwise.

### Inventory Operations

-   The 'add_inventory()' function takes input from the user and inserts a new inventory item into the 'inventory' table.
-   The 'view_inventory()' function retrieves all inventory items from the 'inventory' table and displays them in a formatted table.
-   The 'update_inventory()' function prompts the user for an ItemID and new inventory details, and updates the corresponding row in the 'inventory' table.
-   The 'delete_inventory()' function prompts the user for an ItemID and removes the corresponding row from the 'inventory' table.

### Main Menu

-   The 'main()' function provides a menu-driven interface for user interaction.
-   It handles user input and calls the appropriate functions for registration, login, and inventory management.

## Example Usage

1.  Run the script.
2.  Choose "1. REGISTER USER" to create a new account.
3.  Choose "2. LOGIN" to log in with your credentials.
4.  Once logged in, you can add, view, update, and delete inventory items.
5.  Choose "5.LOGOUT" to return to the login screen.
6.  Choose "3.EXIT" to close the application.

## Database Structure

### 'inventory' Table

| Column          | Data Type | Description                  |
| --------------- | --------- | ---------------------------- |
| ItemID          | INTEGER   | Primary key, auto-increment  |
| Date            | TEXT      | Date of inventory entry      |
| ItemName        | TEXT      | Name of the item             |
| ItemDescription | TEXT      | Description of the item      |
| UnitPrice       | REAL      | Price per unit               |
| Quantity        | REAL      | Total quantity of the item   |

### 'users' Table

| Column   | Data Type | Description                  |
| -------- | --------- | ---------------------------- |
| UserID   | INTEGER   | Primary key, auto-increment  |
| Username | TEXT      | Unique username              |
| Password | TEXT      | User's password              |