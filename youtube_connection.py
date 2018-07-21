from Tkinter import *
from selenium import webdriver
from time import sleep
from getpass import getpass

def button():
    search = s.get()
    connection(search)

def connection(search):

    driver = webdriver.Chrome("C:\Python27\selenium\webdriver\Chrome\chromedriver.exe")
    driver.get('https://www.youtube.com/')
    driver.maximize_window()
    print('Opened Youtube')
    sleep(1)

    search_box = driver.find_element_by_id('search')
    search_box.send_keys(search)
    print('Search entered')
    sleep(1)

    enter_box = driver.find_element_by_id('search-icon-legacy')
    enter_box.click()

    print("Done")
    #driver.quit()
    print("Finished")


root = Tk()
root.title("Youtube")

s = StringVar()

label1 = Label(root, text="Search:")


entry1 = Entry(root,textvariable=s)

button = Button(root, text="Search", command=button)
label1.grid(row=0)
entry1.grid(row=0,column=1)
button.grid(row=1)


root.mainloop()
