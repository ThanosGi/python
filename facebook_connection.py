from Tkinter import *
from selenium import webdriver
from time import sleep
from getpass import getpass

def button():
    usr = u.get()
    pwd = p.get()
    connection(usr,pwd)

def connection(usr,pwd):

    driver = webdriver.Chrome("C:\Python27\selenium\webdriver\Chrome\chromedriver.exe")
    driver.get('https://www.facebook.com')
    driver.maximize_window()
    print('Opened Facebook')
    sleep(1)

    username_box = driver.find_element_by_id('email')
    username_box.send_keys(usr)
    print('Email id entered')
    sleep(1)

    username_box = driver.find_element_by_id('pass')
    username_box.send_keys(pwd)
    print('Password entered')

    login_box = driver.find_element_by_id('loginbutton')
    login_box.click()

    print("Done")


root = Tk()
root.title("Facebook")

u = StringVar()
p = StringVar()

label1 = Label(root, text="Username:")
label2 = Label(root, text="Password:")


entry1 = Entry(root,textvariable=u)

entry2 = Entry(root,textvariable=p,show="*")

button = Button(root, text="Login", command=button)
label1.grid(row=0)
entry1.grid(row=0,column=1)
label2.grid(row=1,column=0)
entry2.grid(row=1,column=1)
button.grid(row=2)


root.mainloop()
