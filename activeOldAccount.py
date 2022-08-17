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
from Modules import log, wordlist, captcha
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import urllib.parse as urlparse
from capmonster_python import NoCaptchaTaskProxyless

app = 'PreSearch'
register = 'https://presearch.org/signup?rid=2508931'
user_name = 'hungnguyenthac12081995.'
last_name = '@gmail.com'

wl = wordlist.get()
presearch_max_count = 30

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "Drivers/chromedriver94")
geckodriver = os.path.join(PROJECT_ROOT, "Drivers/geckodriver")
waiter = 0

opts = Options()
opts.binary_location = os.path.expanduser("/Applications/Brave Browser.app/Contents/MacOS/Brave Browser")

chromedriver_path = DRIVER_BIN

now = datetime.now()

def getUserNameByCount(count):
    count_str = "%s" % count
    name = user_name + count_str + last_name
    return name

def getPassword():
    return chr(110) + chr(116) + chr(102) + chr(111) + chr(114) + chr(101) + chr(118) + chr(101) + chr(114)


# accounts = ["hungnguyenthac12081995dd@gmail.com", "hungnguyenthac12081995cc@gmail.com", "hungnguyenthac12081995bb@gmail.com", "hungnguyenthac12081995aa@gmail.com", "hungnguyenthac12081995aaa@gmail.com", "hungnguyenthac12081995bbb@gmail.com", "hungnguyenthac12081995ccc@gmail.com", "hungnguyenthac12081995ddd@gmail.com", "hungnguyenthac12081995eee@gmail.com", "hungnguyenthac12081995fff@gmail.com", "hungnguyenthac12081995ggg@gmail.com", "hungnguyenthac12081995hhh@gmail.com", "hungnguyenthac12081995iii@gmail.com", "hungnguyenthac12081995jjj@gmail.com", "hungnguyenthac12081995kkk@gmail.com", "hungnguyenthac12081995lll@gmail.com", "hungnguyenthac12081995mmm@gmail.com", "hungnguyenthac12081995nnn@gmail.com", "hungnguyenthac12081995ooo@gmail.com", "hungnguyenthac12081995ppp@gmail.com", "hungnguyenthac12081995qqq@gmail.com", "hungnguyenthac12081995rrr@gmail.com", "hungnguyenthac12081995sss@gmail.com", "hungnguyenthac12081995ttt@gmail.com", "hungnguyenthac12081995uuu@gmail.com", "hungnguyenthac12081995vvv@gmail.com", "hungnguyenthac12081995www@gmail.com", "hungnguyenthac12081995xxx@gmail.com", "hungnguyenthac12081995yyy@gmail.com", "hungnguyenthac12081995zzz@gmail.com", "hungnguyenthac12081995.001@gmail.com", "hungnguyenthac12081995.002@gmail.com", "hungnguyenthac12081995.003@gmail.com", "hungnguyenthac12081995.004@gmail.com", "hungnguyenthac12081995.005@gmail.com", "hungnguyenthac12081995.006@gmail.com", "hungnguyenthac12081995.007@gmail.com", "hungnguyenthac12081995.008@gmail.com", "hungnguyenthac12081995.009@gmail.com", "hungnguyenthac12081995.010@gmail.com", "hungnguyenthac12081995.011@gmail.com", "hungnguyenthac12081995.012@gmail.com", "hungnguyenthac12081995.013@gmail.com", "hungnguyenthac12081995.014@gmail.com", "hungnguyenthac12081995.015@gmail.com", "hungnguyenthac12081995.016@gmail.com", "hungnguyenthac12081995.017@gmail.com", "hungnguyenthac12081995.018@gmail.com", "hungnguyenthac12081995.019@gmail.com", "hungnguyenthac12081995.020@gmail.com", "hungnguyenthac12081995.021@gmail.com", "hungnguyenthac12081995.022@gmail.com", "hungnguyenthac12081995.023@gmail.com", "hungnguyenthac12081995.024@gmail.com", "hungnguyenthac12081995.025@gmail.com", "hungnt12081995zzy@gmail.com", "hungnt12081995yyx@gmail.com", "hungnt12081995yyz@gmail.com", "hungnt12081995xxy@gmail.com", "hungnt12081995zzx@gmail.com", "hungnguyenthac12081995@gmail.com", "hungnt12081995zzz@gmail.com", "hungnguyenthac12081995xyz@gmail.com", "hungnguyenthac.vcc1208@gmail.com", "hungnguyen12081995zzz@gmail.com", "zelly0kun1@gmail.com", "hungnguyenthac@vccorp.vn"]
# def solveCaptcha():
    # try:
    #     recaptcha = browser.find_element_by_xpath(
    #         "//iframe[contains(@title, 'reCAPTCHA')]")
    #     sitekey = ''
    #     for query in urlparse.urlparse(
    #             recaptcha.get_attribute('src')).query.split(
    #         '&'):
    #         if 'k=' in query:
    #             sitekey = query.split('=')[1]
    #     token = rc.reCaptcha(sitekey, browser.current_url)
    #     if token != 'Expired':
    #         log.screen_n_file(
    #             '    [+] Captcha response is %s.' % (
    #                     token[:7] + '...' + token[-7:]))
    #         # Run callback function
    #         browser.execute_script('''
    #             function call_cbf(token) {
    #                 let widgetId = 0;
    #                 let widget = ___grecaptcha_cfg.clients[widgetId];
    #                 let callback = undefined;
    #                 for (let k1 in widget) {
    #                     let obj = widget[k1];
    #                     if (typeof obj !== "object") continue;
    #                     for (let k2 in obj) {
    #                         if (obj[k2] === null) continue;
    #                         if (typeof obj[k2] !== "object") continue;
    #                         if (obj[k2].callback === undefined) continue;
    #                         callback = obj[k2].callback;
    #                         break
    #                     }
    #                     if (callback === undefined) break;
    #                 }
    #                 callback.bind(this);
    #                 callback(token);
    #             }
    #             call_cbf(arguments[0]);
    #         ''', token)
    #         time.sleep(1)
    #         browser.find_element_by_xpath(
    #             "//button[contains(@class, 'button button-secondary button-large text-1-5rem text-bold mx-1')]").click()
    #         time.sleep(10)
    #         browser.switch_to.window(gameTab)
    #         for i in range(-5, 5):
    #             for j in range(-5, 5):
    #                 CanvasDraw(browser, 210 + i, -115 + j)  # Click to Close button
    #         time.sleep(2)
    #         CanvasDraw(browser, 0, 50)  # Click to Claim button if 1 button
    #         CanvasDraw(browser, -70,
    #                     60)  # Click to Claim button if 2 buttons, included Change Land button.
    #         time.sleep(5)
    #         if len(browser.window_handles) > 1:
    #             isTransactionExpired = True
    #             log.screen_n_file('  [-] Transaction is expired.')
    #         break
    #     else:
    #         # Try to solve captcha again
    #         browser.execute_script('''
    #             window.grecaptcha.reset();
    #         ''')
    #         time.sleep(1)
    #         tryTime -= 1
    #         log.screen_n_file(
    #             '    [-] Captcha is expired! %d times left to try.' % tryTime)
    #         # notification.notify(app, 'Captcha is expired! %d times left to try.' % tryTime)
    #         if tryTime <= 0:
    #             browser.close()
    #             time.sleep(1)
    #             isCaptchaExpired = True
    #             break
    # except:
    #     pass

