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

namez = "dragon"
fnamez = "champagne"
app = 'PreSearch'
register = 'https://account.presearch.org/signup?rid=2508931'
url_base = "https://account.presearch.com/" 
url_user_profile = "https://account.presearch.com/user-profile"
url_referral_terms = "https://account.presearch.com/referral-terms"
url_privacy_settings = "https://account.presearch.com/privacy-settings"
# url_user_profile = "https://account.presearch.com/user-profile"

user_name = 'ginandtonicbarneystinsonhimym.' + namez
last_name = '@gmail.com'

wl = wordlist.get()
presearch_max_count = 30
min_pre = 50

DRIVER_BIN = os.path.join(os.getcwd(), "Drivers/chromedriver104linux")
waiter = 0

chromedriver_path = DRIVER_BIN

now = datetime.now()


opts = Options()
ser = Service(DRIVER_BIN)
opts.binary_location = "/usr/bin/google-chrome"

opts.add_argument("--headless")
opts.add_argument("--remote-debugging-port=9222")
opts.add_argument("--disable-extensions")
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-dev-shm-usage")
opts.add_argument("--disable-setuid-sandbox")

def getUserNameByCount(count):
    count_str = "%s" % count
    name = user_name + count_str + last_name
    return name

def getPassword():
    return chr(110) + chr(116) + chr(102) + chr(111) + chr(114) + chr(101) + chr(118) + chr(101) + chr(114)


