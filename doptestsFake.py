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
import tkinter as tk
from Modules import log, captcha
import json


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(os.getcwd(), "Drivers/chromedriverlinux114")
Metamask = os.path.join(os.getcwd(), "MetaMaskz.crx")

proxyAPIKEY = "192.168.31.102:49579"

opts = Options()
opts.binary_location = "/usr/bin/google-chrome"
opts.add_extension(Metamask)
opts.add_argument("--enable-javascript")
opts.add_argument("--headless-new")

def getPassword1():
    return chr(110) + chr(116) + chr(102) + chr(111) + chr(114) + chr(101) + chr(118) + chr(101) + chr(114) 

def getPassword():
    return chr(110) + chr(116) + chr(102) + chr(111) + chr(114) + chr(101) + chr(118) + chr(101) + chr(114) + chr(49)

def current_seconds_time():
    return round(time.time())
    


def START():
    root = tk.Tk()
    root.withdraw()  # to hide the window
    indexin = 0
    while True:
        browser = webdriver.Chrome(options=opts)
        browser.set_window_position(0, 0)
        browser.maximize_window()
        browser.delete_all_cookies()
        number_tabs = 5
        while True:
            try:
                if len(browser.window_handles) == 2:
                    browser.switch_to.window(browser.window_handles[1])
                    break
            except Exception as ex:
                time.sleep(0.1)
        time.sleep(1)

        checkE = 0
        spazz = ""
        seed_phase_str = ""
        while True:
            try:
                if checkE > 200:
                    break
                browser.find_element("xpath", '//input[@class="check-box onboarding__terms-checkbox far fa-square"]').click()
                break
            except Exception as ex:
                checkE += 1
                time.sleep(0.1)
        
        if checkE < 200:
            checkE = 0
            while True:
                try:
                    if checkE > 200:
                        break
                    browser.find_element("xpath", '//button[@class="button btn--rounded btn-primary"]').click()
                    # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                    break
                except Exception as ex:
                    checkE += 1
                    time.sleep(0.1)
            
            if checkE > 200:
                browser.quit()
                continue
                
            checkE = 0
            while True:
                try:
                    if checkE > 200:
                        break
                    browser.find_element("xpath", '//button[@class="button btn--rounded btn-primary btn--large"]').click()
                    # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                    break
                except Exception as ex:
                    checkE += 1
                    time.sleep(0.1)

            if checkE > 200:
                browser.quit()
                continue
                
            checkE = 0
            while True:
                try:
                    if checkE > 200:
                        break
                    browser.find_element("xpath", '//input[@data-testid="create-password-new"]').send_keys(getPassword1())
                    # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                    break
                except Exception as ex:
                    checkE += 1
                    time.sleep(0.1)

            if checkE > 200:
                browser.quit()
                continue
                
            checkE = 0
            while True:
                try:
                    if checkE > 200:
                        break
                    browser.find_element("xpath", '//input[@data-testid="create-password-confirm"]').send_keys(getPassword1())
                    # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                    break
                except Exception as ex:
                    checkE += 1
                    time.sleep(0.1)
            if checkE > 200:
                browser.quit()
                continue
                
            checkE = 0
            while True:
                try:
                    if checkE > 200:
                        break
                    browser.find_element("xpath", '//input[@data-testid="create-password-terms"]').click()
                    # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                    break
                except Exception as ex:
                    checkE += 1
                    time.sleep(0.1)
                    
            if checkE > 200:
                browser.quit()
                continue
                
            checkE = 0
            while True:
                try:
                    if checkE > 200:
                        break
                    browser.find_element("xpath", '//button[@class="button btn--rounded btn-primary btn--large create-password__form--submit-button"]').click()
                    # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                    break
                except Exception as ex:
                    checkE += 1
                    time.sleep(0.1)
            if checkE > 200:
                browser.quit()
                continue
                
            checkE = 0
            while True:
                try:
                    if checkE > 200:
                        break
                    browser.find_element("xpath", '//button[@data-testid="secure-wallet-later"]').click()
                    # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                    break
                except Exception as ex:
                    checkE += 1
                    time.sleep(0.1)
            if checkE > 200:
                browser.quit()
                continue
                
            checkE = 0
            while True:
                try:
                    if checkE > 200:
                        break
                    browser.find_element("xpath", '//input[@class="check-box skip-srp-backup-popover__checkbox far fa-square"]').click()
                    # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                    break
                except Exception as ex:
                    checkE += 1
                    time.sleep(0.1)
                    
            if checkE > 200:
                browser.quit()
                continue
                
            checkE = 0
            while True:
                try:
                    if checkE > 200:
                        break
                    browser.find_element("xpath", '//button[@data-testid="skip-srp-backup"]').click()
                    # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                    break
                except Exception as ex:
                    checkE += 1
                    time.sleep(0.1)
            if checkE > 200:
                browser.quit()
                continue
                
            checkE = 0

            while True:
                try:
                    if checkE > 200:
                        break
                    browser.find_element("xpath", '//button[@data-testid="onboarding-complete-done"]').click()
                    # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                    break
                except Exception as ex:
                    checkE += 1
                    time.sleep(0.1)

            if checkE < 200:
                checkE = 0
                while True:
                    try:
                        if checkE > 200:
                            break
                        browser.find_element("xpath", '//button[@data-testid="pin-extension-next"]').click()
                        # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                        break
                    except Exception as ex:
                        checkE += 1
                        time.sleep(0.1)

                if checkE > 200:
                    browser.quit()
                    continue
                    
                checkE = 0
                while True:
                    try:
                        if checkE > 200:
                            break
                        browser.find_element("xpath", '//button[@data-testid="pin-extension-done"]').click()
                        # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                        break
                    except Exception as ex:
                        checkE += 1
                        time.sleep(0.1)

                if checkE > 200:
                    browser.quit()
                    continue
                    
                checkE = 0
                while True:
                    try:
                        if checkE > 200:
                            break
                        browser.find_element("xpath", '//button[@data-testid="popover-close"]').click()
                        # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                        break
                    except Exception as ex:
                        checkE += 1
                        time.sleep(0.1)

                if checkE > 200:
                    browser.quit()
                    continue
                    
                checkE = 0
                while True:
                    try:
                        if checkE > 200:
                            break
                        browser.find_element("xpath", '//button[@data-testid="account-menu-icon"]').click()
                        # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                        break
                    except Exception as ex:
                        checkE += 1
                        time.sleep(0.1)
                        
                if checkE > 200:
                    browser.quit()
                    continue
                    
                checkE = 0
                while True:
                    try:
                        if checkE > 200:
                            break
                        browser.find_element("xpath", '//div[@class="mm-box mm-box--margin-bottom-4"][2]/button/span').click()
                        break
                    except Exception as ex:
                        checkE += 1
                        time.sleep(0.1)

                if checkE > 200:
                    browser.quit()
                    continue
                    
                checkE = 0
                while True:
                    try:
                        if checkE > 200:
                            break
                        browser.find_element("xpath", '//input[@id="private-key-box"]').send_keys("19190687f93a2e043acdcd766dc98d0f5da340fe9bbe1d327a86fe64b3735c18")
                        # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                        break
                    except Exception as ex:
                        checkE += 1
                        time.sleep(0.1)

                if checkE < 200:
                    checkE = 0
                    while True:
                        try:
                            if checkE > 200:
                                break
                            browser.find_element("xpath", '//button[@data-testid="import-account-confirm-button"]').click()
                            # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                            break
                        except Exception as ex:
                            checkE += 1
                            time.sleep(0.1)

                    if checkE > 200:
                        browser.quit()
                        continue
                        
                    checkE = 0
            # login twitter
                    browser.switch_to.window(browser.window_handles[0])
                    # emailz = listDiscord[indexin]
                    emailz = "hungnt1208aaa" + str(indexin) + "@gmail.com"
                    while True:
                        try:
                            browser.get("https://doptest.dop.org/id=aK6C8HH")
                            break
                        except:
                            time.sleep(0.1)
                            
                    time.sleep(0.5)
                    while True:
                        try:
                            if checkE > 200:
                                break
                            browser.find_element("xpath", '//div[@class="content"]').click()
                            break
                        except Exception as ex:
                            checkE += 1
                            time.sleep(0.1)
                            
                    if checkE > 200:
                        browser.quit()
                        continue
                        
                    checkE = 0
                    while True:
                        try:
                            if checkE > 200:
                                break
                            browser.find_element("xpath", '//input[@placeholder="Enter your email address"]').send_keys(emailz)
                            break
                        except:
                            checkE += 1
                            time.sleep(0.1)
                    time.sleep(0.5)
                    if checkE > 200:
                        browser.quit()
                        continue
                        
                    checkE = 0
                    while True:
                        try:
                            if checkE > 200:
                                break
                            browser.find_element("xpath", '//button[@type="submit"]').click()
                            break
                        except:
                            checkE += 1
                            time.sleep(0.1)

                    time.sleep(0.5)
                    if checkE > 200:
                        browser.quit()
                        continue
                        
                    checkE = 0
                    while True:
                        try:
                            if checkE > 200:
                                break
                            browser.find_element("xpath", '//button[@class="common-btnone"]').click()
                            break
                        except:
                            checkE += 1
                            time.sleep(0.1)
                    
                    if checkE > 200:
                        browser.quit()
                        continue
                        
                    checkE = 0
                    while True:
                        try:
                            if checkE > 200:
                                break
                            browser.find_element("xpath", '//input[@placeholder="Enter new password"]').send_keys(getPassword1())
                            break
                        except:
                            checkE += 1
                            time.sleep(0.1)

                    if checkE > 200:
                        browser.quit()
                        continue
                        
                    checkE = 0
                    while True:
                        try:
                            if checkE > 200:
                                break
                            browser.find_element("xpath", '//input[@placeholder="Confirm new password"]').send_keys(getPassword1())
                            break
                        except:
                            checkE += 1
                            time.sleep(0.1)
                    time.sleep(0.5)
                    if checkE > 200:
                        browser.quit()
                        continue
                        
                    checkE = 0
                    while True:
                        try:
                            if checkE > 200:
                                break
                            browser.find_element("xpath", '//button[@type="submit"]').click()
                            break
                        except:
                            checkE += 1
                            time.sleep(0.1)
                    time.sleep(0.5)
                    if checkE > 200:
                        browser.quit()
                        continue
                        
                    checkE = 0
                    seed_phase = []
                    while True:
                        try:
                            ps = browser.find_elements("xpath", '//div[@class="single-phrase"]/p')

                            for p in ps:
                                seed_phase.append(p.text)
                            break
                        except Exception as ex:
                            time.sleep(0.1)

                    seed_phase_str = ""
                    for i in range(len(seed_phase)):
                        if i == 0:
                            seed_phase_str = seed_phase[i]
                        else:
                            seed_phase_str = seed_phase_str + " " + seed_phase[i]
                    
                    time.sleep(0.5)
                    while True:
                        try:
                            if checkE > 200:
                                break
                            browser.find_element("xpath", '//button[@class="btn-verify w-100"]').click()
                            break
                        except Exception as ex:
                            checkE += 1
                            time.sleep(0.1)
                    
                    if checkE > 200:
                        browser.quit()
                        continue
                        
                    checkE = 0
                    time.sleep(1.5)
                    for i in range(len(seed_phase)):
                        seed = seed_phase[i]
                        while True:
                            try:
                                buttons = browser.find_elements("xpath", '//button[@class="single-phrase"]')
                                
                                for butt in buttons:
                                    if seed == butt.text:
                                        butt.click()
                                        break

                                break
                            except Exception as ex:
                                time.sleep(0.1)
                    
                    time.sleep(0.5)
                    while True:
                        try:
                            if checkE > 200:
                                break
                            browser.find_element("xpath", '//button[@class="btn-verify done-btn w-100"]').click()
                            break
                        except:
                            checkE += 1
                            time.sleep(0.1)

                    if checkE > 200:
                        browser.quit()
                        continue
                        
                    checkE = 0
                    time.sleep(0.5)
                    while True:
                        try:
                            if checkE > 200:
                                break
                            browser.find_element("xpath", '//button[@class="btn-verify done-btn w-100"]').click()
                            break
                        except:
                            checkE += 1
                            time.sleep(0.1)
                    
                    if checkE > 200:
                        browser.quit()
                        continue
                        
                    checkE = 0
                    time.sleep(0.5)
                    while True:
                        try:
                            if checkE > 200:
                                break
                            span = browser.find_element("xpath", '//span[@class="gsvsvcvst"]')
                            spazz = span.text
                            break
                        except:
                            checkE += 1
                            time.sleep(0.1)

                    if checkE > 200:
                        browser.quit()
                        continue
                        
                    checkE = 0
                    time.sleep(0.5)
                    while True:
                        try:
                            if checkE > 200:
                                break
                            browser.find_element("xpath", '//button[@class="btn-verify w-100"]').click()
                            break
                        except:
                            checkE += 1
                            time.sleep(0.1)

                    if checkE > 200:
                        browser.quit()
                        continue
                        
                    checkE = 0
                    time.sleep(0.5)
                    while True:
                        try:
                            if checkE > 200:
                                break
                            browser.find_element("xpath", '//input[@placeholder="********"]').send_keys(getPassword1())
                            break
                        except:
                            checkE += 1
                            time.sleep(0.1)

                    if checkE > 200:
                        browser.quit()
                        continue
                        
                    checkE = 0
                    time.sleep(0.5)
                    while True:
                        try:
                            if checkE > 200:
                                break
                            browser.find_element("xpath", '//button[@type="submit"]').click()
                            break
                        except:
                            checkE += 1
                            time.sleep(0.1)

                    if checkE > 200:
                        browser.quit()
                        continue
                        
                    checkE = 0
                    time.sleep(0.5)
                    while True:
                        try:
                            if checkE > 200:
                                break
                            browser.find_element("xpath", '//button[@class="continuebutton"]').click()
                            break
                        except:
                            checkE += 1
                            time.sleep(0.1)
                    if checkE > 200:
                        browser.quit()
                        continue
                        
                    checkE = 0
                    time.sleep(0.5)
                    while True:
                        try:
                            if checkE > 200:
                                break
                            browser.find_element("xpath", '//button[@class="btn-verifyss my-2 mt-3 metamask "]').click()
                            break
                        except:
                            checkE += 1
                            time.sleep(0.1)
                    
                    if checkE > 200:
                        browser.quit()
                        continue
                        
                    checkE = 0
                    
                    while True:
                        if len(browser.window_handles) > 2:
                            browser.switch_to.window(browser.window_handles[2])
                            time.sleep(1)
                            while True:
                                try:
                                    if checkE > 200:
                                        break
                                    browser.find_element("xpath", '//button[@data-testid="page-container-footer-next"]').click()
                                    break
                                except Exception as ex:
                                    checkE += 1
                                    time.sleep(0.1)
                            time.sleep(1)
                            if checkE > 200:
                                break
                            while True:
                                try:
                                    if checkE > 200:
                                        break
                                    browser.find_element("xpath", '//button[@data-testid="page-container-footer-next"]').click()
                                    break
                                except Exception as ex:
                                    checkE += 1
                                    time.sleep(0.1)
                            time.sleep(2)
                            break

                    if checkE < 200:
                        checkE = 0
                        while True:
                            if len(browser.window_handles) > 2:
                                browser.switch_to.window(browser.window_handles[2])
                                time.sleep(1)
                                while True:
                                    try:
                                        if checkE > 200:
                                            break
                                        browser.find_element("xpath", '//button[@class="button btn--rounded btn-primary"]').click()
                                        break
                                    except Exception as ex:
                                        checkE += 1
                                        time.sleep(0.1)
                                time.sleep(2)
                                break
                        
                        if checkE > 200:
                            break
                        else:
                            browser.switch_to.window(browser.window_handles[0])

                            time.sleep(1)
                            while True:
                                try:
                                    browser.find_element("xpath", '//div[@class="modal-body"]/button').click()
                                    break
                                except Exception as ex:
                                    time.sleep(0.1)

                            time.sleep(1)
                            while True:
                                try:
                                    imgs = browser.find_elements("xpath", '//img[@src="\Assets\copy.svg"]')
                                    img = imgs[len(imgs) - 1]
                                    img.click()
                                    break
                                except Exception as ex:
                                    time.sleep(0.1)
                            time.sleep(1)
                                
                            variable = ""
                            while True:
                                try:
                                    variable = root.clipboard_get()
                                    break
                                except Exception as ex:
                                    print(ex)
                                    time.sleep(0.1)
                            
                            print(seed_phase_str)
                            print(spazz)
                            print(variable)
                            
                            ara = []
                            dic = {
                                "seed_phase":seed_phase_str,
                                "key":spazz,
                                "address":variable
                            }
                            fname = "doptestsFake.json"
                            with open(fname) as jsonfile:
                                dataz = json.load(jsonfile)
                                dataz.append(dic)
                                ara = dataz
                            with open(fname, 'w') as outfile:
                                json.dump(ara, outfile)

                            print(" ")

                            indexin += 1
    
        browser.quit()


START()