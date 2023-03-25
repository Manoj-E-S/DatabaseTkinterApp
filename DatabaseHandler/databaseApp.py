from tkinter import *
from PIL import ImageTk, Image
import sqlite3


def add():
    
    # Creates DB or connects to one
    conn = sqlite3.connect('AddressBook.db')

    # Creates a cursor to operate on the connected DB
    c = conn.cursor()

    # Executes the code passed in as a parameter
    '''
    c.execute("""
        CREATE TABLE addresses(
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            pincode integer
        )
    """)
    '''
    
    c.execute("INSERT INTO addresses VALUES (:a, :b, :c, :d, :e, :f)",
    {
        'a': f_name.get(),
        'b': l_name.get(),
        'c': address.get(),
        'd': city.get(),
        'e': state.get(),
        'f': pincode.get()
    })

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    pincode.delete(0, END)

    # Commits changes
    conn.commit()

    # Closes Connection
    conn.close()


def update(itemList):

    # Creates DB or connects to one
    conn = sqlite3.connect('AddressBook.db')

    # Creates a cursor to operate on the connected DB
    c = conn.cursor()

    # Executes the code passed in as a parameter
    
    c.execute(
    """
    UPDATE addresses
    SET
            first_name = :a,
            last_name = :b,
            address = :c,
            city = :d,
            state = :e,
            pincode = :f
    WHERE 
            oid= :id
    """,
    {
        'a': itemList[0].get(),
        'b': itemList[1].get(),
        'c': itemList[2].get(),
        'd': itemList[3].get(),
        'e': itemList[4].get(),
        'f': itemList[5].get(),
        'id': ID.get()
    })

    itemList[0].delete(0, END)
    itemList[1].delete(0, END)
    itemList[2].delete(0, END)
    itemList[3].delete(0, END)
    itemList[4].delete(0, END)
    itemList[5].delete(0, END)

    ID.delete(0, END)

    global editor
    editor.destroy()

    # Commits changes
    conn.commit()

    # Closes Connection
    conn.close()


def show():
    
    # Creates DB or connects to one
    conn = sqlite3.connect('AddressBook.db')

    # Creates a cursor to operate on the connected DB
    c = conn.cursor()

    # Executes the code passed in as a parameter
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()

    sub_win1 = Toplevel()
    sub_win1.title("Address Book Records")
    sub_win1.geometry("500x400")

    query_response = []
    for i in range(len(records)):
        print_text = f'  {i+1}. {records[i][0]} {records[i][1]}\tID: {records[i][6]}'
        query_response.append(Label(sub_win1, text=print_text, anchor=W))
        query_response[i].grid(row=i, column=0, sticky=W+E)

    # Commits changes
    conn.commit()

    # Closes Connection
    conn.close()


def delete():

    # Creates DB or connects to one
    conn = sqlite3.connect('AddressBook.db')

    # Creates a cursor to operate on the connected DB
    c = conn.cursor()

    # Executes the code passed in as a parameter
    c.execute(f"DELETE FROM addresses WHERE oid={str(ID.get())}")

    ID.delete(0, END)

    # Commits changes
    conn.commit()

    # Closes Connection
    conn.close()


def edit():

    # Creates DB or connects to one
    conn = sqlite3.connect('AddressBook.db')

    # Creates a cursor to operate on the connected DB
    c = conn.cursor()

    # Executes the code passed in as a parameter

    c.execute(f"SELECT * FROM addresses WHERE oid={str(ID.get())}")
    record = c.fetchone()

    global editor
    editor = Toplevel()
    editor.title("Editor")

    f_name_label_e = Label(editor, text="First Name: ").grid(row=0, column=0)
    f_name_e = Entry(editor, width=60)
    f_name_e.insert(0, record[0])
    f_name_e.grid(row=0, column=1)

    l_name_label_e = Label(editor, text="Last Name: ").grid(row=1, column=0)
    l_name_e = Entry(editor, width=60)
    l_name_e.insert(0, record[1])
    l_name_e.grid(row=1, column=1)

    address_label_e = Label(editor, text="Address: ").grid(row=2, column=0)
    address_e = Entry(editor, width=60)
    address_e.insert(0, record[2])
    address_e.grid(row=2, column=1)

    city_label_e = Label(editor, text="City: ").grid(row=3, column=0)
    city_e = Entry(editor, width=60)
    city_e.insert(0, record[3])
    city_e.grid(row=3, column=1)

    state_label_e = Label(editor, text="State: ").grid(row=4, column=0)
    state_e = Entry(editor, width=60)
    state_e.insert(0, record[4])
    state_e.grid(row=4, column=1)

    pincode_label_e = Label(editor, text="Pincode: ").grid(row=5, column=0)
    pincode_e = Entry(editor, width=60)
    pincode_e.insert(0, record[5])
    pincode_e.grid(row=5, column=1)

    list_to_update_fn = [f_name_e, l_name_e, address_e, city_e, state_e, pincode_e]

    update_rec_e = Button(editor, text="Update Record", command=lambda l = list_to_update_fn : update(l), padx=20, pady=20)
    update_rec_e.grid(row=6, column=0, columnspan=2, ipadx=230, pady=(10,0))


    # Commits changes
    conn.commit()

    # Closes Connection
    conn.close()


root = Tk()
root.title('Database App')

# Entries

f_name_label = Label(root, text="First Name: ").grid(row=0, column=0)
f_name = Entry(root, width=60)
f_name.grid(row=0, column=1)

l_name_label = Label(root, text="Last Name: ").grid(row=1, column=0)
l_name = Entry(root, width=60)
l_name.grid(row=1, column=1)

address_label = Label(root, text="Address: ").grid(row=2, column=0)
address = Entry(root, width=60)
address.grid(row=2, column=1)

city_label = Label(root, text="City: ").grid(row=3, column=0)
city = Entry(root, width=60)
city.grid(row=3, column=1)

state_label = Label(root, text="State: ").grid(row=4, column=0)
state = Entry(root, width=60)
state.grid(row=4, column=1)

pincode_label = Label(root, text="Pincode: ").grid(row=5, column=0)
pincode = Entry(root, width=60)
pincode.grid(row=5, column=1)

ID_label = Label(root, text="Select ID: ").grid(row=8, column=0, pady=10)
ID = Entry(root, width=60)
ID.grid(row=8, column=1, pady=10)


# Buttons
 
add_rec = Button(root, text="Add Record", command=add, padx=20, pady=20).grid(row=6, column=0, columnspan=2, ipadx=230, pady=(10,0))
show_rec = Button(root, text="Show Records", command=show, padx=20, pady=20).grid(row=7, column=0, columnspan=2, ipadx=220)
del_rec = Button(root, text="Delete Record", command=delete, padx=20, pady=20).grid(row=9, column=0, columnspan=2, ipadx=220)
edit_rec = Button(root, text="Edit Record", command=edit, padx=20, pady=20).grid(row=10, column=0, columnspan=2, ipadx=230)


root.mainloop()
