from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import NoSuchElementException

options = webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('start-maximized')

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
driver.get(url="http://localhost:5000/")

sleep(1.75)

entrar_btn = driver.find_element(By.XPATH, '//*[@id="navbarResponsive"]/ul/li[2]/a')
entrar_btn.click()

sleep(1.75)

email_entrada = driver.find_element(By.XPATH, '//*[@id="email"]')
senha_entrada = driver.find_element(By.XPATH, '//*[@id="password"]')
submit_btn = driver.find_element(By.XPATH, '//*[@id="submit"]')
driver.execute_script("arguments[0].scrollIntoView();", submit_btn)

sleep(1.75)

palavras = ["teste@teste.com", "123"]
entradas = [email_entrada, senha_entrada]

for index, palavra in enumerate(palavras):
    for letra in palavra:
        entradas[index].send_keys(letra)
        sleep(0.25)

sleep(1.25)
submit_btn.click()

sleep(60)
