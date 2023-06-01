import database 

# database.add_one(14,"andrew 1","Nzioki","laura@gmail.com")

#delete record use rowid as string

stuff=[
    (4,"Brenda","Joshua","breanda@"),
    (5,"Josh","Joshua","breanda@"),
    (6,"Alex","Joshua","breanda@")
]

database.delete_one("11")
database.delete_one("11")
# database.delete_one("5")
# database.delete_one("6")

# database.add_many(stuff)
# database.email_lookup("breanda@")
# database.show_all()
