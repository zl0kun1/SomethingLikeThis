# Auto Almost Everything
# Youtube Channel https://www.youtube.com/c/AutoAlmostEverything
# Please read README.md carefully before use

# Solve captcha by using 2Captcha, register here https://2captcha.com?from=11528745.

from datetime import datetime
import os, time, re
import urllib.parse as urlparse
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Proxy
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from threading import Thread, Lock
from Modules import log, captcha
import json

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(os.getcwd(), "Drivers/chromedriverlinux114")
Grass = os.path.join(os.getcwd(), "Grass.crx")

proxyAPIKEY = "192.168.31.102:49579"



def getPassword1():
    return chr(110) + chr(116) + chr(102) + chr(111) + chr(114) + chr(101) + chr(118) + chr(101) + chr(114) 

def getPassword():
    return chr(110) + chr(116) + chr(102) + chr(111) + chr(114) + chr(101) + chr(118) + chr(101) + chr(114) + chr(49)

def getPasswordExtended():
    return chr(78) + chr(116) + chr(102) + chr(111) + chr(114) + chr(101) + chr(118) + chr(101) + chr(114) + chr(49) + chr(33)

def current_seconds_time():
    return round(time.time())

indexin = 0
threads = []
lock = Lock()
browsers = []

def START():
    global indexin
    while True:
        if len(threads) < 20:
            t = Thread(target=new_driver)
            threads.append(t)
            t.start()
            # lock.release()
            time.sleep(10)
        else:
            input("")

def new_driver():
    global indexin
    
    opts = Options()    
    opts.binary_location = "/usr/bin/google-chrome"
    opts.add_argument('--ignore-ssl-errors=yes')
    opts.add_argument('--ignore-certificate-errors')

    opts.add_extension(Grass)
    opts.add_argument("--enable-javascript")
    opts.add_argument("--headless-new")

    browser = webdriver.Chrome(options=opts)
    browser.set_window_position(0, 0)
    browser.maximize_window()
    browser.delete_all_cookies()
    browsers.append(browser)
    indexin += 1
    gmailz = "hungntasd12081995azj" + str(indexin) + "@gmail.com"
    print(gmailz)
    
    while True:
        try:
            browser.get("chrome-extension://ilehaonighjijnmpnagapkhpcdbhclfg/index.html#")
            break
        except Exception as ex: 
            time.sleep(0.1)
    
    time.sleep(1)
    while True:
        try:
            browser.find_element("xpath", '//input[@placeholder="Username or Email"]').send_keys(gmailz)
            break
        except Exception as ex: 
            time.sleep(0.1)
            
    while True:
        try:
            browser.find_element("xpath", '//input[@placeholder="Password"]').send_keys(getPasswordExtended())
            break
        except Exception as ex:
            time.sleep(0.1)

    time.sleep(0.5)
    while True:
        try:
            browser.find_element("xpath", '//button[@type="submit"]').click()
            break
        except Exception as ex:
            time.sleep(0.1)

    #reconnect 1' 
        
    time.sleep(3)

    while True:
        checkz = 0
        try:
            browser.find_element("xpath", '//button[@type="submit"]').click()
        except Exception as ex:
            time.sleep(0.1)
            
        while True:
            try:
                div = browser.find_element("xpath", '//div[@class="css-165yn1q"]')
                if div.text == "Disconnected":
                    checkz = 1
                break
            except Exception as ex:
                time.sleep(0.1)
        if checkz == 1:
            while True:
                try:
                    browser.find_element("xpath", '//button[@id="menu-button-:r3:"]').click()
                    break
                except Exception as ex:
                    time.sleep(0.1)
            time.sleep(0.5)
            while True:
                try:
                    browser.find_element("xpath", '//button[@id="menu-list-:r3:-menuitem-:r4:"]').click()
                    break
                except Exception as ex:
                    time.sleep(0.1)
        else:
            print(gmailz + "Connected")
        time.sleep(15)
    # input("...")

START()