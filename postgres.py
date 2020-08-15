import psycopg2


def create_table():
    con = psycopg2.connect("dbname = 'check_python' password = '123' host = 'localhost' user= 'postgres' ")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS name (item TEXT, quantity INTEGER, price REAL)")
    con.commit()
    con.close()


def insert(item, quantity, price):
    con = psycopg2.connect("dbname = 'check_python' password = '123' host = 'localhost' user= 'postgres' ")
    cur = con.cursor()
    cur.execute("INSERT INTO name VALUES(%s,%s,%s)", (item, quantity, price))
    con.commit()
    con.close()


def delete(item):
    con = psycopg2.connect("dbname = 'check_python' password = '123' host = 'localhost' user= 'postgres' ")
    cur = con.cursor()
    cur.execute("DELETE FROM name WHERE item = %s", (item,))
    con.commit()
    con.close()

def update(i,j):
    con = psycopg2.connect("dbname = 'check_python' password = '123' host = 'localhost' user= 'postgres' ")
    cur = con.cursor()
    cur.execute("UPDATE name SET item = %s WHERE item = %s", (j,i))
    con.commit()
    con.close()


if __name__=="__main__":
    create_table()
    #insert("Red Wine", 100, 10000)
    #insert("White Wine", 100, 10000)
    #insert("Purple Wine", 100, 10000)
    #insert("Orange Wine", 100, 10000)
    #insert("Grey Wine", 100, 10000)
    #insert("Blue Wine", 100, 10000)
    #delete("White Wine")
    update("Purple Wine", "Changed")