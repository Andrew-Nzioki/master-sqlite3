import sqlite3  # import sqlite3
# create a connection || in this sqlite3 creates the databse customer in this directore


# query the database and return all records
def show_all():
    conn = sqlite3.connect("customer.db")
    cur = conn.cursor()
    cur.execute("SELECT rowid,*FROM customers")
    items = cur.fetchall()
    for item in items:
        print(item)
    # commit our command
    conn.commit()
    conn.close()

# add new record to the db


def add_one(id, first, last, email):
    conn = sqlite3.connect("customer.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO customers VALUES(?,?,?,?)",
                (id, first, last, email))
    # commit
    conn.commit()
    # close connection
    conn.close()

def add_many(list):
    conn = sqlite3.connect("customer.db")
    cur = conn.cursor()
    cur.executemany("INSERT INTO customers VALUES (?,?,?,?)",(list))

    conn.commit()
    # close connection
    conn.close()

def delete_one(id):
    conn = sqlite3.connect("customer.db")
    cur = conn.cursor()

    cur.execute("DELETE from customers WHERE id = (?)", (id,))
    conn.commit()
    # close connection
    conn.close()

#LOOKUP with where
def email_lookup(email):
    conn = sqlite3.connect("customer.db")
    cur = conn.cursor()

    cur.execute("""SELECT *FROM customers WHERE email=(?)""",(email,))
    items=cur.fetchall()

    for item in items:
        print(item)

    conn.commit()
    # close connection
    conn.close()
