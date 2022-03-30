from selenium.webdriver.common.keys import Keys
import driver_config
import time

def login(driver, user, password):
    driver.get('https://app.rdstation.com.br/leads')
    driver_config.driver_delay(driver)
    driver.find_element_by_id("email").send_keys(user)
    time.sleep(0.5)
    driver.find_element_by_id("password").send_keys(password, Keys.ENTER)
    time.sleep(0.5)

    return driver
