import sqlite3


def create_Table():
    con = sqlite3.connect("Item.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    con.commit()
    con.close()


def insert(item, quantity, price):
    con = sqlite3.connect("Item.db")
    cur = con.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
    con.commit()
    con.close()
    

def View():
    con = sqlite3.connect("Item.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    con.close()

    return rows


def delete(item):
    con = sqlite3.connect("Item.db")
    cur = con.cursor()
    cur.execute("DELETE FROM store WHERE price = ?", (item, ))
    con.commit()
    con.close()


def Update(quantity, item):
    con = sqlite3.connect("Item.db")
    cur = con.cursor()
    cur.execute("UPDATE store SET quantity = ? WHERE item = ? ", (quantity, item))
    con.commit()
    con.close()


if __name__=="__main__":
    create_Table()
    #insert("White Wine", 1, 10)
    #insert("Red Wine", 2, 20)
    #insert("Blue Wine", 3, 30)
    #insert("Purple Wine", 4, 40)
    #insert("Orange Wine", 5, 50)
    #insert("Yellow Wine", 6, 60)
    #delete(20)
    Update(300000, "Blue Wine")
    print(View())