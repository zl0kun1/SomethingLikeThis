# Auto Almost Everything
# Youtube Channel https://www.youtube.com/c/AutoAlmostEverything
# Please read README.md carefully before use

from datetime import datetime
import os, threading, random, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Proxy
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Modules import log, wordlist
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import urllib.parse as urlparse
# from capmonster_python import NoCaptchaTaskProxyless

app = 'PreSearch'
register = 'https://account.presearch.org/signup?rid=2508931'
user_name = 'mikestand62649gogo.ult'
last_name = '@gmail.com'

wl = wordlist.get()
presearch_max_count = 30

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "Drivers/chromedriver101")
geckodriver = os.path.join(PROJECT_ROOT, "Drivers/geckodriver")
waiter = 0
chromedriver_path = DRIVER_BIN

opts = Options()
opts.binary_location = os.path.expanduser("/Applications/Brave Browser.app/Contents/MacOS/Brave Browser")
opts.add_extension('/Users/hungnguyen/Desktop/Desktop/test/PreSearch/buster_captcha_solver-1.3.1.xpi')

now = datetime.now()

def getUserNameByCount(count):
    count_str = "%s" % count
    name = user_name + count_str + last_name
    return name

def getPassword():
    return chr(110) + chr(116) + chr(102) + chr(111) + chr(114) + chr(101) + chr(118) + chr(101) + chr(114)

def CanvasDraw(browser, xoffset, yoffset):
    canvas = browser.find_element_by_xpath("//*[@class='login-box']")
    action = ActionChains(browser)
    action.move_to_element(canvas)
    action.move_by_offset(xoffset=xoffset, yoffset=yoffset)
    action.click()
    action.perform()
    log.screen_n_file('CanvasDraw xoffset %d yoffset %d' %(xoffset, yoffset))
    # log.screen(' [*] Click to (%d, %d)' % (xoffset, yoffset))

