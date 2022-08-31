from models import (Base, session, Product, engine)
import datetime
import csv

def add_csv():
    with open('inventory.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(row)
            
def clean_quantity():
    
def clean_price():

def clean_date_updated():

def create_list_of_product_dictionaries():
    
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
    #app()
    add_csv()