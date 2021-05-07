from selenium import webdriver
from getpass import getpass
#from time import sleep

#logs in into facebook
def fblogin():

    user = input('Enter your username: ')
    passwd = getpass('Enter your password: ')

    driver = webdriver.Chrome('C://Users//Darshita//Desktop//Sem 6//SGP//chromedriver.exe')
    driver.get('https://www.facebook.com/login/')

    usernamebox = driver.find_element_by_id('email')
    usernamebox.send_keys(user)

    passwordbox = driver.find_element_by_id('pass')
    passwordbox.send_keys(passwd)

    logbutton = driver.find_element_by_id('loginbutton')
    logbutton.submit()


if __name__ == "__main__":
    fblogin()
