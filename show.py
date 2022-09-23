from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyperclip
import sqlite3


def sh():
   db = sqlite3.connect('information.db')
   cursor = db.cursor()
   sql = "SELECT * FROM users"
   cursor.execute(sql)
   rows = cursor.fetchall()
   total = cursor.rowcount
   print("Total Data Entries: "+str(total))    
   win = Tk()
   # Set the size of the tkinter window
   win.geometry("700x350")
   s = ttk.Style()
   s.theme_use('clam')
   # Add a Treeview widget
   tree = ttk.Treeview(win, column=("c1", "c2", "c3"), show='headings', height=5)
   tree.column("# 1", anchor=CENTER)
   tree.heading("# 1", text="website-name")
   tree.column("# 2", anchor=CENTER)
   tree.heading("# 2", text="email-id")
   tree.column("# 3", anchor=CENTER)
   tree.heading("# 3", text="password")
   # Insert the data in Treeview widget
   for i in rows:
    tree.insert('', 'end', values=i)

   tree.pack()
   win.mainloop()
#    for i in rows:
#     tv.insert('', 'end', values=i)
#    window.title("Password Manager")
#    window.geometry('500x500')
#    window.resizable(False, False)
   
