import sqlite3
from models import (Base, session, Product, engine)
import datetime
import csv
import time


def menu():
    while True:
        print('''
              \rMENU
              \rView a Product (Enter v)
              \rAdd a Product (Enter a)
              \rMake a Backup of the Database (Enter b)''')
        choice = input("\nWhat would you like to do? ")
        if choice in ['v', 'V', 'a', 'A', 'b', 'B']:
            return choice
        else:
            input('''
                  \rPlease only choose one of the options above.
                  \rEither the letter v, a or b.
                  \nPress enter to try again. ''')
            

def clean_price(price_str):
    try:
        if price_str[0] == "$":
            split_price = price_str.split('$')
            updated_price = split_price[1]
            price_float = float(updated_price)
            return int(price_float* 100)
        else:
            price_str_to_num = float(price_str)
            updated_price = price_str_to_num
            return int(updated_price * 100)
    except ValueError:
        input('''
              \r*** PRICE ERROR ***
              \rThe price should be a number without a currency symbol (Ex: 20.99)
              \rPress enter to try again.''')
        return
    

def clean_quantity(quantity_str):
    try:
        cleaned_quantity = int(quantity_str)
        return cleaned_quantity
    except ValueError:
        input('''
        \r*** QUANTITY ERROR ***
        \rThe date should be a number (Ex: 20).)
        \rPress enter to try again.''')
    return

def clean_date_updated(date_str):
    try:
        split_date = date_str.split("/")
        month = int(split_date[0])
        day = int(split_date[1])
        year = int(split_date[2])
        return datetime.date(year, month, day)
    except ValueError:
        input('''
        \r*** DATE ERROR ***
        \rThe date should be entered like this: 8/15/2022 (Month/Day/Year).
        \rPress enter to try again.''')
        return
        

def add_csv():
    with open('inventory.csv') as csvfile:
        data = csv.reader(csvfile)
        next(data)
        for row in data:
            product_in_db = session.query(Product).filter(Product.product_name==row[0]).one_or_none()
            if product_in_db == None:
                product_name = row[0]
                product_price = clean_price(row[1])
                product_quantity = clean_quantity(row[2])
                date_updated = clean_date_updated(row[3])
                new_product = Product(product_name=product_name, product_price=product_price, product_quantity=product_quantity, date_updated=date_updated)
                session.add(new_product)
        session.commit()

def view_product():
    import models
    list_available_ids = []
    for item in models.session.query(models.Product).filter(models.Product.product_id):
        list_available_ids.append(item.product_id)
    try:
        try:
            user_search_choice = int(input("Enter the ID of the product you'd like to look up: "))
        except ValueError:
            raise ValueError('''
                            \r***PRODUCT ID ERROR***
                            \rPlease enter only a number.''')
        if user_search_choice not in list_available_ids:
            raise ValueError('''
                            \r***PRODUCT ID ERROR***
                            \rThat product ID does not exist in the database.
                            \rPlease try again.''')
    except ValueError as err:
        print(err)
    else:
        for item in models.session.query(models.Product).filter(models.Product.product_id == user_search_choice):
            print(f'''\rProduct found! 
                  \r{item}''')
            time.sleep(2)
            return
        
        
def add_product():
    new_product_name = input("Product name: ")
    price_error = True
    while price_error:
        product_price = input("Product price: ")
        product_price = clean_price(product_price)
        if type(product_price) == int:
            price_error = False
    product_quantity_error = True
    while product_quantity_error:
        product_quantity = input("Product quantity: ")
        product_quantity = clean_quantity(product_quantity)
        if type(product_quantity) == int:
            product_quantity_error = False
    date_updated_error = True
    while date_updated_error:
        date_updated = input(
            "Date updated (Ex: 10/11/2012) (Month/Day/Year): ")
        date_updated = clean_date_updated(date_updated)
        if type(date_updated) == datetime.date:
            date_updated_error = False
    #query database to find duplicate record if there is one [DONE]
    import models
    duplicate_item = models.session.query(Product).filter(Product.product_name==new_product_name).first()
    if duplicate_item is not None:
    #if duplicate product name exists in the database
        #update the existing record with price, quantity, and date_updated.
        duplicate_item.product_price = product_price
        duplicate_item.product_quantity = product_quantity
        duplicate_item.date_published = date_updated
        session.commit()
        print(f'''*** MESSAGE ***
              \r{duplicate_item.product_name} already exists in your database.
              \rInstead of adding a duplicate to the database, the existing information for {duplicate_item.product_name} was updated.''')
        time.sleep(1.5)
        return
    #else, add the brand new product.
    else:
        new_product = Product(product_name=new_product_name, product_price=product_price,
                                product_quantity=product_quantity, date_updated=date_updated)
        session.add(new_product)
        session.commit()
        print("Product added!")
        time.sleep(1.5)
        return
    
def export_database_to_csv():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute("select * from products;")
    with open("backupfile.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
    conn.close()
    print('''
          \rDatabase successfully backed up!
          \rIt should be saved as backupfile.csv''')
    time.sleep(1.5)
    

def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == "v":
            view_product()
        elif choice == "a":
            add_product()
        elif choice == "b":
            export_database_to_csv()
        else:
            print("Goodbye!")
            app_running = False
        
        
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    add_csv()
    app()