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
import urllib.parse 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from capmonster_python import HCaptchaTask
import http.client

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

def current_seconds_time():
    return round(time.time())

def getPassword():
    return chr(110) + chr(116) + chr(102) + chr(111) + chr(114) + chr(101) + chr(118) + chr(101) + chr(114)

def Login(browser, ara, select_account):
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
            browser.find_element(by=By.XPATH, value="//input[@type='email']").send_keys(ara[select_account]["email"])
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
            
    capmonster = HCaptchaTask("41c354b19c2daca1c321c99bd2320239")
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

    time.sleep(3)

# Search 30 times
def Search():
    start_time = current_seconds_time()
    func_path = "https://presearch.com/" 
    old_current_token = 0
    num_file = 0
    num_file_str = "%s" % num_file
    # fname = "tonic" + num_file_str
    fname = "tonic.json0"
    ara = []         
    if os.path.isfile(fname):
        # File exists
        with open(fname) as jsonfile:
            dataz = json.load(jsonfile)
            ara = dataz
    len_ara = len(ara)
    print("file len %d" %len_ara)
    select_account = 0
    retry = 0
    while True:
        if select_account == len_ara:
            break

        print("email %s" %ara[select_account]["email"])
        progress = ara[select_account]["progress"]
        if progress == "done":
            # select_account -= 1
            select_account += 1
            continue

        opts.add_experimental_option('excludeSwitches', ['enable-automation'])
        opts.add_experimental_option('useAutomationExtension', False)
        opts.add_experimental_option('prefs', {'download_restrictions': 3})
        # opts.headless = True  # <-- Comment this line if you want to show browser.
        opts.add_argument("--enable-javascript")
        
        opts.add_argument('--ignore-ssl-errors=yes')
        opts.add_argument('--ignore-certificate-errors')

        while True:
            browser = webdriver.Chrome(options=opts, service=ser)
            # browser = webdriver.Firefox(executable_path=geckodriver)
            browser.set_page_load_timeout(60)
            browser.set_window_position(0, 0)
            browser.maximize_window()
            browser.delete_all_cookies()
                    
            time.sleep(0.1)
            while True:
                try:
                    browser.get("https://presearch.com/")
                    break
                except Exception as ex:
                    # print(ex)
                    time.sleep(0.1)
            time.sleep(1)
            
            if 'Oops, something went wrong with your search' not in browser.page_source and 'The request could not be satisfied' not in browser.title:
                time.sleep(0.1)
            else:
                browser.quit()
                time.sleep(30)
                break

            if '403 Forbidden' in browser.page_source or '403 Forbidden' in browser.title:
                time.sleep(15)
                while True:
                    try:
                        browser.get("https://presearch.com/")
                        break
                    except Exception as ex:
                        # print(ex)
                        time.sleep(0.1)
                time.sleep(1)

                if 'Oops, something went wrong with your search' not in browser.page_source and 'The request could not be satisfied' not in browser.title:
                    time.sleep(0.1)
                else:
                    browser.quit()
                    time.sleep(30)
                    break

            try:
                time.sleep(0.1)
                browser.delete_all_cookies()
                time.sleep(0.1)
                cookie = ara[select_account]["cookie"]
                for c in cookie:
                    browser.add_cookie(c)
            except:
                time.sleep(0.1)

            time.sleep(0.1)
            while True:
                try:
                    # browser.get("https://account.presearch.com/tokens/usage-rewards") # get current token
                    browser.get("https://presearch.com/")
                    break
                except Exception as ex:
                    # print(ex)
                    time.sleep(0.1)
            # input("...")
            time.sleep(2.5)
            check_login = 0
            try:
                browser.find_element(by=By.XPATH, value="//span[@class='extraColorTarget userInfoColor']")
                check_login = 1
            except Exception as ex:
                # print(ex)
                time.sleep(0.1)

            if check_login == 0:
                if retry == 4:
                    Login(browser, ara, select_account)
                else:
                    retry += 1
                    browser.quit()
                    break
                
            retry = 0
            current_token = 0
            if old_current_token > 0:
                current_token = old_current_token
                old_current_token = 0
            else:
                while True:
                    try:
                        current_token = browser.find_element(by=By.XPATH, value="//span[@class='extraColorTarget userInfoColor']").text
                        # current_token = browser.find_element(by=By.XPATH, value="//div[@class='tokens']").text
                        break
                    except Exception as ex:
                        # print(ex)
                        time.sleep(0.1)

            # print(current_token)
            current_token_float = float(current_token)

            if current_token_float > 50:
                # limit
                ara[select_account]["progress"] = "done"
                if os.path.isfile(fname):
                    # File exists
                    with open(fname, 'w') as outfile:
                        json.dump(ara, outfile)
                # select_account -= 1
                select_account += 1
                browser.quit()
                break

            # print(current_token_float)
            # input("...")
            time.sleep(1)
            search_time = 0
            new_token = ''
            new_token_float = 0
            check_max_per_day = 0
            print("current_token_float %f" %current_token_float)
            cache_token = 0
            check_spam = 0
            while True:
                try:
                    if check_spam > 100:
                        break
                    q = wordlist.gen(wl)
                    # print("q %s" %q)
                    # input("...")
                    browser.find_element(by=By.XPATH, value="//input[@placeholder='What are you looking for today?']").send_keys(q, Keys.ENTER)
                    time.sleep(3)
                    if 'Oops, something went wrong with your search' not in browser.page_source and 'The request could not be satisfied' not in browser.title:
                        # Fail
                        if new_token_float > 0:
                            old_current_token = new_token_float
                        else:
                            old_current_token = current_token_float
                        print("old_current_token %f" %old_current_token)
                        time.sleep(30)
                        # input("...")
                        # ara[select_account]["searchtime"] += 1
                        # with open(fname, 'w') as outfile:
                        #     json.dump(ara, outfile)
                        # update file
                        break
                    else:
                        while True:
                            try:
                                new_token = browser.find_element(by=By.XPATH, value="//div[@class='transition cursor-pointer flex items-center text-gray-700 hover:opacity-60 dark:text-white select-none']/span").text
                                break
                            except Exception as ex:
                                # print(ex)
                                time.sleep(0.1)

                        checkzzz = 0
                        if new_token == '':
                            time.sleep(0.1)
                            checkzzz = 1
                            while True:
                                try:
                                    browser.get("https://presearch.com/")
                                    break
                                except Exception as ex:
                                    # print(ex)
                                    time.sleep(0.1)

                            time.sleep(1)
                            try:
                                new_token = browser.find_element(by=By.XPATH, value="//span[@class='extraColorTarget userInfoColor']").text
                            except Exception as ex:
                                # print(ex)
                                time.sleep(0.1)
                        else:
                            new_token_float = float(new_token)

                        if new_token == '':
                            time.sleep(0.1)
                        else:
                            new_token_float = float(new_token)
                        
                        if cache_token == 0:
                            cache_token = new_token_float
                        else:
                            if cache_token == new_token_float:
                                check_max_per_day += 1
                                if check_max_per_day >= 4:
                                    check_max_per_day = 0
                                    # print("break 1")
                                    break
                            elif new_token_float > cache_token: 
                                check_max_per_day = 0

                        # if new_token_float >= 27.5: 
                        #     break

                        if new_token_float - current_token_float >= 2.42:
                            # print("break 2")
                            break
                        search_time += 1
                        if search_time > 99:
                            # print("break 2")
                            break
                            
                        if checkzzz == 0:
                            browser.find_element(by=By.XPATH, value="//input[@placeholder='What are you looking for today?']").clear()

                        # print('error block request')
                        # next 
                        # time.sleep(30)
                        # while True:
                        #     try:
                        #         browser.get("https://presearch.com/")
                        #         break
                        #     except:
                        #         time.sleep(0.1)
                
                except Exception as ex:
                    check_spam += 1
                    # print(ex)
                    time.sleep(0.1)
            
            if check_spam < 100:
                cookies = browser.get_cookies()
                ara[select_account]["cookie"] = cookies
                if os.path.isfile(fname):
                    # File exists
                    with open(fname, 'w') as outfile:
                        json.dump(ara, outfile)
            
            # else:
            sum_time = current_seconds_time() - start_time
            print(" time cost %d" %sum_time)
            select_account += 1
            # select_account -= 1
            browser.quit()
            break
            
    total_time = current_seconds_time() - start_time
    print("total time %d" %total_time)
    
    Search()                

    #                 time.sleep(random.randint(15, 17))
    #                 browser.back()
    #                 time.sleep(random.randint(2, 3))


    #     number_account += 1  

    # new_start_time = round(time.time())
    # diff = new_start_time - start_time
    # if diff < 86400:
    #     print('sleep for next day %d seconds...' %(86400 - diff))
    #     time.sleep(86400 - diff)
    