# Search 30 times
def Search():
    func = "Multi-Account Search"
    func_path = 'https://engine.presearch.org'
    number_name = 1
    while True:
        #opts.headless = True  # <-- Comment this line if you want to show browser.
        browser = webdriver.Chrome(options=opts, executable_path=chromedriver_path)
        # browser = webdriver.Firefox(executable_path=geckodriver)
        browser.set_page_load_timeout(60)
        browser.set_window_position(0, 0)
        browser.maximize_window()
        browser.delete_all_cookies()
        username = getUserNameByCount(number_name)
        print('username %s\n' % username)
        password = getPassword()

        try:
            while True:
                try:
                    browser.get(register)
                    break
                except:
                    time.sleep(0.1)
            time.sleep(0.3)
            while True:
                try:
                    browser.find_element_by_xpath("//a[@href='https://account.presearch.org/login?signin']").click()
                    break
                except:
                    time.sleep(0.1)
            time.sleep(1)
            while True:
                try:
                    browser.find_element_by_xpath("//a[@class='register-form-show btn btn-block tw-bg-presearch-blue tw-text-white hover:tw-text-white dark:tw-bg-blue-600 hover:tw-opacity-70 tw-transition']").click()
                    break
                except:
                    time.sleep(0.1)

            time.sleep(1)
            while True:
                try:
                    browser.find_element_by_xpath("//input[@placeholder='Email Address']").send_keys(username)
                    break
                except:
                    time.sleep(0.1)

            while True:
                try:
                    browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/input[@placeholder='Password']").send_keys(password)
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            while True:
                try:
                    browser.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys(password)
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            while True:
                try:
                    browser.find_element_by_xpath("//input[@name='agreed_to_terms']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(0.1)
            # while True:
            #     try:
            #         # recaptcha = browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/div/div/iframe[@title='reCAPTCHA']")
            #         recaptcha = browser.find_element_by_xpath("//iframe[contains(@title, 'reCAPTCHA')]")
            #         print("recaptcha")
            #         sitekey = ''
            #         for query in urlparse.urlparse(
            #                 recaptcha.get_attribute('src')).query.split(
            #             '&'):
            #             if 'k=' in query:
            #                 sitekey = query.split('=')[1]

            #         captcha = NoCaptchaTaskProxyless(client_key="1a4a36584f30ba67eef2d5b80de4120b")
            #         taskId = captcha.createTask(browser.current_url, sitekey)
            #         response = captcha.joinTaskResult(taskId)
            #         # browser.execute_script(f"document.getElementById('g-recaptcha-response')[0].innerHTML = '{response}';")
            #         browser.execute_script('''
            #                 document.getElementById("g-recaptcha-response-1").innerHTML=arguments[0];
            #             ''', response)
            #         print("captcha solve")
            #         # time.sleep(11)
            #         # while True:
            #         #     try:
            #         #         browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/button[@class='btn btn-lg btn-block tw-bg-yellow-600 tw-text-white hover:tw-text-white hover:tw-opacity-60 tw-transition']").click()
            #         #     except Exception as ex:
            #         #         print(ex)
            #         #      
            #         break
            #     except Exception as ex:
            #         print(ex)
            #         time.sleep(0.1)    
            iframe = None
            while True:
                try:
                    iframe = browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/div/div/iframe")
                    iframe.click()
                    # iframe = browser.find_element_by_xpath('iframe')[0]
                    # iframe.find_element_by_xpath("//*[@class='recaptcha-checkbox-spinner'").click()
                    # browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/div/div/iframe[@placeholder='Password']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(2)
            checkIfVerified = 0
            login_box = None
            try:
                login_box = browser.find_element_by_xpath("//*[@class='login-box']/div/div/form")
            except Exception as ex:
                print(ex)
                time.sleep(0.1)
            try:
                # iframe = browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/div/div/iframe/")
                browser.switch_to.frame(iframe)
                span = browser.find_element_by_xpath("//*[@id='rc-anchor-container']/div/div/div/div/span")
                verify = span.get_attribute('aria-checked')
                if verify == 'true':
                    checkIfVerified = 1
                else:
                    while True:
                        try:
                            browser.switch_to.frame(login_box)
                            #rc-imageselect
                            #rc-footer
                            #rc-controls
                            #primary-controls
                            #rc-buttons
                            #error rc-doscaptcha-header rc-doscaptcha-header-text
                            # input("...")
                            # iframe2 = browser.find_elements_by_xpath("//iframe")
                            # print(iframe2)
                            # # browser.switch_to.frame(iframe2)
                            # input("...")
                            
                            # try:
                            #     browser.find_element_by_xpath("//div[@class='rc-imageselect']")
                            #     break
                            # except Exception as ex:
                            #     print(ex)
                            #     time.sleep(0.1)
                            # try:
                            #     browser.find_element_by_xpath("//div[@class='rc-footer']")
                            #     break
                            # except Exception as ex:
                            #     print(ex)
                            #     time.sleep(0.1)
                            # try:
                            #     browser.find_element_by_xpath("//div[@class='rc-controls']")
                            #     break
                            # except Exception as ex:
                            #     print(ex)
                            #     time.sleep(0.1)
                            # try:
                            #     browser.find_element_by_xpath("//div[@class='primary-controls']")
                            #     break
                            # except Exception as ex:
                            #     print(ex)
                            #     time.sleep(0.1)
                            # try:
                            #     browser.find_element_by_xpath("//div[@class='rc-buttons']")
                            #     break
                            # except Exception as ex:
                            #     print(ex)
                            #     time.sleep(0.1)
                            # # button-holder help-button-holder
                            # button_holder = browser.find_element_by_xpath("//*[@class='button-holder help-button-holder']")
                            # browser.switch_to.frame(button_holder)
                            # browser.find_element_by_id("button-holder help-button-holder").click()
                            # browser.find_element_by_xpath("//*[@id='solver-button']").click()
                            input("...")
                            CanvasDraw(browser, 120, 120)
                            input("...")
                            break
                        except Exception as ex:
                            print(ex)
                            time.sleep(0.1)
            except Exception as ex:
                time.sleep(0.1)

            input("...")
            #solver-button
            time.sleep(0.1)
            while True:
                try:
                    browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/button[@class='btn btn-lg btn-block tw-bg-yellow-600 tw-text-white hover:tw-text-white hover:tw-opacity-60 tw-transition']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)
            time.sleep(2)

            check_login1 = 0

            try:
                browser.find_element_by_xpath("//div[@class='ajax-error form-group text-danger text-center']")
                check_login1 = 1
            except Exception as ex:
                check_login1 = 0
                print(ex)

            if check_login1:
                time.sleep(333)
                browser.get(register)
                time.sleep(0.3)
                while True:
                    try:
                        browser.find_element_by_xpath("//a[@href='https://account.presearch.org/login']").click()
                        break
                    except:
                        time.sleep(0.1)
                
                time.sleep(1)
                while True:
                    try:
                        browser.find_element_by_xpath("//a[@class='register-form-show btn btn-block tw-bg-presearch-blue tw-text-white hover:tw-text-white dark:tw-bg-blue-600 hover:tw-opacity-70 tw-transition']").click()
                        break
                    except:
                        time.sleep(0.1)

                time.sleep(1)
                while True:
                    try:
                        browser.find_element_by_xpath("//input[@placeholder='Email Address']").send_keys(username)
                        break
                    except:
                        time.sleep(0.1)

                while True:
                    try:
                        browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/input[@placeholder='Password']").send_keys(password)
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                while True:
                    try:
                        browser.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys(password)
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                while True:
                    try:
                        browser.find_element_by_xpath("//input[@name='agreed_to_terms']").click()
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                time.sleep(0.1)
                # while True:
                #     try:
                #         # recaptcha = browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/div/div/iframe[@title='reCAPTCHA']")
                #         recaptcha = browser.find_element_by_xpath("//iframe[contains(@title, 'reCAPTCHA')]")
                #         print("recaptcha")
                #         sitekey = ''
                #         for query in urlparse.urlparse(
                #                 recaptcha.get_attribute('src')).query.split(
                #             '&'):
                #             if 'k=' in query:
                #                 sitekey = query.split('=')[1]

                #         captcha = NoCaptchaTaskProxyless(client_key="1a4a36584f30ba67eef2d5b80de4120b")
                #         taskId = captcha.createTask(browser.current_url, sitekey)
                #         response = captcha.joinTaskResult(taskId)
                #         # browser.execute_script(f"document.getElementById('g-recaptcha-response')[0].innerHTML = '{response}';")
                #         browser.execute_script('''
                #                 document.getElementById("g-recaptcha-response-1").innerHTML=arguments[0];
                #             ''', response)
                #         print("captcha solve")
                #         # time.sleep(11)
                #         # while True:
                #         #     try:
                #         #         browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/button[@class='btn btn-lg btn-block tw-bg-yellow-600 tw-text-white hover:tw-text-white hover:tw-opacity-60 tw-transition']").click()
                #         #     except Exception as ex:
                #         #         print(ex)
                #         #         time.sleep(0.1)
                #         break
                #     except Exception as ex:
                #         print(ex)
                #         time.sleep(0.1)    

                time.sleep(0.1)
                while True:
                    try:
                        browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/button[@class='btn btn-lg btn-block tw-bg-yellow-600 tw-text-white hover:tw-text-white hover:tw-opacity-60 tw-transition']").click()
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)
                
                time.sleep(2)        

            #{"method":"xpath","selector":"//*[@class='introjs-tooltip introjs-top-left-aligned']/div/a[@class='introjs-button introjs-nextbutton introjs-fullbutton']"}
            while True:
                try:
                    browser.find_element_by_xpath("//div[@class='introjs-tooltipReferenceLayer']/div/div/a[@class='introjs-button introjs-nextbutton introjs-fullbutton']").click()
                    break
                except Exception as ex:
                    time.sleep(0.1)

            time.sleep(0.2)

            while True:
                try:
                    browser.find_element_by_xpath("//*[@class='introjs-tooltip introjs-bottom-right-aligned']/div/a[@class='introjs-button introjs-nextbutton']").click()
                    break
                except Exception as ex:
                    time.sleep(0.1)

            time.sleep(0.2)
            
            while True:
                try:
                    browser.find_element_by_xpath("//*[@class='introjs-tooltip introjs-top-left-aligned']/div/a[@class='introjs-button introjs-nextbutton']").click()
                    break
                except Exception as ex:
                    time.sleep(0.1)

            time.sleep(0.2)
            
            while True:
                try:
                    browser.find_element_by_xpath("//*[@class='introjs-tooltip introjs-top-left-aligned']/div/a[@class='introjs-button introjs-nextbutton']").click()
                    break
                except Exception as ex:
                    time.sleep(0.1)

            time.sleep(0.2)
            
            while True:
                try:
                    browser.find_element_by_xpath("//*[@class='introjs-tooltip introjs-top-left-aligned']/div/a[@class='introjs-button introjs-nextbutton']").click()
                    break
                except Exception as ex:
                    time.sleep(0.1)

            time.sleep(0.2)
            
            while True:
                try:
                    browser.find_element_by_xpath("//*[@class='introjs-tooltip introjs-left']/div/a[@class='introjs-button introjs-skipbutton introjs-donebutton']").click()
                    break
                except Exception as ex:
                    time.sleep(0.1)

            time.sleep(1)
            
            while True:
                try:
                    browser.find_element_by_xpath("//div[@class='introjs-tooltipReferenceLayer']/div/div/a[@class='introjs-button introjs-nextbutton introjs-fullbutton']").click()
                    break
                except Exception as ex:
                    time.sleep(0.1)

            time.sleep(0.2)
            
            while True:
                try:
                    browser.find_element_by_xpath("//div[@class='introjs-tooltipReferenceLayer']/div/div/a[@class='introjs-button introjs-nextbutton']").click()
                    break
                except Exception as ex:
                    time.sleep(0.1)

            time.sleep(1)
            
            while True:
                try:
                    browser.find_element_by_xpath("//div[@class='introjs-tooltipReferenceLayer']/div/div/a[@class='introjs-button introjs-nextbutton']").click()
                    break
                except Exception as ex:
                    time.sleep(0.1)

            time.sleep(2.5)
            
            while True:
                try:
                    browser.find_element_by_xpath("//div[@class='introjs-tooltipReferenceLayer']/div/div/a[@class='introjs-button introjs-nextbutton']").click()
                    break
                except Exception as ex:
                    time.sleep(0.1)

            time.sleep(1.5)
            
            while True:
                try:
                    browser.find_element_by_xpath("//div[@class='introjs-tooltipReferenceLayer']/div/div/a[@class='introjs-button introjs-nextbutton']").click()
                    break
                except Exception as ex:
                    time.sleep(0.1)

            time.sleep(3)
            
            while True:
                try:
                    browser.find_element_by_xpath("//div[@class='introjs-tooltipReferenceLayer']/div/div/a[@class='introjs-button introjs-nextbutton']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(0.5)
            
            while True:
                try:
                    browser.find_element_by_xpath("//div[@class='introjs-tooltipReferenceLayer']/div/div/a[@class='introjs-button introjs-nextbutton']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(0.5)
            
            while True:
                try:
                    browser.find_element_by_xpath("//div[@class='introjs-tooltipReferenceLayer']/div/div/a[@class='introjs-button introjs-skipbutton introjs-donebutton']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(1)
            # hungnguyenthac12081995.100@gmail.com
            while True:
                try:
                    browser.find_element_by_xpath("//div[@class='container-fluid no-gutter']/div/ul/li/a[@id='user-menu-toggle']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)
                    
            time.sleep(0.1)

            while True:
                try:
                    browser.find_element_by_xpath("//div[@class='container-fluid no-gutter']/div/ul/li/ul/li/a[@href='https://presearch.org/logout']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(1.5)

            while True:
                try:
                    browser.find_element_by_xpath("//div[@class='container-fluid no-gutter']/div/ul/li/a[@href='https://presearch.org/login']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(2.5)

            while True:
                try:
                    browser.find_element_by_xpath("//*[@class='tab-content']/div/form/div/input[@placeholder='Email']").send_keys(username)
                    break
                except:
                    time.sleep(0.1)

            time.sleep(0.1)

            while True:
                try:
                    browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/input[@placeholder='Password']").send_keys(password)
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(0.1)
            
            while True:
                try:
                    browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/div/div[@class='checkbox blue text-left']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(0.1)
            # while True:
            #     try:
            #         # recaptcha = browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/div/div/iframe[@title='reCAPTCHA']")
            #         recaptcha = browser.find_element_by_xpath("//iframe[contains(@title, 'reCAPTCHA')]")
            #         print("recaptcha")
            #         sitekey = ''
            #         for query in urlparse.urlparse(
            #                 recaptcha.get_attribute('src')).query.split(
            #             '&'):
            #             if 'k=' in query:
            #                 sitekey = query.split('=')[1]

            #         captcha = NoCaptchaTaskProxyless(client_key="1a4a36584f30ba67eef2d5b80de4120b")
            #         taskId = captcha.createTask(browser.current_url, sitekey)
            #         response = captcha.joinTaskResult(taskId)
            #         # browser.execute_script(f"document.getElementById('g-recaptcha-response')[0].innerHTML = '{response}';")
            #         browser.execute_script('''
            #                 document.getElementById("g-recaptcha-response").innerHTML=arguments[0];
            #             ''', response)
            #         print("captcha solve")
            #         # time.sleep(11)
            #         # while True:
            #         #     try:
            #         #         browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/button[@class='btn btn-lg btn-block tw-bg-yellow-600 tw-text-white hover:tw-text-white hover:tw-opacity-60 tw-transition']").click()
            #         #     except Exception as ex:
            #         #         print(ex)
            #         #         time.sleep(0.1)
            #         break
            #     except Exception as ex:
            #         print(ex)
            #         time.sleep(0.1) 
                        
            # input("Solve Captcha then Enter...")

            time.sleep(0.1)
            
            while True:
                try:
                    browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/button[@type='submit']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(2)

            check_login2 = 0

            try:
                browser.find_element_by_xpath("//div[@class='ajax-error form-group text-danger text-center']")
                check_login2 = 1
            except Exception as ex:
                check_login2 = 0
                print(ex)

            if check_login2:
                time.sleep(333)

                browser.get("https://account.presearch.org/login")

                time.sleep(3)

                while True:
                    try:
                        browser.find_element_by_xpath("//*[@class='tab-content']/div/form/div/input[@placeholder='Email']").send_keys(username)
                        break
                    except:
                        time.sleep(0.1)

                time.sleep(0.1)

                while True:
                    try:
                        browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/input[@placeholder='Password']").send_keys(password)
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                time.sleep(0.1)
                
                while True:
                    try:
                        browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/div/div[@class='checkbox blue text-left']").click()
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                time.sleep(0.1)
                # while True:
                #     try:
                #         # recaptcha = browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/div/div/iframe[@title='reCAPTCHA']")
                #         recaptcha = browser.find_element_by_xpath("//iframe[contains(@title, 'reCAPTCHA')]")
                #         print("recaptcha")
                #         sitekey = ''
                #         for query in urlparse.urlparse(
                #                 recaptcha.get_attribute('src')).query.split(
                #             '&'):
                #             if 'k=' in query:
                #                 sitekey = query.split('=')[1]

                #         captcha = NoCaptchaTaskProxyless(client_key="1a4a36584f30ba67eef2d5b80de4120b")
                #         taskId = captcha.createTask(browser.current_url, sitekey)
                #         response = captcha.joinTaskResult(taskId)
                #         # browser.execute_script(f"document.getElementById('g-recaptcha-response')[0].innerHTML = '{response}';")
                #         browser.execute_script('''
                #                 document.getElementById("g-recaptcha-response").innerHTML=arguments[0];
                #             ''', response)
                #         print("captcha solve")
                #         # time.sleep(11)
                #         # while True:
                #         #     try:
                #         #         browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/button[@class='btn btn-lg btn-block tw-bg-yellow-600 tw-text-white hover:tw-text-white hover:tw-opacity-60 tw-transition']").click()
                #         #     except Exception as ex:
                #         #         print(ex)
                #         #         time.sleep(0.1)
                #         break
                #     except Exception as ex:
                #         print(ex)
                #         time.sleep(0.1) 
                            
                # input("Solve Captcha then Enter...")

                time.sleep(0.1)
                
                while True:
                    try:
                        browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/button[@type='submit']").click()
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                time.sleep(2)

            while True:
                try:
                    q = wordlist.gen(wl)
                    browser.find_element_by_xpath("//input[@placeholder='Search']").send_keys(q, Keys.ENTER)
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(5)

            while True:
                try:
                    browser.find_element_by_xpath("//*[@class='flex flex-col flex-auto w-full min-h-screen']/div/div/div/div/div/a[@href='javascript:void(0)']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(1)
            #Get cookie save to file
            #len(array)
            token = ""
            remember = ""
            try:
                cookies = browser.get_cookies()
                for cookie in cookies:
                    name = cookie["name"]
                    if name == "token":
                        token = cookie["value"]
                        print('token %s\n' % token)
                    if name == "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d":
                        remember = cookie["value"]
                        print('remember %s\n' % remember)

                if not token or not remember:
                    time.sleep(1)
                    try:
                        cookies = browser.get_cookies()
                        
                        for cookie in cookies:
                            name = cookie["name"]
                            if name == "token":
                                token = cookie["value"]
                                print('token %s\n' % token)
                            if name == "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d":
                                remember = cookie["value"]
                                print('remember %s\n' % remember)
                    except Exception as ex:
                        print(ex)

                if not token or not remember:
                    time.sleep(1)
                    try:
                        cookies = browser.get_cookies()
                        
                        for cookie in cookies:
                            name = cookie["name"]
                            if name == "token":
                                token = cookie["value"]
                                print('token %s\n' % token)
                            if name == "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d":
                                remember = cookie["value"]
                                print('remember %s\n' % remember)
                    except Exception as ex:
                        print(ex)

            except Exception as ex:
                print(ex)
            
            time.sleep(1)

            #verify account
            while True:
                try:
                    browser.find_element_by_xpath("//*[@class='flex flex-col flex-auto w-full min-h-screen']/div/div/div/div/div/a[@href='https://presearch.org/account']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(1)

            while True:
                try:
                    browser.find_element_by_xpath("//*[@class='row slim-gutter']/div/div/a[@href='https://account.presearch.org/account/privacy-settings']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(2)

            while True:
                try:
                    browser.find_element_by_xpath("//*[@id='main']/div/a/button[@class='btn btn-primary']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(2)

            code = ""
            while True:
                try:
                    code = browser.find_element_by_xpath("//*[@id='main']/div/code").text
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)
            print("2fa %s" %code)
            try:
                data = {"email":username, "token":token, "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d":remember, "code":code}
                fname = "babe.json"
                if os.path.isfile(fname):
                    # File exists
                    ara = []
                    with open(fname) as jsonfile:
                        dataz = json.load(jsonfile)
                        dataz.append(data)
                        ara = dataz
                    with open(fname, 'w') as outfile:
                        json.dump(ara, outfile)
                else: 
                    # Create file
                    with open(fname, 'w') as outfile:
                        array = []
                        array.append(data)
                        json.dump(array, outfile)

            except Exception as ex:
                print(ex)
                time.sleep(0.1)

            fa = ""
            try:
                # Open a new window
                browser.execute_script("window.open('');")
                browser.switch_to.window(browser.window_handles[1])
                browser.get("https://get2fa.dev/")
                # Switch to the new window
                try:
                    browser.find_element_by_xpath("//*[@class='container']/div/div/input[@placeholder='The secret key (in base-32 format)']").clear()
                    browser.find_element_by_xpath("//*[@class='container']/div/div/input[@placeholder='The secret key (in base-32 format)']").send_keys(code)
                except Exception as ex:
                    print(ex)

                time.sleep(0.5)

                try:
                    fa = browser.find_element_by_xpath("//*[@class='container']/div/p[@class='title is-size-1 has-text-centered']").text
                except Exception as ex:
                    time.sleep(0.1)
                    print(ex)

                if not fa:
                    time.sleep(0.5)
                    try:
                        fa = browser.find_element_by_xpath("//*[@class='container']/div/p[@class='title is-size-1 has-text-centered']").text
                    except Exception as ex:
                        print(ex)

                browser.switch_to.window(browser.window_handles[0])
            except Exception as ex:
                print(ex)
                time.sleep(0.1)

            time.sleep(0.5)
            while True:
                try:
                    browser.find_element_by_xpath("//*[@id='main']/div/form/input[@placeholder='000000']").clear()
                    browser.find_element_by_xpath("//*[@id='main']/div/form/input[@placeholder='000000']").send_keys(fa)
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(0.3)
            while True:
                try:
                    browser.find_element_by_xpath("//*[@id='main']/div/form/button[@type='submit']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(1)
            check_success = 0
            try:
                fail = browser.find_element_by_xpath("//div[@class='alert alert-danger text-center']").text
                if "Invalid code" in fail:
                    check_success = 0
            except Exception as ex:
                print(ex)
                time.sleep(0.1)

            try:
                success = browser.find_element_by_xpath("//div[@class='alert alert-success text-center']").text
                if "Two-Factor Authentication Activated" in success:
                    check_success = 1
            except Exception as ex:
                print(ex)
                time.sleep(0.1)
            
            if not check_success:
                try:
                    browser.switch_to.window(browser.window_handles[1])
                    try:
                        browser.find_element_by_xpath("//*[@class='container']/div/div/input[@placeholder='The secret key (in base-32 format)']").clear()
                        browser.find_element_by_xpath("//*[@class='container']/div/div/input[@placeholder='The secret key (in base-32 format)']").send_keys(code)
                    except Exception as ex:
                        print(ex)

                    time.sleep(0.5)

                    try:
                        fa = browser.find_element_by_xpath("//*[@class='container']/div/p[@class='title is-size-1 has-text-centered']").text
                    except Exception as ex:
                        time.sleep(0.1)
                        print(ex)

                    if not fa:
                        time.sleep(0.5)
                        try:
                            fa = browser.find_element_by_xpath("//*[@class='container']/div/p[@class='title is-size-1 has-text-centered']").text
                        except Exception as ex:
                            print(ex)

                    browser.switch_to.window(browser.window_handles[0])
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

                time.sleep(0.5)
                while True:
                    try:
                        browser.find_element_by_xpath("//*[@id='main']/div/form/input[@placeholder='000000']").clear()
                        browser.find_element_by_xpath("//*[@id='main']/div/form/input[@placeholder='000000']").send_keys(fa)
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                time.sleep(0.3)
                while True:
                    try:
                        browser.find_element_by_xpath("//*[@id='main']/div/form/button[@type='submit']").click()
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

            time.sleep(1)

            while True:
                try:
                    browser.find_element_by_xpath("//div[@class='container-fluid no-gutter']/div/ul/li/a[@id='user-menu-toggle']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)
                    
            time.sleep(0.1)

            while True:
                try:
                    browser.find_element_by_xpath("//div[@class='container-fluid no-gutter']/div/ul/li/ul/li/a[@href='https://presearch.org/account']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(1.5)

            while True:
                try:
                    browser.find_element_by_xpath("//*[@class='row slim-gutter']/div/div/a[@href='https://presearch.org/account/referrals']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)


            time.sleep(1.5)
            while True:
                try:
                    browser.find_element_by_xpath("//div[@id='main']/div/form/div/label/input[@type='checkbox']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(0.3)
            while True:
                try:
                    browser.find_element_by_xpath("//div[@id='main']/div/form/button[@type='submit']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(1.5)

            while True:
                try:
                    browser.find_element_by_xpath("//div[@class='container-fluid no-gutter']/div/ul/li/a[@id='user-menu-toggle']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)
                    
            time.sleep(0.1)

            while True:
                try:
                    browser.find_element_by_xpath("//div[@class='container-fluid no-gutter']/div/ul/li/ul/li/a[@href='https://presearch.org/account']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(1.5)

            while True:
                try:
                    browser.find_element_by_xpath("//*[@class='row slim-gutter']/div/div/a[@href='https://presearch.org/account/user-profile']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(1.5)
            while True:
                try:
                    browser.find_element_by_xpath("//div[@id='main']/div/form/div/input[@id='name']").send_keys("NGUYEN THAC HUNG")
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(0.1)
            while True:
                try:
                    num = "%s" % number_name
                    browser.find_element_by_xpath("//div[@id='main']/div/form/div/input[@id='display_name']").send_keys("hungnt" + num)
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(0.1)
            while True:
                try:
                    browser.find_element_by_xpath("//div[@id='main']/div/form/div/select[@name='gender']/option[@value='M']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(0.1)
            while True:
                try:
                    browser.find_element_by_xpath("//div[@id='main']/div/form/div/select[@name='country_id']/option[@value='704']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(0.1)
            while True:
                try:
                    browser.find_element_by_xpath("//div[@id='main']/div/form/button[@type='submit']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(1)
            print("Finish creating :" + username)
            number_name += 1  
            browser.quit()
            # print("Wait 60s to continue...")
            # time.sleep(60)
        except Exception as ex:
            log.screen_n_file('[!] %s has exception: %s!' % (app, ex))
        finally:
            browser.quit()


Search()