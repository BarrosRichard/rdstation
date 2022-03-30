from selenium.webdriver.chrome.options import Options
import os

def driver_delay(driver, delay=30):
    driver.implicitly_wait(delay)

def driver_options(empresa):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--log-level=3")
    prefs = {'download.default_directory' : os.getcwd()+rf'.\leads\{empresa.name_project}'}
    options.add_experimental_option('prefs', prefs)

    return options
