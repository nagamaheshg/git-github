from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class GmailLogin:

    def loginpage(self):
        base_url = 'https:\\www.gmail.com'
        gecko_driver = 'E:\\Python\\workspace\\geckodriver.exe'
        driver = webdriver.Firefox(executable_path = gecko_driver)
        driver.get(base_url)

        try:
            # Login
            login_id = driver.find_element_by_id('identifierId')
            if login_id is not None:
                login_id.send_keys('mahesh.gatta@northalley.com')
                login_id.send_keys(Keys.ENTER)
                time.sleep(3)

            # password
            password = driver.find_element_by_name('password')
            if password is not None:
                password.send_keys('*******')
                password.send_keys(Keys.ENTER)
                time.sleep(8)

            # Mail Compose
            path = '/html/body/div[7]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[1]/div/div'
            compose_btn = driver.find_element_by_xpath(path)
            if compose_btn is not None:
                compose_btn.click()
                time.sleep(5)

            # To Party mail Address
            to_party = driver.find_element_by_name('to')
            if to_party is not None:
                to_party.send_keys('apar')
                time.sleep(2)
                to_party.send_keys(Keys.TAB, Keys.TAB)
                time.sleep(3)

            # Subject Content
            subject = driver.find_element_by_name('subjectbox')
            if subject is not None:
                subject.send_keys('My First Automation script in Python')
                time.sleep(2)

            else:
                print('I Skip this part')

            # content Area
            content_area = driver.find_element_by_class_name('Am')
            if content_area is not None:
                content_area.send_keys('Hi.....Anna') # Keys.TAB, Keys.ENTER
                time.sleep(3)

            else:
                print('No Element found')

            # send
            send = driver.find_element_by_css_selector('.aoO')
            if send is not None:
                send.click()
                time.sleep(2)

            else:
                print('No Element found')

        except:
            print('Element Not found!!!. Execution Stopped')
            raise Exception

        finally:
            driver.close()


obj = GmailLogin()
obj.loginpage()