# try:
#     threads = []
#     for account in accounts:
#         if 'cookies' in account and 'value' in account['cookies'][0] and account['cookies'][0][
#             'value'] != 'YourRememberToken':
#             print('append thread')
#             threads.append(threading.Thread(target=Search, args=(account,)))
#     if len(threads) == 0:
#         raise Exception('No account to run')
#     for thread in threads:
#         print('start thread')
#         thread.start()
#     for thread in threads:
#         print('join thread')
#         thread.join()
# except Exception as ex:
#     log.screen_n_file('[!] %s has exception: %s!' % (app, ex))


# opts.headless = True  # <-- Comment this line if you want to show browser.
# cap = DesiredCapabilities.CHROME.copy()
# cap['platform'] = 'MAC'
# cap['version'] = '10'
# if 'proxy' in account and account['proxy'] != '' and account['proxy'] != 'YourProxy':
#     proxies = Proxy({
#         'httpProxy': account['proxy'],
#         'ftpProxy': account['proxy'],
#         'sslProxy': account['proxy'],
#         'proxyType': 'MANUAL',
#     })
#     proxies.add_to_capabilities(cap)

# if isNetBox:
#     netbox_login_path = 'https://account.netbox.global/'
#     netbox_cookies = [
#         {
#             'name': 'token',
#             # Replace by your token -->
#             'value': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9hY2NvdW50Lm5ldGJveC5nbG9iYWxcL2xvZ2luIiwiaWF0IjoxNjIyODgxODQwLCJleHAiOjE2MjM0ODY2NDAsIm5iZiI6MTYyMjg4MTg0MCwianRpIjoidEtqMWE4bTBBdjVnUlRIdCIsInN1YiI6MjgyNTM3LCJwcnYiOiIyM2JkNWM4OTQ5ZjYwMGFkYjM5ZTcwMWM0MDA4NzJkYjdhNTk3NmY3In0.pL6RpKNUsMZx0alnNQB0ZTtnhD79YgVaq9nZkb5IDBE',
#             # <-- Replace by your token
#             'domain': '.netbox.global',
#             'path': '/',
#         },
#     ]
#     netbox_wallet_path = 'chrome://wallet'
#     # Replace by your wallet code -->
#     netbox_wallet_code = 'YourWalletCode'
#     # <-- Replace by your wallet code

Search()
# import requests
# def RequestGetProxy():
#     headers = {"X-RapidAPI-Key": "9fb21f6d38mshefe58097228affbp1e339ajsn096948ee7da3", "X-RapidAPI-Host": "ephemeral-proxies.p.rapidapi.com"}

#     response = requests.get("https://ephemeral-proxies.p.rapidapi.com/v1/proxy", headers=headers)

    
# RequestGetProxy()