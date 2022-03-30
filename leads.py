from infra.config import Database
from infra.Models import Empresas
from selenium import webdriver
import auth
import login
import driver_config
import time
import unzip
import populate
import os

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def leads(empresa):
    infra = Database().infra
    empresa = infra.query(Empresas).filter_by(name_project=empresa).first()

    user, password = auth.auth(empresa)

    options = driver_config.driver_options(empresa)
    driver = webdriver.Chrome("./drivers/chromedriver.exe", chrome_options=options)
    os.system("cls")
    print(f"Logando com {empresa.name}...")

    login.login(driver, user, password)
    driver_config.driver_delay(driver)
    time.sleep(3)
    print("Logou!!!")

    print("Baixando leads...")
    driver.find_element_by_xpath('//*[@id="leads_crm"]/div[1]/div/div[2]/div/button').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="leads_crm"]/div[1]/div/div[2]/div/ul/li[4]/a').click()
    time.sleep(3)

    driver.find_element_by_id("select-all").click()
    time.sleep(0.5)
    driver.find_element_by_id("go-forward-button").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("/html/body/section/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/label/input").click()
    time.sleep(3)
    driver.find_element_by_id("export-finish-button").click()

    driver.get("https://app.rdstation.com.br/leads/exportacoes")
    driver_config.driver_delay(driver)


    success = False
    while success == False:
        try:
            success = True
            driver.find_element_by_xpath("/html/body/section/div[1]/div[2]/div[1]/header/div/div[2]/a").click()
        except:
            success = False
            time.sleep(5)

    time.sleep(10)

    print("Donwload concluído!")
    print("Descompactando arquivos...")
    unzip.unzip(empresa)
    print("Arquivos descompactados!")
    print("Populando banco de dados...")
    populate.populate(empresa)
    print("Banco populado!")

leads("bild")
leads("vitta")
