from models import (Base, session, Product, engine)
import datetime
import csv


def menu():
    while True:
        print('''
              \rMENU
              \r1) View a Product (Enter v)
              \r2) Add a Product (Enter a)
              \r3) Make a Backup of the Database (Enter b)''')
        choice = input("\nWhat would you like to do? ")
        if choice in ['v', 'a', 'b']:
            return choice
        else:
            input('''
                  \rPlease only choose one of the options above.
                  \rEither the letter v, a or b (in lowercase.)
                  \nPress enter to try again. ''')
            

def clean_price(price_str):
    split_price = price_str.split('$')
    updated_price = split_price[1]
    price_float = float(updated_price)
    return int(price_float* 100)
    


def clean_quantity(quantity_str):
    cleaned_quantity = int(quantity_str)
    return cleaned_quantity


def clean_date_updated(date_str):
    split_date = date_str.split("/")
    month = int(split_date[0])
    day = int(split_date[1])
    year = int(split_date[2])
    return datetime.date(year, month, day)

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


def create_list_of_product_dictionaries():
    pass

def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == "v":
            #view product
            pass
        elif choice == "a":
            #add product
            pass
        elif choice == "b":
            pass
        else:
            print("Goodbye!")
            app_running = False
        
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    clean_price("$2.03")
    add_csv()
    for product in session.query(Product):
        print(product)