import sqlite3
import datetime

def connect_db():
    con=sqlite3.connect('inventory.db')
    cursor=con.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory(
                      ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
                      Date TEXT,
                      ItemName TEXT,
                      ItemDescription TEXT,
                      UnitPrice REAL,
                      Quantity REAL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Username TEXT UNIQUE,
                        Password TEXT)''')
    con.commit()
    return con,cursor
def register(con,cursor):
    username=input("ENTER YOUR USERNAME : ")
    password=input("ENTER YOUR PASSWORD : ")

    try:
        cursor.execute("INSERT INTO users(username.password) VALUES?(?,?)",(username,password))
        con.commit()
        print("USER REGISTRATION SUCCESSFUL | YOU CAN LOGIN")

    except sqlite3.IntegrityError:
        print("USERNAME ALREADY EXISTS !  TRY AGAIN")

def login(cursor):
    username=input("ENTER YOUR REGISTERED USERNAME : ")
    password=input("ENTER YOUR REGISTERED PASSWORD : ")

    cursor.execute("SELECT * FROM user WHERE username=?,password=?",(username,password))
    user=cursor.fetchone()

    if user:
        print(f"WELCOME ,{username}")
        return True
    else:
        print("LOGIN FAILED ! TRY AGAIN")
        return False


def add_inventory(con,cursor):
    date=datetime.date.today()
    itemname=input("ENTER THE INVENTORY NAME : ")
    itemdescription=input("ENTER THE ITEM DESCRIPTION : ")
    unitprice=float(input("ENTER THE PRICE OF ONE UNIT : "))
    quantity=int(input("ENTER THE TOTAL UNIT : "))

    cursor.execute("INSERT INTO inventory(Date,ItemName,ItemDescription,UnitPrice,Quantity) VALUES(?,?,?,?,?)",
                   (date,itemname,itemdescription,unitprice,quantity))
    con.commit()
    print("___INVENTORY ADDED SUCCESSFULLY___")

def view_inventory(cursor):
    cursor.execute("SELECT * FROM inventory")
    inventory=cursor.fetchall()
    if not inventory:
        print("NO INVENTORY FOUND.\n")
        return
    print("ItemID | Date | ItemName | ItemDescription | UnitPrice | Quantity")
    print("_" * 60)
    for inventory in inventory:
        print(f"{inventory[0]} | {inventory[1]} | {inventory[2]} | {inventory[3]} | {inventory[4]} | {inventory[5]}")
    print("\n")

def update_inventory(con,cursor):
    view_inventory(cursor)
    inventory_id=int(input("ENTER ITEM ID TO UPDATE : "))
    itemname = input("ENTER THE NEW INVENTORY NAME : ")
    itemdescription = input("ENTER THE NEW ITEM DESCRIPTION : ")
    unitprice = float(input("ENTER THE NEW PRICE OF ONE UNIT : "))
    quantity = int(input("ENTER THE NEW TOTAL UNIT : "))

    cursor.execute("UPDATE inventory SET ItemName=?,ItemDescription=?,UnitPrice=?,Quantity=? WHERE ItemID=?",
                   (itemname,itemdescription,unitprice,quantity,inventory_id))
    con.commit()
    print("___INVENTORY UPDATED SUCCESSFULLY___")

def delete_inventory(con,cursor):
    view_inventory(cursor)
    inventory_id=int(input("ENTER THE ITEM ID TO DELETE : "))
    cursor.execute("DELETE FROM inventory WHERE ItemID=?",(inventory_id,))
    con.commit()
    print("___INVENTORY DELETED SUCCESSFULLY___")

def main():
    con, cursor = connect_db()
    while True:
       print("___LOGIN MENU___")
       print("1.REGISTER USER")
       print("2.LOGIN")
       print("3.EXIT")

       choice=input("ENTER YOUR CHOICE : ")
       if choice=='1':
           register(con,cursor)
       elif choice=='2':
           if login(cursor):
              while True:
                  print("\n___INVENTORY MANAGER___")
                  print("1. ADD INVENTORY")
                  print("2. VIEW INVENTORY")
                  print("3. UPDATE INVENTORY")
                  print("4. DELETE INVENTORY")
                  print("5.LOGOUT")
                  choice = input("ENTER YOUR CHOICE: ")
                  if choice == '1':
                      add_inventory(con, cursor)
                  elif choice == '2':
                      view_inventory(cursor)
                  elif choice == '3':
                      update_inventory(con, cursor)
                  elif choice == '4':
                      delete_inventory(con, cursor)
                  elif choice=='5':
                      print("LOGGING OUT ...")
                      break
                  else:
                       print("INVALID CHOICE")
       elif choice=='3':
           print("EXCITING GOOD BYE")
           break
       else:
           print("INVALID CHOICE")
    con.close()

main()

