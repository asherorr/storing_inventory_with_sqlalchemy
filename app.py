from models import (Base, session, Product, engine)
#Main menu (view a product, add a product, make a backup)
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
#data cleaning function

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    menu()