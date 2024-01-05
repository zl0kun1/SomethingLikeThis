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

from Modules import log, captcha
import json
# from capmonster_python import HCaptchaTaskProxyless


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
    indexin = 0 #max 53
    namez = "hungnty"
    
    while True:
        browser = webdriver.Chrome(options=opts)
        browser.set_window_position(0, 0)
        browser.maximize_window()
        browser.delete_all_cookies()
        print(indexin)
        number_tabs = 5
        while True:
            try:
                if len(browser.window_handles) == 2:
                    browser.switch_to.window(browser.window_handles[1])
                    break
            except Exception as ex:
                time.sleep(0.1)

        time.sleep(1)
        while True:
            try:
                while True:
                    try:
                        browser.get("chrome-extension://pojknglminpfceibjhoablbpohbghdbi/home.html")
                        break
                    except:
                        time.sleep(0.1)
                time.sleep(1)
                browser.find_element("xpath", '//input[@class="check-box onboarding__terms-checkbox far fa-square"]').click()
                # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                break
            except Exception as ex:
                time.sleep(0.1)
        
        while True:
            try:
                browser.find_element("xpath", '//button[@class="button btn--rounded btn-primary"]').click()
                # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                break
            except Exception as ex:
                time.sleep(0.1)
        
        while True:
            try:
                browser.find_element("xpath", '//button[@class="button btn--rounded btn-primary btn--large"]').click()
                # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                break
            except Exception as ex:
                time.sleep(0.1)

        while True:
            try:
                browser.find_element("xpath", '//input[@data-testid="create-password-new"]').send_keys(getPassword1())
                # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                break
            except Exception as ex:
                time.sleep(0.1)

        while True:
            try:
                browser.find_element("xpath", '//input[@data-testid="create-password-confirm"]').send_keys(getPassword1())
                # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                break
            except Exception as ex:
                time.sleep(0.1)
        while True:
            try:
                browser.find_element("xpath", '//input[@data-testid="create-password-terms"]').click()
                # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                break
            except Exception as ex:
                time.sleep(0.1)
                
        while True:
            try:
                browser.find_element("xpath", '//button[@class="button btn--rounded btn-primary btn--large create-password__form--submit-button"]').click()
                # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                break
            except Exception as ex:
                time.sleep(0.1)
                        
        while True:
            try:
                browser.find_element("xpath", '//button[@data-testid="secure-wallet-recommended"]').click()
                break
            except Exception as ex:
                time.sleep(0.1)

        while True:
            try:
                browser.find_element("xpath", '//button[@data-testid="recovery-phrase-reveal"]').click()
                break
            except Exception as ex:
                time.sleep(0.1)

        seedphraseStr = ""
        recovery_phrase = []
        while True:
            try:
                for i in range(12):
                    data_testid = "//div[@data-testid=" + "\"recovery-phrase-chip-" + str(i) + "\"]"
                    seed = browser.find_element("xpath", data_testid).text
                    recovery_phrase.insert(i,seed) 
                    if i == 0:
                        seedphraseStr = seed
                    else:
                        seedphraseStr = seedphraseStr + " " + seed
                break
            except Exception as ex:
                time.sleep(0.1)
        print(seedphraseStr)
        

        while True:
            try:
                browser.find_element("xpath", '//button[@data-testid="recovery-phrase-next"]').click()
                break
            except Exception as ex:
                time.sleep(0.1)

        for i in range(12):
            try:
                data_testid = "//input[@data-testid=" + "\"recovery-phrase-input-" + str(i) + "\"]"
                browser.find_element("xpath", data_testid).send_keys(recovery_phrase[i])
            except Exception as ex:
                time.sleep(0.1)

                
        while True:
            try:
                browser.find_element("xpath", '//button[@data-testid="recovery-phrase-confirm"]').click()
                break
            except Exception as ex:
                time.sleep(0.1)

        while True:
            try:
                browser.find_element("xpath", '//button[@data-testid="onboarding-complete-done"]').click()
                # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                break
            except Exception as ex:
                time.sleep(0.1)

        while True:
            try:
                browser.find_element("xpath", '//button[@data-testid="pin-extension-next"]').click()
                # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                break
            except Exception as ex:
                time.sleep(0.1)

        while True:
            try:
                browser.find_element("xpath", '//button[@data-testid="pin-extension-done"]').click()
                # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                break
            except Exception as ex:
                time.sleep(0.1)

        while True:
            try:
                browser.find_element("xpath", '//button[@data-testid="popover-close"]').click()
                # browser.find_element_by_xpath("//input[@name='username']").send_keys("+84" + number)
                break
            except Exception as ex:
                time.sleep(0.1)
        try:
            browser.switch_to.window(browser.window_handles[0])
            while True:
                try:
                    browser.get("https://www.glacier.io/referral/?0xe354307d602204dac5a21d7b236c223bbb86ab24")
                    break
                except:
                    time.sleep(0.1)
                    
            while True:
                browser.switch_to.window(browser.window_handles[0])
                time.sleep(2)
                if len(browser.window_handles) > 2:
                    browser.switch_to.window(browser.window_handles[2])
                    time.sleep(1)
                    while True:
                        try:
                            browser.find_element("xpath", '//button[@data-testid="popover-close"]').click()
                        except Exception as ex:
                            time.sleep(0.1)
                        try:
                            browser.find_element("xpath", '//button[@data-testid="page-container-footer-next"]').click()
                            break
                        except Exception as ex:
                            time.sleep(0.1)
                    time.sleep(1)
                    while True:
                        try:
                            browser.find_element("xpath", '//button[@data-testid="page-container-footer-next"]').click()
                            break
                        except Exception as ex:
                            time.sleep(0.1)
                    time.sleep(2)
                    break

            while True:
                browser.switch_to.window(browser.window_handles[0])
                time.sleep(2)
                if len(browser.window_handles) > 2:
                    browser.switch_to.window(browser.window_handles[2])
                    time.sleep(1)
                    while True:
                        try:
                            browser.find_element("xpath", '//button[@data-testid="popover-close"]').click()
                        except Exception as ex:
                            time.sleep(0.1)
                        try:
                            browser.find_element("xpath", '//button[@data-testid="page-container-footer-next"]').click()
                            break
                        except Exception as ex:
                            time.sleep(0.1)
                    time.sleep(2)
                    break
            browser.switch_to.window(browser.window_handles[0])

            while True:
                try:
                    browser.get("https://playground.bnb.glacier.io/")
                    break
                except:
                    time.sleep(0.1)

            while True:
                try:
                    browser.find_element("xpath", '//button[@class="arco-btn arco-btn-primary arco-btn-size-large arco-btn-shape-round arco-btn-long"]').click()
                    break
                except:
                    time.sleep(0.1)
                    
                    
            while True:
                try:
                    browser.find_element("xpath", '//div[@class="arco-modal-content"]').click()
                    break
                except:
                    time.sleep(0.1)

            while True:
                if len(browser.window_handles) > 2:
                    browser.switch_to.window(browser.window_handles[2])
                    time.sleep(1)
                    while True:
                        try:
                            browser.find_element("xpath", '//button[@data-testid="popover-close"]').click()
                        except Exception as ex:
                            time.sleep(0.1)
                        try:
                            browser.find_element("xpath", '//button[@data-testid="page-container-footer-next"]').click()
                            break
                        except Exception as ex:
                            time.sleep(0.1)
                    time.sleep(1)
                    while True:
                        try:
                            browser.find_element("xpath", '//button[@data-testid="page-container-footer-next"]').click()
                            break
                        except Exception as ex:
                            time.sleep(0.1)
                    time.sleep(2)
                    break
            
            browser.switch_to.window(browser.window_handles[0])
            
            while True:
                try:
                    browser.find_element("xpath", '//button[@class="arco-btn arco-btn-primary arco-btn-size-default arco-btn-shape-square arco-btn-long"]').click()
                    break
                except:
                    time.sleep(0.1)
            
            while True:
                try:
                    browser.find_element("xpath", '//input[@id="name_input"]').send_keys(name + str(indexin))
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            while True:
                try:
                    buttons = browser.find_elements("xpath", '//button[@type="button"]')
                    for butt in buttons:
                        try:
                            if butt.text == "OK":
                                butt.click()
                                break
                        except Exception as ex:
                            time.sleep(0.1)
                    break
                except Exception as ex:
                    time.sleep(0.1)
                    
            while True:
                if len(browser.window_handles) > 2:
                    browser.switch_to.window(browser.window_handles[2])
                    time.sleep(1)
                    while True:
                        try:
                            browser.find_element("xpath", '//button[@data-testid="popover-close"]').click()
                        except Exception as ex:
                            time.sleep(0.1)
                        try:
                            browser.find_element("xpath", '//button[@data-testid="page-container-footer-next"]').click()
                            break
                        except Exception as ex:
                            time.sleep(0.1)
                    time.sleep(2)
                    break
            
            browser.switch_to.window(browser.window_handles[0])
            while True:
                try:
                    browser.find_element("xpath", '//button[@class="arco-btn arco-btn-outline arco-btn-size-default arco-btn-shape-square arco-btn-long"]').click()
                    break
                except:
                    time.sleep(0.1)
            
            while True:
                try:
                    browser.find_element("xpath", '//input[@id="name_input"]').send_keys(name + str(indexin))
                    break
                except Exception as ex:
                    time.sleep(0.1)
            while True:
                try:
                    buttons = browser.find_elements("xpath", '//button[@type="button"]')
                    for butt in buttons:
                        try:
                            if butt.text == "OK":
                                butt.click()
                                break
                        except Exception as ex:
                            time.sleep(0.1)
                    break
                except Exception as ex:
                    time.sleep(0.1)
                    
            while True:
                if len(browser.window_handles) > 2:
                    browser.switch_to.window(browser.window_handles[2])
                    time.sleep(1)
                    while True:
                        try:
                            browser.find_element("xpath", '//button[@data-testid="popover-close"]').click()
                        except Exception as ex:
                            time.sleep(0.1)
                        try:
                            browser.find_element("xpath", '//button[@data-testid="page-container-footer-next"]').click()
                            break
                        except Exception as ex:
                            time.sleep(0.1)
                    time.sleep(2)
                    break
            
            browser.switch_to.window(browser.window_handles[0])
            
            
            while True:
                try:
                    browser.find_element("xpath", '//button[@class="arco-btn arco-btn-primary arco-btn-size-mini arco-btn-shape-square arco-btn-icon-only"]').click()
                    break
                except:
                    time.sleep(0.1)
            
            while True:
                try:
                    browser.find_element("xpath", '//input[@id="name_input"]').send_keys(name + str(indexin))
                    break
                except Exception as ex:
                    time.sleep(0.1)
            while True:
                try:
                    browser.find_element("xpath", '//input[@placeholder="Name"]').send_keys(name + str(indexin))
                    break
                except Exception as ex:
                    time.sleep(0.1)

            while True:
                try:
                    buttons = browser.find_elements("xpath", '//button[@type="button"]')
                    for butt in buttons:
                        try:
                            if butt.text == "OK":
                                butt.click()
                                break
                        except Exception as ex:
                            time.sleep(0.1)
                    break
                except Exception as ex:
                    time.sleep(0.1)
                    
            while True:
                if len(browser.window_handles) > 2:
                    browser.switch_to.window(browser.window_handles[2])
                    time.sleep(1)
                    while True:
                        try:
                            browser.find_element("xpath", '//button[@data-testid="popover-close"]').click()
                        except Exception as ex:
                            time.sleep(0.1)
                        try:
                            browser.find_element("xpath", '//button[@data-testid="page-container-footer-next"]').click()
                            break
                        except Exception as ex:
                            time.sleep(0.1)
                    time.sleep(2)
                    break
            
            browser.switch_to.window(browser.window_handles[0])
            
            
            while True:
                try:
                    browser.find_element("xpath", '//button[@class="arco-btn arco-btn-primary arco-btn-size-mini arco-btn-shape-square arco-btn-icon-only"]').click()
                    break
                except:
                    time.sleep(0.1)
            
            while True:
                try:
                    browser.find_element("xpath", '//input[@id="name_input"]').send_keys("hungntza")
                    break
                except Exception as ex:
                    time.sleep(0.1)
            while True:
                try:
                    browser.find_element("xpath", '//input[@placeholder="Name"]').send_keys("hungntza")
                    break
                except Exception as ex:
                    time.sleep(0.1)

            while True:
                try:
                    buttons = browser.find_elements("xpath", '//button[@type="button"]')
                    for butt in buttons:
                        try:
                            if butt.text == "OK":
                                butt.click()
                                break
                        except Exception as ex:
                            time.sleep(0.1)
                    break
                except Exception as ex:
                    time.sleep(0.1)
                    
            while True:
                if len(browser.window_handles) > 2:
                    browser.switch_to.window(browser.window_handles[2])
                    time.sleep(1)
                    while True:
                        try:
                            browser.find_element("xpath", '//button[@data-testid="popover-close"]').click()
                        except Exception as ex:
                            time.sleep(0.1)
                        try:
                            browser.find_element("xpath", '//button[@data-testid="page-container-footer-next"]').click()
                            break
                        except Exception as ex:
                            time.sleep(0.1)
                    time.sleep(2)
                    break
            
            browser.switch_to.window(browser.window_handles[0])
            
            while True:
                try:
                    browser.find_element("xpath", '//div[@class="style_row__AC8mP"]').click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)
