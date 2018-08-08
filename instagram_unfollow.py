from Tkinter import *
from selenium import webdriver
from time import sleep
from getpass import getpass
import tkMessageBox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def button():
    usr = u.get()
    pwd = p.get()
    unf = un.get()
    connection(usr,pwd,unf)

def connection(usr,pwd,unf):

    driver = webdriver.Chrome("C:\Python27\selenium\webdriver\Chrome\chromedriver.exe")
    driver.get('https://www.instagram.com/accounts/login/')
    driver.maximize_window()
    print('Opened Instagram')
    sleep(1)

    username_box = driver.find_element_by_name('username')
    username_box.send_keys(usr)
    print('Email id entered')
    sleep(1)

    username_box = driver.find_element_by_name('password')
    username_box.send_keys(pwd)
    print('Password entered')

    login_box = driver.find_element_by_xpath('//form/span/button[text()="Log in"]')
    login_box.click()
    sleep(5)
    print("Connected")

    sleep(5)
    element = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[1]/a')
    profile = element.get_attribute('href')
    driver.get(profile)

    followings = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
    followings.click()

    sleep(2)
    for i in range(int(unf)):
        actions = ActionChains(driver)
        actions = actions.send_keys(Keys.TAB)
        actions = actions.send_keys(Keys.TAB)
        actions = actions.send_keys(Keys.TAB)
        actions = actions.send_keys(Keys.ENTER)
        actions = actions.send_keys(Keys.TAB)
        actions = actions.send_keys(Keys.ENTER)
        actions.perform()


root = Tk()
root.title("Instagram")

u = StringVar()
p = StringVar()
un = StringVar()

label1 = Label(root, text="Username:")
label2 = Label(root, text="Password:")
label3 = Label(root, text="Number of Unfollow/s")

entry1 = Entry(root,textvariable=u)
entry2 = Entry(root,textvariable=p,show="*")
entry3 = Entry(root,textvariable=un)

button = Button(root, text="Login", command=button)

label1.grid(row=0)
entry1.grid(row=0,column=1)
label2.grid(row=1,column=0)
entry2.grid(row=1,column=1)
label3.grid(row=2,column=0)
entry3.grid(row=2,column=1)
button.grid(row=3)

root.mainloop()
