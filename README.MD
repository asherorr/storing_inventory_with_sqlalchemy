PROJECT TITLE: STORE INVENTORY WITH SQLALCHEMY

---TABLE OF CONTENTS--- 
SECTION 1: GENERAL INFO 
SECTION 2: TECHNOLOGIES
SECTION 3: LICENSE

SECTION 1: GENERAL INFO

This is my fourth project in the Python TechDegree program at Treehouse. I'm so excited to share it with you!

In the models.py file, sqlalchemy is used to create a database called inventory.db

It has one table, "products", which contains an id (PKID), name, price, quantity, and date_updated column for each item.

The file inventory_app.py contains a script that enables users to interact with the database. 

First, it adds an existing CSV. Data is cleaned as each row is added to the database: item price and quantity are converted to integers, and date_updated becomes a datetime object. 

Then a menu displays. Users can search for a product, add a product, or make a backup (a new CSV file) of the database.

If users choose to add a product, their input data (strings) are also cleaned. The item price and quantity are converted to integers, and date_updated becomes a datetime object.

If the user attempts to add a product that already exists in the database, the add_product function updates the existing record with the new information entered for price, quantity, and date_updated.

SECTION 2: TECHNOLOGIES

Project is created with:

- Python
- SQLite

SECTION 3: LICENSE

Copyright (c) [2022] [Stephen Asher Orr]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.