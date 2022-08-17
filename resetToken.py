# Auto Almost Everything
# Youtube Channel https://www.youtube.com/c/AutoAlmostEverything
# Please read README.md carefully before use

from datetime import datetime
import os, threading, random, time, json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Proxy
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Modules import log, wordlist
import urllib.parse as urlparse
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from capmonster_python import HCaptchaTask

app = 'PreSearch'
wl = wordlist.get()
presearch_max_count = 30
presearch_maximum = 100

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "Drivers/chromedriver104")
waiter = 0

chromedriver_path = DRIVER_BIN

now = datetime.now()


opts = Options()
ser = Service(DRIVER_BIN)
opts.binary_location = os.path.expanduser("/Applications/Brave Browser.app/Contents/MacOS/Brave Browser")

def getPassword():
    return chr(110) + chr(116) + chr(102) + chr(111) + chr(114) + chr(101) + chr(118) + chr(101) + chr(114)

# Search 30 times
def Search():
    now = datetime.now()
    func_path = "https://presearch.com/" 
    old_current_token = 0
    num_file = 0
    num_file_str = "%s" % num_file
    fname = "tonic" + num_file_str
    ara = []         
    if os.path.isfile(fname):
        # File exists
        with open(fname) as jsonfile:
            dataz = json.load(jsonfile)
            ara = dataz
    len_ara = len(ara)
    select_account = 0 #73
    retry = 0
    while True:
        # Browser config
        # opts = Options()
        # opts.binary_location = os.path.expanduser("/Applications/Brave Browser.app/Contents/MacOS/Brave Browser")
        opts.add_experimental_option('excludeSwitches', ['enable-automation'])
        opts.add_experimental_option('useAutomationExtension', False)
        opts.add_experimental_option('prefs', {'download_restrictions': 3})
        opts.headless = True  # <-- Comment this line if you want to show browser.
        opts.add_argument("--enable-javascript")
        
        while True:
            if select_account == len_ara:
                num_file += 1
                num_file_str = "%s" % num_file
                select_account = 0
                fname = "tonic" + num_file_str
                ara = []         
                if os.path.isfile(fname):
                    # File exists
                    with open(fname) as jsonfile:
                        dataz = json.load(jsonfile)
                        ara = dataz
                len_ara = len(ara)
                break
                
            try:
                check_cookie = 0
                cookie = ara[select_account]["cookie"]
                for c in cookie:
                    if c["name"] == "last_global_settings_change":
                        check_cookie = 1

                if check_cookie > 0:
                    select_account += 1
                    break
                
                # rem = ara[select_account]["last_global_settings_change"]
                # if rem == None or rem == '': 
                #     time.sleep(0.1)
                # else:
                #     select_account += 1
                #     break

            except Exception as ex:
                time.sleep(0.1)

            browser = webdriver.Chrome(options=opts, service=ser)
            # browser = webdriver.Firefox(executable_path=geckodriver)
            browser.set_page_load_timeout(60)
            browser.set_window_position(0, 0)
            browser.maximize_window()
            browser.delete_all_cookies()
            email = ara[select_account]["email"]
            print("email %s" %email)
            time.sleep(0.1)
            while True:
                try:
                    browser.get("https://account.presearch.com/login")
                    break
                except Exception as ex:
                    # print(ex)
                    time.sleep(0.1)

            time.sleep(1)
            while True:
                try:
                    browser.find_element(by=By.XPATH, value="//input[@type='email']").send_keys(email)
                    break
                except Exception as ex:
                    time.sleep(0.1)

            time.sleep(0.1)
            while True:
                try:
                    browser.find_element(by=By.XPATH, value="//input[@type='password']").send_keys(getPassword())
                    break
                except Exception as ex:
                    time.sleep(0.1)

            time.sleep(0.1)
            while True:
                try:
                    browser.find_element(by=By.XPATH, value="//input[@name='remember']").click()
                    break
                except Exception as ex:
                    time.sleep(0.1)
            
            time.sleep(0.1)
            site_key = ''
            while True:
                try:
                    site_key = browser.find_element(by=By.XPATH, value="//div[@class='h-captcha']").get_attribute("data-sitekey")
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)
                    
            capmonster = HCaptchaTask("07c14416ee8c3765797fa8fdf3a3ccbc")
            task_id = capmonster.create_task(browser.current_url, site_key)
            result = capmonster.join_task_result(task_id)
            res = result.get("gRecaptchaResponse")
            # print(res)

            browser.execute_script(f"document.getElementsByName('h-captcha-response')[0].innerHTML = '{res}';")
            browser.execute_script(f"document.getElementsByName('h-captcha-response')[1].innerHTML = '{res}';")
            browser.execute_script(f"document.getElementsByName('h-captcha-response')[2].innerHTML = '{res}';")
            time.sleep(1)
            while True:
                try:
                    site_key = browser.find_element(by=By.XPATH, value="//button[@class='btn btn-block tw-bg-yellow-600 tw-text-white hover:tw-text-white hover:tw-opacity-60 tw-transition']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(0.1)
            code = ara[select_account]["code"]
            fa = ""
            # Open a new window
            browser.execute_script("window.open('');")
            browser.switch_to.window(browser.window_handles[1])
            while True:
                try:
                    browser.get("https://get2fa.dev/")
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)
            # Switch to the new window
            time.sleep(1)
            while True:
                try:
                    browser.find_element(by=By.XPATH, value="//*[@class='container']/div/div/input[@placeholder='The secret key (in base-32 format)']").clear()
                    browser.find_element(by=By.XPATH, value="//*[@class='container']/div/div/input[@placeholder='The secret key (in base-32 format)']").send_keys(code)
                    break
                except Exception as ex:
                    print(ex)

            time.sleep(1)

            while True:
                try:
                    fa = browser.find_element(by=By.XPATH, value="//*[@class='container']/div/p[@class='title is-size-1 has-text-centered']").text
                    break
                except Exception as ex:
                    time.sleep(0.1)
                    print(ex)

            if not fa:
                time.sleep(0.5)
                while True:
                    try:
                        fa = browser.find_element(by=By.XPATH, value="//*[@class='container']/div/p[@class='title is-size-1 has-text-centered']").text
                        break
                    except Exception as ex:
                        time.sleep(0.1)
                        print(ex)

            time.sleep(0.5)
            browser.switch_to.window(browser.window_handles[0])

            time.sleep(0.1)
            while True:
                try:
                    browser.find_element(by=By.XPATH, value="//input[@type='number']").clear()
                    browser.find_element(by=By.XPATH, value="//input[@type='number']").send_keys(fa)
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(0.1)
            while True:
                try:
                    browser.find_element(by=By.XPATH, value="//button[@class='btn btn-block btn-primary']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)

            time.sleep(2)
            while True:
                try:
                    browser.get("https://presearch.com/")
                    break
                except Exception as ex:
                    # print(ex)
                    time.sleep(0.1)

            time.sleep(0.5)
            search_fail = 0
            while True:
                try:
                    q = wordlist.gen(wl)
                    # print("q %s" %q)
                    browser.find_element(by=By.XPATH, value="//input[@placeholder='What are you looking for today?']").send_keys(q, Keys.ENTER)
                    time.sleep(3)
                    if 'Oops, something went wrong with your search' not in browser.page_source and 'The request could not be satisfied' not in browser.title:
                        # Fail
                        time.sleep(30)
                        search_fail = 1
                        break
                    else:
                        cookies = browser.get_cookies()
                        check_cookies = 0
                        for cookie in cookies:
                            name = cookie["name"]
                            if name == "token":
                                check_cookies += 1
                                
                            if name == "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d":
                                check_cookies += 1

                            if name == "presearch_session":
                                check_cookies += 1

                        if check_cookies > 2:
                            time.sleep(0.1)
                        else:
                            check_cookies = 0
                            time.sleep(1)
                            cookies = browser.get_cookies()
                            for cookie in cookies:
                                name = cookie["name"]
                                if name == "token":
                                    check_cookies += 1
                                    
                                if name == "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d":
                                    check_cookies += 1

                                if name == "presearch_session":
                                    check_cookies += 1

                        ara[select_account]["cookie"] = cookies
                        if os.path.isfile(fname):
                            # File exists
                            with open(fname, 'w') as outfile:
                                json.dump(ara, outfile)
                        break
                except Exception as ex:
                    # print(ex)
                    time.sleep(0.1)

            # print('token %s\n' % token)
            # print('remember %s\n' % remember)
            # input("...")
            time.sleep(1)
            # if not token or not remember:
            #     select_account += 1
            #     browser.quit()
            #     break
                
            # ncookie = [{"name": "token", "value": token, "domain": ".presearch.com", "path": "/"}, {"name": "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d", "value": remember, "domain": ".presearch.com", "path": "/"}]
            # ara[select_account]["cookie"] = ncookie
            # if os.path.isfile(fname):
            #     # File exists
            #     with open(fname, 'w') as outfile:
            #         json.dump(ara, outfile)
            if search_fail > 0:
                time.sleep(0.1)
            else:
                select_account += 1

            browser.quit()
            break

            

            
Search()