# Search 30 times
def Search():
    func = "Multi-Account Search"
    func_path = 'https://engine.presearch.org'
    file_number = 0
    number_name = 0

    while True:
        # Browser config
        # opts = Options()
        # opts.binary_location = os.path.expanduser("/Applications/Brave Browser.app/Contents/MacOS/Brave Browser")
        # opts.add_experimental_option('excludeSwitches', ['enable-automation'])
        # opts.add_experimental_option('useAutomationExtension', False)
        # opts.add_experimental_option('prefs', {'download_restrictions': 3})
        # opts.headless = True  # <-- Comment this line if you want to show browser.
        # opts.add_argument("--enable-javascript")
        opts.add_argument("--ignore-certificate-errors")

        while True:
            browser = webdriver.Chrome(options=opts, service=ser)
            # browser = webdriver.Firefox(executable_path=geckodriver)
            # browser.set_page_load_timeout(60)
            # browser.set_window_position(0, 0)
            # browser.maximize_window()
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
                        # browser.find_element_by_xpath("//a[@href='https://presearch.org/login']").click()
                        browser.find_element(by=By.XPATH, value="//a[@href='https://account.presearch.com/login?signin']").click()  # by=By.ID, By.TAG_NAME, By.CLASS_NAME, By.NAME
                        break
                    except Exception as ex:
                        time.sleep(0.1)
                time.sleep(1)
                while True:
                    try:
                        browser.find_element(by=By.XPATH, value="//a[@href='#register-form']").click()
                        # browser.find_element_by_xpath("//a[@class='register-form-show btn btn-block tw-bg-presearch-blue tw-text-white hover:tw-text-white dark:tw-bg-blue-600 hover:tw-opacity-70 tw-transition']").click()
                        break
                    except Exception as ex:
                        time.sleep(0.1)

                username = getUserNameByCount(number_name)
                # print('username %s\n' % username)
                time.sleep(1)
                while True:
                    try:
                        browser.find_element(by=By.XPATH, value="//input[@placeholder='Email Address']").send_keys(username)
                        # browser.find_element_by_xpath("//input[@placeholder='Email Address']").send_keys(username)
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                password = getPassword()
                while True:
                    try:
                        browser.find_element(by=By.XPATH, value="//*[@class='login-box']/div/div/form/div/input[@placeholder='Password']").send_keys(password)
                        # browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/input[@placeholder='Password']").send_keys(password)
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                while True:
                    try:
                        browser.find_element(by=By.XPATH, value="//input[@placeholder='Confirm Password']").send_keys(password)
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                while True:
                    try:
                        browser.find_element(by=By.XPATH, value="//input[@name='agreed_to_terms']").click()
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                site_key = ''
                while True:
                    try:
                        site_key = browser.find_element(by=By.XPATH, value="//div[@class='h-captcha']").get_attribute("data-sitekey")
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)
                        
                capmonster = HCaptchaTask("8efd657d0d151110a0be0d69c9dc0678")
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
                        browser.find_element(by=By.XPATH, value="//button[@class='btn btn-lg btn-block tw-bg-yellow-600 tw-text-white hover:tw-text-white hover:tw-opacity-60 tw-transition']").click()
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                time.sleep(3)
                
                while True:
                    try:
                        browser.get(url_user_profile)
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                time.sleep(1)
                check_time = 0
                while True:
                    try:
                        check_time += 1
                        if check_time > 50:
                            while True:
                                try:
                                    browser.get(url_user_profile)
                                    break
                                except Exception as ex:
                                    print(ex)
                                    time.sleep(0.1)
                            time.sleep(1)
                            check_time = 0
                        browser.find_element(by=By.XPATH, value="//input[@id='name']").send_keys("NGUYEN THAC HUNG")
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                time.sleep(0.1)
                while True:
                    try:
                        num = "%s" % number_name
                        browser.find_element(by=By.XPATH, value="//input[@id='display_name']").send_keys(namez + num)
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)
                        
                time.sleep(0.1)
                while True:
                    try:
                        browser.find_element(by=By.XPATH, value="//select[@name='gender']/option[@value='M']").click()
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                time.sleep(0.1)
                while True:
                    try:
                        browser.find_element(by=By.XPATH, value="//select[@name='country_id']/option[@value='704']").click()
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                time.sleep(0.1)
                while True:
                    try:
                        browser.find_element(by=By.XPATH, value="//button[@type='submit']").click()
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)
                
                time.sleep(3)

                while True:
                    try:
                        browser.get(url_privacy_settings)
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                time.sleep(0.1)
                while True:
                    try:
                        browser.find_element(by=By.XPATH, value="//button[@class='btn btn-primary']").click()
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                time.sleep(3)

                code = ""
                while True:
                    try:
                        code = browser.find_element(by=By.XPATH, value="//*[@id='main']/div/code").text
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)
                print("2fa %s" %code)
                time.sleep(0.1)

                # solve 2fa
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
                check_2fa = 0
                while True:
                    try:
                        if check_2fa > 30:
                            check_2fa = 0
                            while True:
                                try:
                                    browser.get("https://get2fa.dev/")
                                    break
                                except Exception as ex:
                                    print(ex)
                                    time.sleep(0.1)
                            time.sleep(1)

                        browser.find_element(by=By.XPATH, value="//*[@class='container']/div/div/input[@placeholder='The secret key (in base-32 format)']").clear()
                        browser.find_element(by=By.XPATH, value="//*[@class='container']/div/div/input[@placeholder='The secret key (in base-32 format)']").send_keys(code)
                        break
                    except Exception as ex:
                        check_2fa += 1
                        print(ex)
                        time.sleep(0.1)

                time.sleep(0.5)

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

                browser.switch_to.window(browser.window_handles[0])

                time.sleep(0.1)
                while True:
                    try:
                        browser.find_element(by=By.XPATH, value="//input[@placeholder='000000']").clear()
                        browser.find_element(by=By.XPATH, value="//input[@placeholder='000000']").send_keys(fa)
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                time.sleep(0.1)
                while True:
                    try:
                        browser.find_element(by=By.XPATH, value="//button[@type='submit']").click()
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                time.sleep(3)
                check_success = 0
                try:
                    fail = browser.find_element(by=By.XPATH, value="//div[@class='alert alert-danger text-center']").text
                    if "Invalid code" in fail:
                        check_success = 0
                except Exception as ex:
                    # print(ex)
                    time.sleep(0.1)

                try:
                    success = browser.find_element(by=By.XPATH, value="//div[@class='alert alert-success text-center']").text
                    if "Two-Factor Authentication Activated" in success:
                        check_success = 1
                except Exception as ex:
                    # print(ex)
                    time.sleep(0.1)
                
                if not check_success:
                    browser.switch_to.window(browser.window_handles[1])

                    while True:
                        try:
                            browser.find_element(by=By.XPATH, value="//*[@class='container']/div/div/input[@placeholder='The secret key (in base-32 format)']").clear()
                            browser.find_element(by=By.XPATH, value="//*[@class='container']/div/div/input[@placeholder='The secret key (in base-32 format)']").send_keys(code)
                            break
                        except Exception as ex:
                            print(ex)

                    time.sleep(0.5)

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

                    browser.switch_to.window(browser.window_handles[0])

                    time.sleep(0.1)
                    while True:
                        try:
                            browser.find_element(by=By.XPATH, value="//input[@placeholder='000000']").clear()
                            browser.find_element(by=By.XPATH, value="//input[@placeholder='000000']").send_keys(fa)
                            break
                        except Exception as ex:
                            print(ex)
                            time.sleep(0.1)

                    time.sleep(0.1)
                    while True:
                        try:
                            browser.find_element(by=By.XPATH, value="//button[@type='submit']").click()
                            break
                        except Exception as ex:
                            print(ex)
                            time.sleep(0.1)


                time.sleep(1)

                while True:
                    try:
                        browser.get(url_referral_terms)
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                time.sleep(0.1)
                while True:
                    try:
                        browser.find_element(by=By.XPATH, value="//input[@type='checkbox']").click()
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                time.sleep(0.1)
                while True:
                    try:
                        browser.find_element(by=By.XPATH, value="//button[@type='submit']").click()
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                time.sleep(1)
                while True:
                    try:
                        browser.get("https://presearch.com/")
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)

                time.sleep(0.1)
                check_search = 0
                while True:
                    try:
                        if check_search > 30:
                            check_search = 0
                            while True:
                                try:
                                    browser.get("https://presearch.com/")
                                    break
                                except Exception as ex:
                                    print(ex)
                                    time.sleep(0.1)
                            time.sleep(1)

                        q = wordlist.gen(wl)
                        browser.find_element(by=By.XPATH, value="//input[@placeholder='What are you looking for today?']").send_keys(q, Keys.ENTER)
                        break
                    except Exception as ex:
                        check_search += 1
                        print(ex)
                        time.sleep(0.1)
                
                time.sleep(1)

                while True:
                    try:
                        browser.get("https://presearch.com/")
                        break
                    except Exception as ex:
                        print(ex)
                        time.sleep(0.1)
                time.sleep(1)
                # token = ""
                # presearch_session = ""
                
                cookies = browser.get_cookies()
                # print(cookies)
                # for cookie in cookies:
                #     name = cookie["name"]
                #     if name == "token":
                #         token = cookie["value"]
                #         # print('token %s\n' % token)
                #     if name == "presearch_session":
                #         presearch_session = cookie["value"]
                #         # print('presearch_session %s\n' % presearch_session)

                # if not token or not presearch_session:
                #     time.sleep(1)
                #     cookies = browser.get_cookies()
                    
                #     for cookie in cookies:
                #         name = cookie["name"]
                #         if name == "token":
                #             token = cookie["value"]
                #             # print('token %s\n' % token)
                #         if name == "presearch_session":
                #             presearch_session = cookie["value"]
                #             # print('presearch_session %s\n' % presearch_session)

                # if not token or not presearch_session:
                #     time.sleep(1)
                #     cookies = browser.get_cookies()
                    
                #     for cookie in cookies:
                #         name = cookie["name"]
                #         if name == "token":
                #             token = cookie["value"]
                #         if name == "presearch_session":
                #             presearch_session = cookie["value"]

                # print('token %s\n' % token)
                # print('presearch_session %s\n' % presearch_session)
                # input("...")
                time.sleep(1)
                if not cookies:
                    browser.quit()
                    break
                # ncookie = [{"name": "token", "value": token, "domain": ".presearch.com", "path": "/"}, {"name": "presearch_session", "value": presearch_session, "domain": ".presearch.com", "path": "/"}]
                check_limit = 0
                num_file = "%s" % file_number
                fname = fnamez + num_file              
                ip = ""
                data = {}
                try:
                    ip = os.popen('dig +short myip.opendns.com @resolver1.opendns.com').readlines(-1)[0].strip()
                except Exception as ex:
                    time.sleep(0.1)
                    
                data = {"email":username, "cookie":cookies, "code":code, "progress":"todo", "ip":ip}
                if os.path.isfile(fname):
                    # File exists
                    ara = []
                    with open(fname) as jsonfile:
                        dataz = json.load(jsonfile)
                        dataz.append(data)
                        ara = dataz
                    len_ara = len(ara)
                    if len_ara > 280:
                        file_number = file_number + 1
                        check_limit = 1
                    else:
                        with open(fname, 'w') as outfile:
                            json.dump(ara, outfile)
                else: 
                    # Create file
                    with open(fname, 'w') as outfile:
                        array = []
                        array.append(data)
                        json.dump(array, outfile)

                if check_limit > 0:
                    num_file = "%s" % file_number
                    fname = fnamez + num_file     
                    if os.path.isfile(fname):
                        # File exists
                        ara = []
                        with open(fname) as jsonfile:
                            dataz = json.load(jsonfile)
                            dataz.append(data)
                            ara = dataz
                        len_ara = len(ara)
                        if len_ara > 280:
                            file_number = file_number + 1
                            check_limit = 1
                        else:
                            with open(fname, 'w') as outfile:
                                json.dump(ara, outfile)
                    else: 
                        # Create file
                        with open(fname, 'w') as outfile:
                            array = []
                            array.append(data)
                            json.dump(array, outfile)

                number_name += 1
                browser.quit()
                break

            except Exception as ex:
                log.screen_n_file('[!] %s has exception: %s!' % (app, ex))
  

    # new_start_time = round(time.time())
    # diff = new_start_time - start_time
    # if diff < 86400:
    #     print('sleep for next day %d seconds...' %(86400 - diff))
    #     time.sleep(86400 - diff)
    
    # start_time = round(time.time())
    # Search()

    # coo = [{"name": "token", "value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2NTk5NzUwODIsImV4cCI6MTY2MDU3OTg4MiwidXNlcl9pZCI6NDMxOTA1MSwidXNlcl9hcGlfa2V5IjpudWxsLCJjcyI6MSwiYmV0YXMiOltdfQ.EMRX92AUuw9ffZJ7sO8WOa01jmtWEEpMN_tSpdPuAECjnKJjYEln98udQICYvzpbpoMdDUAUab0zTxa2rNwlsdcPPulBKXYFRhOoe-xYdfc_SEjjn3mT577YYHPh1_AzTjtpEl1M6dQPcDmC5boWN6dq00nz8a845SjH7oZZThOJFLLiWP-C-qtVL0rsQHi9RI7_-algBzOSYsFJYBqs5JjL6LXCbhP43qk5v_KS-GFavPhChGg5GvY7i9Jdhiq4HaHo9bDB-hoUXLNxQ5kKG37t8W3PsYwFnN-arzLc-oMhur3uTGbHllXqvhjzcqrvYHozqL9wvZuL1rs6m6Z8Wg", "domain": ".presearch.com", "path": "/"}, {"name": "presearch_session", "value": "eyJpdiI6ImZpR3h2WW5pNUZmZ2I3WS9aZGxWalE9PSIsInZhbHVlIjoic3U1aHBGUEg2WStEOXdCRUlrZjhLcWRmRk5tRVhtaVZrZ1dEcU5tSU5meWY3NEFGUWJaaG9xSzNreVN5SHkxcHV5dEtJTms4SDBYNGhNeXdPaUxzRDczWmxKS0J2VzVRa3BOclNBSVpCOW1nT2k1Vm5EcWdzS3NTd2tCZGdYelIiLCJtYWMiOiI3YjBhZmIzZWYzNjA3ZDYwN2E5MGI3MzZkNjU0YjFlZWQxZWM4NTQ2NGQ5MzQ3YTYzMTQxMmZhMTkyZjI1ZDQzIn0%3D", "domain": ".presearch.com", "path": "/"}]

    # while True:
    #     try:
    #         browser.get("https://account.presearch.com/")
    #         break
    #     except:
    #         time.sleep(0.1)
    
    # browser.delete_all_cookies()
    # for c in coo:
    #     browser.delete_cookie(c['name'])
    #     browser.add_cookie(c)
    # while True:
    #     try:
    #         browser.get("https://account.presearch.com/")
    #         break
    #     except:
    #         time.sleep(0.1)

    
    # input("....")
Search()