# Search 30 times
def ResetToken():

    # with open('oldAcc.json') as jsonfile:
    #     dataz = json.load(jsonfile)
    #     for data in dataz:
    #         print(data)
    fname = "a.json"
    accounts = []
    with open(fname) as jsonfile:
        accounts = json.load(jsonfile)

    # input("...")
    for account in accounts:
        browser = webdriver.Chrome(executable_path=chromedriver_path)
        # browser = webdriver.Firefox(executable_path=geckodriver)
        browser.set_page_load_timeout(60)
        browser.set_window_position(0, 0)
        browser.maximize_window()
        browser.delete_all_cookies()

        username = account["email"]
        code = account["code"]
        print('username %s\n' % username)
        password = getPassword()

        try:
            browser.get(register)
            time.sleep(0.3)
            while True:
                try:
                    browser.find_element_by_xpath("//a[@href='https://presearch.org/login']").click()
                    break
                except:
                    time.sleep(0.1)
            
            time.sleep(1)

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

            while True:
                try:
                    # recaptcha = browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/div/div/iframe[@title='reCAPTCHA']")
                    recaptcha = browser.find_element_by_xpath("//iframe[contains(@title, 'reCAPTCHA')]")
                    print("recaptcha")
                    sitekey = ''
                    for query in urlparse.urlparse(
                            recaptcha.get_attribute('src')).query.split(
                        '&'):
                        if 'k=' in query:
                            sitekey = query.split('=')[1]

                    captcha = NoCaptchaTaskProxyless(client_key="da52ffbb815fb08c8be6d349d229480b")
                    taskId = captcha.createTask(browser.current_url, sitekey)
                    response = captcha.joinTaskResult(taskId)
                    # browser.execute_script(f"document.getElementById('g-recaptcha-response')[0].innerHTML = '{response}';")
                    browser.execute_script('''
                            document.getElementById("g-recaptcha-response").innerHTML=arguments[0];
                        ''', response)

                    print(response)
                    # time.sleep(11)
                    # while True:
                    #     try:
                    #         browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/button[@class='btn btn-lg btn-block tw-bg-yellow-600 tw-text-white hover:tw-text-white hover:tw-opacity-60 tw-transition']").click()
                    #     except Exception as ex:
                    #         print(ex)
                    #         time.sleep(0.1)
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)    

            # input("Solve Captcha then Enter...")

            time.sleep(0.1)
            
            while True:
                try:
                    browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/button[@type='submit']").click()
                    break
                except Exception as ex:
                    print(ex)
                    time.sleep(0.1)
            # submit turn 1

            time.sleep(2)
            check_login = 0
            try:
                browser.find_element_by_xpath("//div[@class='ajax-error form-group text-danger text-center']")
                check_login = 1
            except Exception as ex:
                check_login = 0
                print(ex)

            if check_login:
                time.sleep(180)

                browser.get(register)
                time.sleep(0.3)
                while True:
                    try:
                        browser.find_element_by_xpath("//a[@href='https://presearch.org/login']").click()
                        break
                    except:
                        time.sleep(0.1)
                
                time.sleep(1)

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
                        time.sleep(0.1)

                time.sleep(0.1)
                
                while True:
                    try:
                        browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/div/div[@class='checkbox blue text-left']").click()
                        break
                    except Exception as ex:
                        time.sleep(0.1)

                while True:
                    try:
                        # recaptcha = browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/div/div/iframe[@title='reCAPTCHA']")
                        recaptcha = browser.find_element_by_xpath("//iframe[contains(@title, 'reCAPTCHA')]")
                        print("recaptcha")
                        sitekey = ''
                        for query in urlparse.urlparse(
                                recaptcha.get_attribute('src')).query.split(
                            '&'):
                            if 'k=' in query:
                                sitekey = query.split('=')[1]

                        captcha = NoCaptchaTaskProxyless(client_key="da52ffbb815fb08c8be6d349d229480b")
                        taskId = captcha.createTask(browser.current_url, sitekey)
                        response = captcha.joinTaskResult(taskId)
                        # browser.execute_script(f"document.getElementById('g-recaptcha-response')[0].innerHTML = '{response}';")
                        browser.execute_script('''
                                document.getElementById("g-recaptcha-response").innerHTML=arguments[0];
                            ''', response)
                        print("captcha solve")
                        # time.sleep(11)
                        # while True:
                        #     try:
                        #         browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/button[@class='btn btn-lg btn-block tw-bg-yellow-600 tw-text-white hover:tw-text-white hover:tw-opacity-60 tw-transition']").click()
                        #     except Exception as ex:
                        #         print(ex)
                        #         time.sleep(0.1)
                        break
                    except Exception as ex:
                        time.sleep(0.1)    

                # input("Solve Captcha then Enter...")

                time.sleep(1)
                
                while True:
                    try:
                        browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/button[@type='submit']").click()
                        break
                    except Exception as ex:
                        time.sleep(0.1)
            fa = ""
            
            try:
                # Open a new window
                browser.execute_script("window.open('');")
                browser.switch_to.window(browser.window_handles[1])
                while True:
                    try:
                        browser.get("https://get2fa.dev/")
                        break
                    except:
                        time.sleep(0.1)
                # Switch to the new window
                while True:
                    try:
                        browser.find_element_by_xpath("//*[@class='container']/div/div/input[@placeholder='The secret key (in base-32 format)']").clear()
                        browser.find_element_by_xpath("//*[@class='container']/div/div/input[@placeholder='The secret key (in base-32 format)']").send_keys(code)
                        break
                    except Exception as ex:
                        time.sleep(0.1)

                time.sleep(5)
                while True:
                    try:
                        fa = browser.find_element_by_xpath("//*[@class='container']/div/p[@class='title is-size-1 has-text-centered']").text
                        break
                    except Exception as ex:
                        time.sleep(0.1)

                if not fa:
                    time.sleep(0.5)
                    while True:
                        try:
                            fa = browser.find_element_by_xpath("//*[@class='container']/div/p[@class='title is-size-1 has-text-centered']").text
                            break
                        except Exception as ex:
                            time.sleep(0.1)

                browser.switch_to.window(browser.window_handles[0])
            except Exception as ex:
                time.sleep(0.1)

            
            while True:
                try:
                    browser.find_element_by_xpath("//input[@type='number']").send_keys(fa)
                    break
                except Exception as ex:
                    time.sleep(0.1)

            time.sleep(0.5)
            while True:
                try:
                    browser.find_element_by_xpath("//button[@class='btn btn-block btn-primary']").click()
                    break
                except Exception as ex:
                    time.sleep(0.1)

            time.sleep(1)

            check_invalid_2fa = 0

            try:
                browser.find_element_by_xpath("//div[@class='ajax-error form-group text-danger text-center']")
                check_invalid_2fa = 1
            except Exception as ex:
                time.sleep(0.1)

            if check_invalid_2fa:
                # check Too many attempts.
                check_too_many_attempts = 0
                time.sleep(0.5)

                while True:
                    try:
                        strong = browser.find_element_by_xpath("//div[@class='ajax-error form-group text-danger text-center']/strong")
                        if "Too many attempts." in strong.get_attribute('innerHTML'):
                            check_too_many_attempts = 1
                        break
                    except Exception as ex:
                        time.sleep(0.1)
                if not check_too_many_attempts:
                    browser.switch_to.window(browser.window_handles[1])
                    time.sleep(1)
                    while True:
                        try:
                            fa = browser.find_element_by_xpath("//*[@class='container']/div/p[@class='title is-size-1 has-text-centered']").text
                            break
                        except Exception as ex:
                            time.sleep(0.1)

                    time.sleep(0.5)
                    browser.switch_to.window(browser.window_handles[0])

                    while True:
                        try:
                            browser.find_element_by_xpath("//input[@type='number']").clear()
                            browser.find_element_by_xpath("//input[@type='number']").send_keys(fa)
                            break
                        except Exception as ex:
                            time.sleep(0.1)

                    time.sleep(0.5)
                    while True:
                        try:
                            browser.find_element_by_xpath("//button[@class='btn btn-block btn-primary']").click()
                            break
                        except Exception as ex:
                            time.sleep(0.1)
                else:
                    time.sleep(180)

                    browser.get(register)
                    time.sleep(0.3)
                    while True:
                        try:
                            browser.find_element_by_xpath("//a[@href='https://presearch.org/login']").click()
                            break
                        except:
                            time.sleep(0.1)
                    
                    time.sleep(1)

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
                            time.sleep(0.1)

                    time.sleep(0.1)
                    
                    while True:
                        try:
                            browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/div/div[@class='checkbox blue text-left']").click()
                            break
                        except Exception as ex:
                            time.sleep(0.1)

                    while True:
                        try:
                            # recaptcha = browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/div/div/iframe[@title='reCAPTCHA']")
                            recaptcha = browser.find_element_by_xpath("//iframe[contains(@title, 'reCAPTCHA')]")
                            print("recaptcha")
                            sitekey = ''
                            for query in urlparse.urlparse(
                                    recaptcha.get_attribute('src')).query.split(
                                '&'):
                                if 'k=' in query:
                                    sitekey = query.split('=')[1]

                            captcha = NoCaptchaTaskProxyless(client_key="da52ffbb815fb08c8be6d349d229480b")
                            taskId = captcha.createTask(browser.current_url, sitekey)
                            response = captcha.joinTaskResult(taskId)
                            # browser.execute_script(f"document.getElementById('g-recaptcha-response')[0].innerHTML = '{response}';")
                            browser.execute_script('''
                                    document.getElementById("g-recaptcha-response").innerHTML=arguments[0];
                                ''', response)
                            print("captcha solve")
                            # time.sleep(11)
                            # while True:
                            #     try:
                            #         browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/button[@class='btn btn-lg btn-block tw-bg-yellow-600 tw-text-white hover:tw-text-white hover:tw-opacity-60 tw-transition']").click()
                            #     except Exception as ex:
                            #         print(ex)
                            #         time.sleep(0.1)
                            break
                        except Exception as ex:
                            time.sleep(0.1)    

                    # input("Solve Captcha then Enter...")

                    time.sleep(1)
                    
                    while True:
                        try:
                            browser.find_element_by_xpath("//*[@class='login-box']/div/div/form/div/div/button[@type='submit']").click()
                            break
                        except Exception as ex:
                            time.sleep(0.1)
                fa = ""
                
                try:
                    # Open a new window
                    browser.execute_script("window.open('');")
                    browser.switch_to.window(browser.window_handles[1])
                    while True:
                        try:
                            browser.get("https://get2fa.dev/")
                            break
                        except:
                            time.sleep(0.1)
                    # Switch to the new window
                    while True:
                        try:
                            browser.find_element_by_xpath("//*[@class='container']/div/div/input[@placeholder='The secret key (in base-32 format)']").clear()
                            browser.find_element_by_xpath("//*[@class='container']/div/div/input[@placeholder='The secret key (in base-32 format)']").send_keys(code)
                            break
                        except Exception as ex:
                            time.sleep(0.1)

                    time.sleep(5)
                    while True:
                        try:
                            fa = browser.find_element_by_xpath("//*[@class='container']/div/p[@class='title is-size-1 has-text-centered']").text
                            break
                        except Exception as ex:
                            time.sleep(0.1)

                    if not fa:
                        time.sleep(0.5)
                        while True:
                            try:
                                fa = browser.find_element_by_xpath("//*[@class='container']/div/p[@class='title is-size-1 has-text-centered']").text
                                break
                            except Exception as ex:
                                time.sleep(0.1)

                    browser.switch_to.window(browser.window_handles[0])
                except Exception as ex:
                    time.sleep(0.1)

                
                while True:
                    try:
                        browser.find_element_by_xpath("//input[@type='number']").send_keys(fa)
                        break
                    except Exception as ex:
                        time.sleep(0.1)

                time.sleep(0.5)
                while True:
                    try:
                        browser.find_element_by_xpath("//button[@class='btn btn-block btn-primary']").click()
                        break
                    except Exception as ex:
                        time.sleep(0.1)

                time.sleep(1)

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
            
            try:
                engine = None
                for handle in browser.window_handles:
                    browser.switch_to.window(handle)
                    if "https://engine.presearch.org/" in browser.current_url:
                        engine = handle
                        break

                browser.switch_to.window(engine)
            except Exception as ex:
                time.sleep(0.1)
                

            while True:
                try:
                    browser.find_element_by_xpath("//div[@class='absolute top-0 right-0 hidden mt-8 mr-8 2lg:block']/div/div/div[@class='cursor-pointer hover:opacity-60 dark:text-white transtion min-w-max']").click()
                    break
                except Exception as ex:
                    time.sleep(0.1)

            time.sleep(2)
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

            try:
                data = {"email":username, "token":token, "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d":remember, "code":code}

                fname = "presearchNewData.json"
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

            print("Finish refile :" + username)
            browser.quit()
            # print("Wait 60s to continue...")
            # time.sleep(60)
        except Exception as ex:
            log.screen_n_file('[!] %s has exception: %s!' % (app, ex))
        finally:
            browser.quit()



ResetToken()