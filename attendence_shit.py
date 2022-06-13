from selenium import webdriver
import os
import time
from random import randint
from dotenv import load_dotenv


load_dotenv()

driver = webdriver.PhantomJS()
EMPLOYEEID = os.environ.get('EMPLOYEEID')
PASSWORD = os.environ.get('PASSWORD')
COMPANY = os.environ.get('COMPANY')

homepage_url = "https://hrcloud.myadrenalin.com/adrenalin/"

def login_shit():
    driver.find_element_by_id('txtID').send_keys(EMPLOYEEID)
    driver.find_element_by_id("txtPwd").send_keys(PASSWORD)
    driver.find_element_by_id("txtCompName").send_keys(COMPANY)
    print("Loggged in !")
    driver.save_screenshot("login_page.png")
    driver.find_element_by_id("lblLogin").click()
    time.sleep(1)

def sign_in_shit():
    driver.save_screenshot("signin_shit.png")
    try: 
        driver.find_element_by_id("btnOK").click()
        print("Hurray!!! , You got signed in :)  O3 <3! \nHave Nice Day")
        time.sleep(2)
    except:
        print("Oops! looks like you already signed in or something went wrong, (Maintainace may be required)")
    

def sign_out_shit():
    driver.execute_script("window.top.location.href='https://hrcloud.myadrenalin.com/Adrenalin/iEngine/OkCancelSignOut.aspx';")
    time.sleep(2)
    print("Hurray!!! , You got signed out :) \n Have fun")
    driver.save_screenshot("signout_shit.png")


def main():
    READY_TO_GO = 0
    #  tm_wday [ 0 ,.., 6] : [ mon, ... sunday]
    current_time = time.time()
    week_day = time.localtime(current_time).tm_wday
    hour_of_day = time.localtime(current_time).tm_hour
    min_of_hour = time.localtime(current_time).tm_min

    if week_day >= 0 and week_day < 5:   # filter freaking weekends
        if hour_of_day == 9 or hour_of_day >= 18:
            magic_mins = randint(3,9)
            print(magic_mins*59)
            time.sleep(magic_mins*59)
            READY_TO_GO = 1

    print("READY_TO_GO : " + str(READY_TO_GO))
    if READY_TO_GO:
        driver.get(homepage_url)
        login_shit()
        if hour_of_day == 9:
            sign_in_shit()
        elif hour_of_day >= 19:
            sign_out_shit()
    else:
        print("Time might not be correct, current time in hrs : " + str(time.localtime(current_time).tm_hour))
            

    driver.quit()


main()
