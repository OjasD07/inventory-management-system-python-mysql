# Inventory Management System, By Ojas Deshpande
# Github:https://github.com/ojasd07/
# Repository Link (Github):https://github.com/OjasD07/inventory-management-system-python-mysql


# This is a simple Inventory Management System that allows the user to Add, Display, Update, Search and Remove Product's Record.
# The Product's Record is stored in a MySQL Database. The user can perform all the operations on the Product's Record using this system.
# Note: The user needs to have MySQL installed and a database named "Product_Data" with a table named "Product" to run this system. The user also needs to update the MySQL connection details in the code (host, user, password) before running the system.
# The code is written in Python and uses the mysql.connector library to connect to the MySQL database. The code is structured in a way that each operation (Add, Display, Update, Search, Remove) is implemented as a separate function. The menu function is used to display the menu and to call the appropriate function based on the user's choice.
# The code is simple and easy to understand, and it can be used as a basic template for an Inventory Management System. The user can further enhance the system by adding more features such as sorting, filtering, and generating reports based on the Product's Record.
# The user can also add error handling to the code to handle exceptions that may occur during database operations. Overall, this Inventory Management System provides a basic framework for managing Product's Record in a MySQL database using Python.

# The Product's Record consists of the following details:
# 1. Product ID (PID)  
# 2. Year of Manufacturing (PYOM)
# 3. Product Category (PCategory)           
# 4. Product Brand (PBrand)
# 5. Product Quantity (PQuantity)
# 6. Product Cost (PCost)
# 7. Product Value (PValue) [Calculated as PQuantity * PCost]

# The user can perform the following operations on the Product's Record:
# 1. Add Product: The user can add a new Product's Record to the database. The user will be prompted to enter the Product's details. The system will check if the Product ID already exists in the database. If it does, the system will display a message and will not add the Product's Record. If it does not, the system will add the Product's Record to the database and will display a success message.
# 2. Display Product: The user can display all the Product's Record from the database. The system will display all the Product's Record in a formatted manner. If there are no Product's Record in the database, the system will display a message.
# 3. Update Product: The user can update the Product's Record in the database. The user will be prompted to enter the Product ID. The system will check if the Product ID exists in the database. If it does, the user will be prompted to enter the new Product's Quantity and Cost. The system will update the Product's Record in the database and will display a success message. If it does not, the system will display a message.
# 4. Search Product: The user can search for a Product's Record in the database. The user will be prompted to enter the Product ID. The system will check if the Product ID exists in the database. If it does, the system will display the Product's Record in a formatted manner. If it does not, the system will display a message.
# 5. Remove Product: The user can remove a Product's Record from the database. The user will be prompted to enter the Product ID. The system will check if the Product ID exists in the database. If it does, the system will remove the Product's Record from the database and will display a success message. If it does not, the system will display a message. 
# The user can exit the system by entering 0 in the menu.



import mysql.connector
connection = mysql.connector.connect(host="localhost", user="root",password="Your_Password", database="Product_Data")

# Function to Add Product
def Add_Product():
    PID = input ("\nEnter Product's ID:")
    # Checking if Product ID exists
    if(check_Product(PID) == False) :
        PCategory = input("Enter Product's Category:")
        PBrand = input("Enter Product's Brand:")
        PYOM = int(input("Enter Product's Year of Manufacturing [YYYYMMDD]:"))
        PQuantity = int(input("Enter Product's Quantity:"))
        PCost = int(input("Enter Product's Cost:"))
        PValue = PQuantity * PCost
        data = (PID, PYOM, PCategory,PBrand, PQuantity, PCost, PValue)
        # Inserting Product Details into the Product_Data (Product) Table
        sql = 'insert into Product values(%s,%s,%s,%s,%s,%s,%s)'
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        print("\nSuccessfully Added Product.")
        press = input("\nPress Any Key To Continue.")
        menu()
    else:
        print("\nProduct ID Already Exists!")
        press = input ("\nPress Any Key To Continue.")
        menu()

