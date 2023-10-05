import sqlite3


def show_all():
    con = sqlite3.connect("customer.db")
    c = con.cursor()
    c.execute('select rowid, * from customers')
    items = c.fetchall()
    for item in items:
        print(item)
    
    con.commit()
    con.close()

def add_one(first_name, last_name, Email):
    con = sqlite3.connect('customer.db')
    c=con.cursor()
    c.execute('insert into customers values(?,?,?)',(first_name, last_name, Email))
    
    con.commit()
    con.close()
def add_many(List):
    con = sqlite3.connect('customer.db')
    c=con.cursor()
    c.executemany('insert into customers values(?,?,?)',(List))
    
    con.commit()
    con.close()

def delete_one(id):
    con = sqlite3.connect('customer.db')
    c=con.cursor()
    c.execute('delete from customers where rowid =(?)',id)
    
    con.commit()
    con.close()

def email_lookup(email):
    con = sqlite3.connect('customer.db')
    c=con.cursor()
    c.execute('select * from customers where email=(?)',(email,))
    items = c.fetchall()
    for item in items:
        print(item)
    con.commit()
    con.close()