# chrome-extension://opfgelmcmbiajamepnmloijbpoleiama/popup.html#/welcome
            time.sleep(1)
            while True:
                checkclick = 0
                try:
                    buttons = browser.find_elements("xpath", '//button[@type="button"]')
                    for butt in buttons:
                        try:
                            if butt.text == "Insert Document":
                                checkclick = 1
                                butt.click()
                                break
                        except Exception as ex:
                            time.sleep(0.1)
                    if checkclick == 1:
                        break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            
            while True:
                try:
                    line = '//textarea[@placeholder=\"' + name + str(indexin) + '\"]'
                    browser.find_element("xpath", line).send_keys("hungntzb")
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            while True:
                try:
                    buttons = browser.find_elements("xpath", '//button[@type="button"]')
                    for butt in buttons:
                        try:
                            if butt.text == "OK":
                                butt.click()
                                break
                        except Exception as ex:
                            time.sleep(0.1)
                    break
                except Exception as ex:
                    time.sleep(0.1)

            while True:
                if len(browser.window_handles) > 2:
                    browser.switch_to.window(browser.window_handles[2])
                    time.sleep(1)
                    while True:
                        try:
                            browser.find_element("xpath", '//button[@data-testid="popover-close"]').click()
                        except Exception as ex:
                            time.sleep(0.1)
                        try:
                            browser.find_element("xpath", '//button[@data-testid="page-container-footer-next"]').click()
                            break
                        except Exception as ex:
                            time.sleep(0.1)
                    time.sleep(2)
                    break
            
            browser.switch_to.window(browser.window_handles[0])
            
            time.sleep(1)
            while True:
                try:
                    buttons = browser.find_elements("xpath", '//button[@type="button"]')
                    for butt in buttons:
                        try:
                            if butt.text == "Insert Document":
                                butt.click()
                                break
                        except Exception as ex:
                            time.sleep(0.1)
                    break
                except Exception as ex:
                    time.sleep(0.1)

            
            while True:
                try:
                    line = '//textarea[@placeholder=\"' + name + str(indexin) + '\"]'
                    browser.find_element("xpath", line).send_keys("hungntzc")
                    break
                except Exception as ex:
                    time.sleep(0.1)

            while True:
                try:
                    buttons = browser.find_elements("xpath", '//button[@type="button"]')
                    for butt in buttons:
                        try:
                            if butt.text == "OK":
                                butt.click()
                                break
                        except Exception as ex:
                            time.sleep(0.1)
                    break
                except Exception as ex:
                    time.sleep(0.1)

            while True:
                if len(browser.window_handles) > 2:
                    browser.switch_to.window(browser.window_handles[2])
                    time.sleep(1)
                    while True:
                        try:
                            browser.find_element("xpath", '//button[@data-testid="popover-close"]').click()
                        except Exception as ex:
                            time.sleep(0.1)
                        try:
                            browser.find_element("xpath", '//button[@data-testid="page-container-footer-next"]').click()
                            break
                        except Exception as ex:
                            time.sleep(0.1)
                    time.sleep(2)
                    break
            
            browser.switch_to.window(browser.window_handles[0])
            time.sleep(1)
            while True:
                try:
                    buttons = browser.find_elements("xpath", '//button[@type="button"]')
                    for butt in buttons:
                        try:
                            if butt.text == "Apply":
                                butt.click()
                                break
                        except Exception as ex:
                            time.sleep(0.1)
                    break
                except Exception as ex:
                    time.sleep(0.1)

            ara = []
            fname = "glacier.json"
            with open(fname) as jsonfile:
                dataz = json.load(jsonfile)
                dataz.append(seedphraseStr)
                ara = dataz
            with open(fname, 'w') as outfile:
                json.dump(ara, outfile)
            indexin += 1
            browser.quit()
        except Exception as ex:
            print(ex)
    
    browser.quit()


START()