from Tkinter import *
from selenium import webdriver
from time import sleep
from getpass import getpass
import tkMessageBox

def button():
    usr = u.get()
    pwd = p.get()
    connection(usr,pwd)

def connection(usr,pwd):

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

    print("Connected")

    sleep(5)
    element = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[1]/a')
    profile = element.get_attribute('href')
    driver.get(profile)

    posts = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span')
    post = posts.get_attribute('innerHTML')
    x = post.index(">")
    post = post[x+1:]
    y = post.index("<")
    post = post[0:y]
    print "Posts: " + post

    followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    follower = followers.get_attribute('innerHTML')
    x = follower.index(">")
    follower = follower[x+1:]
    y = follower.index("<")
    follower = follower[0:y]
    print "Followers " + follower

    followings = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
    following = followings.get_attribute('innerHTML')
    x = following.index(">")
    following = following[x+1:]
    y = following.index("<")
    following = following[0:y]
    print "Followings " + following

    driver.quit()

    window = Tk()
    window.wm_withdraw()

    window.geometry("1x1+"+str(window.winfo_screenwidth()/2)+"+"+str(window.winfo_screenheight()/2))
    tkMessageBox.showinfo(title="Instagram Analytics", message="Posts: " + post + "\n Followers: " + follower + "\n Followings: " + following)


root = Tk()
root.title("Instagram")

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
