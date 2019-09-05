from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import traceback
from datetime import datetime
import time

msg = 'Happy Teachers\' Day '
sal = ''

try:

    ## Use according to the browser installed.
    # driver = webdriver.Chrome(executable_path='geckodriver.exe')
    driver = webdriver.Firefox(executable_path='geckodriver.exe')

    driver.get('https://web.whatsapp.com')
    wait = WebDriverWait(driver, 600)

    print('Press Enter after scanning QR code from phone.')
    wait_input = input()

    with open('recipient_list.txt') as fp:
        contacts = list(fp)

    for name in contacts:
        if name.startswith('#'):
            continue
        elif name.startswith('$'):
            sal = name[2:-1]
        else:
            with open('error.txt', 'a') as err:
                try:
                    title = name[:-1]
                    driver.find_element_by_xpath('//*[@title="New chat"]').click()
                    time.sleep(5)
                    ele = driver.find_element_by_xpath('//*[@title="Search contacts"]')
                    time.sleep(5)
                    ele.click()
                    time.sleep(5)
                    ele.send_keys(title)
                    time.sleep(5)
                    ele.send_keys(Keys.ENTER)
                    # driver.find_element_by_xpath('//*[@title="'+title+'"]').click()
                    time.sleep(5)
                    inp_xpath = '//div[@dir="ltr"][@data-tab="1"][@spellcheck="true"]'
                    time.sleep(5)
                    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
                    time.sleep(5)
                    input_box.send_keys(msg + sal + Keys.ENTER)
                    print(str(datetime.now()), '\t', sal, title)
                except:
                    err.write('\n'+str(datetime.now())+'\t'+sal+' '+name)
                    err.write(traceback.format_exc())
                # time.sleep(300)
except:
    with open('error.txt', 'a') as err:
        err.write('\n'+str(datetime.now())+'\n')
        err.write(traceback.format_exc())
    traceback.print_exc()
finally:
    input('Please wait for all messages to be delivered and press Enter to quit.')
    driver.quit()