# Function to Check if Product with given PID exists
def check_Product(Product_id):
    sql = 'select * from Product where PID = %s'
    cursor = connection.cursor(buffered=True)
    data = (Product_id,)
    cursor.execute(sql, data)
    rows = cursor.rowcount
    if rows == 1:
        return True
    else:
        return False

# Function to Display_Product
def Display_Product():
    print("\nDisplay Product's Record")
    # query to select all rows from Product_Data (Product) Table
    sql = 'select * from Product'
    cursor = connection.cursor()
    cursor.execute(sql)
    # Fetching all details of all the Products
    details = cursor.fetchall()
    if not details:
        print("\nProduct Record does not Exist!")
    else:
        for i in details:
            print("\nProduct's Id: ", i[0])
            print("Product's Year of manufacturing: ", i[1])
            print("Product's Category: ", i[2])
            print("Products Brand: ", i[3])
            print("Product's Quantity: ", i[4])
            print("Product's Cost: ", i[5])
            print("Product's Value: ", i[6])

    press = input("\nPress Any Key To Continue.")
    menu()

        

# Function to Update_Product
def Update_Product():
    print("\nUpdate Product's Record")
    PID = input("\nEnter Product's ID: ")
    # checking if Product ID exists
    if (check_Product(PID) == True):
        PQuantity = int(input("Enter Product's Quantity:"))
        PCost = int(input("Enter Product's Cost:"))
        PValue = PQuantity * PCost
        # Updating Product details in Product Table
        sql = 'UPDATE Product SET PQuantity= %s, PCost = %s, PValue = %s WHERE PID = %s'
        data = (PQuantity, PCost, PValue, PID)
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        print("\nUpdated Product's Record")
        press = input("\nPress Any Key To Continue.")
        menu()
    else :
        print("\nProduct Record does not exist!")
        press = input("\nPress Any Key To Continue.")
        menu()

# Function to Remove_Product
def Remove_Product():
    print("\nRemove Product's Record")
    PID = input("\nEnter Product's ID:")
    # checking if Product ID exists
    if (check_Product(PID) == False):
        print("\nProduct's Record does not exist!")
        press = input("\nPress Any Key To Continue.")
        menu()
    else:
        # query to delete Product from Product table
        sql = 'delete from Product where PID = %s'
        data = (PID,)#Converting it into tuple.
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        print("\nProduct Removed!")
        press = input("\nPress Any key To Continue.")
        menu()

# Function to Search_Product
def Search_Product():
    print("\nSearch Product's Record")
    PID = input("\nEnter Product ID: ")
    # checking if Product ID exists
    if (check_Product(PID) == True):
    # query to search Product from Product table
        sql = 'select * from Product where PID = %s'
        data = (PID,)#Converting it into tuple.
        cursor = connection.cursor()
        cursor.execute(sql, data)
        # fetching all details of all the products
        details = cursor.fetchall()
        for i in details:
            print("\nProduct's Id: ", i[0])
            print("Product's Year of manufacturing: ", i[1])
            print("Product's Category: ", i[2])
            print("Products Brand: ",i[3])
            print("Product's Quantity: ", i[4])
            print("Product's Cost: ", i[5])
            print("Product's Value: ", i[6])
            press = input("\nPress Any key To Continue.")
            menu()
    else:
        print("\nProduct Record does not Exist!")
        press = input("\nPress Any Key To Continue.")
        menu()


# Menu function to display menu
def menu():
    print("************************************")
    print("Inventory Management System")
    print("************************************")
    print("    1. Add Product")
    print("    2. Display Product")
    print("    3. Update Product")
    print("    4. Search Product")
    print("    5. Delete Product")
    print("    0. Exit")
    print("************************************")
    print("Choice Options: [1/2/3/4/5/0]:")
    print("************************************")

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        Add_Product()
    elif ch == 2:
        Display_Product()
    elif ch == 3:
        Update_Product()
    elif ch == 4:
        Search_Product()
    elif ch == 5:
        Remove_Product()
    elif ch == 0:
        exit()
    else:
        print("\nInvalid Choice!")
        press = input("\nPress Any key To Continue.")
        menu()

menu()
