from email import message
from tkinter import *
from tkinter import messagebox
import random
from random import choice, randint, shuffle
from twilio.rest import Client
from main import main2

#-----------------------------------sending-otp------------------------------------------------------------
otp = random.randint(1000,9999)
def login():
    user_number = phone_entry.get()
    account_sid = "accont_sid in twilio"
    auth_token = 'auth token in twilio'
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        body = f"your OTP is {otp}",
        from_ = "enter your virtual number",
        to = user_number
    )

def check():
    check_otp = int(otp_entry.get())
    if check_otp == otp:
        main2()
        phone_entry.delete(0,END)
        otp_entry.delete(0,END)

        
#---------------------------------- UI --------------------------------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

phone_number = Label(text="phone-number")
phone_number.grid(row=1, column=0)
phone_entry = Entry(width=35)
phone_entry.grid(row=1, column=1, columnspan=2)
send_otp = Button(text="send-otp", command=login)
send_otp.grid(row=2, column=1)
enter_otp = Label(text="enter-opt")
enter_otp.grid(row=3,column=0)
otp_entry = Entry(width=35)
otp_entry.grid(row=3,column=1,columnspan=2)
check_otp = Button(text="Check-otp",command=check)
check_otp.grid(row=4,column=1)
window.mainloop()
