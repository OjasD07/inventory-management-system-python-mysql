# Inventory Management System (Python + MySQL)

A console-based CRUD application to manage product inventory using Python and MySQL.

## Features
- Add new products
- Display all products
- Search product by ID
- Update product quantity and cost
- Delete product records
- Auto-calculates product value (`PValue = PQuantity * PCost`)

## Tech Stack
- Python
- MySQL
- `mysql-connector-python`

## Project Files
- `Inventory Management System.py`: Main Python application
- `schema.sql`: Database and table creation script

## Database Schema
The app uses:
- Database: `Product_Data`
- Table: `Product`
- Primary key: `PID`

Columns:
- `PID` (INT)
- `PYOM` (DATE)
- `PCategory` (VARCHAR(50))
- `PBrand` (VARCHAR(20))
- `PQuantity` (INT)
- `PCost` (INT)
- `PValue` (INT)

## Prerequisites
- Python 3.x
- MySQL Server
- Python package: `mysql-connector-python`

## Setup and Run
1. Install Python dependency:
```bash
pip install mysql-connector-python
```

2. Create the database/table:
```bash
mysql -u root -p < schema.sql
```

3. Open `Inventory Management System.py` and update MySQL credentials in:
```python
mysql.connector.connect(host="localhost", user="root", password="Your_Password", database="Product_Data")
```

4. Run the application:
```bash
python "Inventory Management System.py"
```

## Menu Options
1. Add Product  
2. Display Product  
3. Update Product  
4. Search Product  
5. Delete Product  
0. Exit

## Notes
- Year of manufacturing is prompted as `YYYYMMDD`.

## Author
Ojas Deshpande  
contact.ojasdeshpande@gmail.com