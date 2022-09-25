# MyPass
This app will generate difficult to crack password and store them in its database.

after downloading code, run it from login.py

Prerequsites:-
1) tkinter - pip install tkinter
2) sqlite3 - pip install sqlite3
3) twilio - pip install twilio

4) main.py contain main logic code.
5) show.py contain function to show data of user using tkinter treeview.
6) login.py contain code to login
inside login.py👇
7) account_sid = "accont_sid in twilio"
    auth_token = 'auth token in twilio'
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        body = f"your OTP is {otp}",
        from_ = "enter your virtual number",
        to = user_number
    )
  8)  In this code 👆 you have to create twilio account and then verify your email and mobile. After that twilio will provide you "virtual mobile number"
    "account_sid" and "auth_token" then copy these values and paste in this code as written and it will work properly


https://user-images.githubusercontent.com/65009822/192137383-69b6cc9e-beeb-409c-8e14-1845f19c51b7.mp4
![ui-3](https://user-images.githubusercontent.com/65009822/192139781-434312a8-11ae-4605-9c88-58406d432243.png)

![ui page-1](https://user-images.githubusercontent.com/65009822/192137393-b8ebea9d-0769-4013-80f6-04d8e4ac4ecf.png)
![ui page-2](https://user-images.githubusercontent.com/65009822/192137399-7c6e65fe-ccf4-4271-ac7d-41fc853a5aaf.png)
