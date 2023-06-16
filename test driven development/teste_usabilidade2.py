from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from main import app
from model.db import db, User, BlogPost, Comment

options = webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('start-maximized')

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
driver.get(url="http://localhost:5000/")

url_entrada = driver.find_element(By.XPATH, '//*[@id="img_url"]')
driver.execute_script("arguments[0].scrollIntoView();", url_entrada)
sleep(1)
url_entrada.clear()
sleep(1)
url_entrada.send_keys('https://cdn.pixabay.com/photo/2023/06/07/18/14/giraffes-8047856_1280.jpg')
sleep(1)
submit_btn = driver.find_element(By.ID, 'submit')
submit_btn.click()

sleep(1)

ckeditor_frame = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(ckeditor_frame)
body = driver.find_element(By.TAG_NAME, "body")
driver.execute_script("arguments[0].scrollIntoView();", body)
body.send_keys("Teste de comentario")
driver.switch_to.default_content()
sleep(1)
submit_btn = driver.find_element(By.ID, 'submit')
submit_btn.click()

submit_btn = driver.find_element(By.ID, 'submit')
driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
sleep(1)

sobre_link = driver.find_element(By.XPATH, '//*[@id="navbarResponsive"]/ul/li[3]/a')
sleep(1)
sobre_link.click()

sobre = driver.find_element(By.XPATH, '/html/body/div/div/div/p[2]')
sleep(2)
driver.execute_script("arguments[0].scrollIntoView();", sobre)
sleep(2)

contato = driver.find_element(By.XPATH, '//*[@id="navbarResponsive"]/ul/li[4]/a')
sleep(2)
driver.execute_script("arguments[0].scrollIntoView();", contato)
sleep(2)
contato.click()

sleep(2)
nome_entrada = driver.find_element(By.XPATH, '//*[@id="name"]')
email_entrada = driver.find_element(By.XPATH, '//*[@id="email"]')
n_tel_entrada = driver.find_element(By.XPATH, '//*[@id="phone"]')
mensagem_entrada = driver.find_element(By.XPATH, '//*[@id="message"]')
contato_enviar_btn = driver.find_element(By.XPATH, '//*[@id="sendMessageButton"]')
entradas = [nome_entrada, email_entrada, n_tel_entrada, mensagem_entrada]
testes = ['Teste contato nome', 'Teste contato email', 'Teste contato telefone', 'Teste contato mensagem']
driver.execute_script("arguments[0].scrollIntoView();", nome_entrada)
sleep(2)
for index, entrada in enumerate(entradas):
    for letra in testes[index]:
        entrada.send_keys(letra)
sleep(2)
contato_enviar_btn.click()
sleep(3)
home_link = driver.find_element(By.XPATH, '//*[@id="navbarResponsive"]/ul/li[1]/a')
home_link.click()

sleep(2)
delete_post = driver.find_element(By.XPATH, '/html/body/div/div/div/div[3]/p/a')
driver.execute_script("arguments[0].scrollIntoView();", delete_post)
sleep(2)
delete_post.click()
sleep(2)
delete_post = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/p/a')
driver.execute_script("arguments[0].scrollIntoView();", delete_post)

sleep(2)
sair_conta_adm = driver.find_element(By.XPATH, '//*[@id="navbarResponsive"]/ul/li[2]/a')
driver.execute_script("arguments[0].scrollIntoView();", sair_conta_adm)
sleep(2)
sair_conta_adm.click()
sleep(2)

driver.set_window_size(766, 652)

sleep(2)
menu_btn = driver.find_element(By.XPATH, '//*[@id="mainNav"]/div/button')
menu_btn.click()

sleep(3)
registrar_link = driver.find_element(By.XPATH, '//*[@id="navbarResponsive"]/ul/li[3]/a')
registrar_link.click()

email_entrada = driver.find_element(By.XPATH, '//*[@id="email"]')
senha_entrada = driver.find_element(By.XPATH, '//*[@id="password"]')
nome_entrada = driver.find_element(By.XPATH, '//*[@id="name"]')
submit_btn = driver.find_element(By.XPATH, '//*[@id="submit"]')
palavras_de_teste = ["nao_adm@teste.com", "321", "Nao Adminstrador"]
entradas = [email_entrada, senha_entrada, nome_entrada]
for index, teste in enumerate(palavras_de_teste):
    for letra in teste:
        entradas[index].send_keys(letra)
        sleep(0.25)
submit_btn.click()
sleep(2)

post_1 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/a/h2')
driver.execute_script("arguments[0].scrollIntoView();", post_1)
sleep(2)
post_1.click()
conteudo = driver.find_element(By.XPATH, '/html/body/article/div/div/div/p')
driver.execute_script("arguments[0].scrollIntoView();", conteudo)
sleep(2)
ckeditor_frame = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(ckeditor_frame)
body = driver.find_element(By.TAG_NAME, "body")
driver.execute_script("arguments[0].scrollIntoView();", body)
body.send_keys("Teste de comentario nao adminstrador.")
driver.switch_to.default_content()
enviar_comentario_btn = driver.find_element(By.XPATH, '//*[@id="submit"]')
driver.execute_script("arguments[0].scrollIntoView();", enviar_comentario_btn)
sleep(2)
enviar_comentario_btn.click()
enviar_comentario_btn = driver.find_element(By.XPATH, '//*[@id="submit"]')
driver.execute_script("arguments[0].scrollIntoView();", enviar_comentario_btn)

sleep(2)
menu_btn = driver.find_element(By.XPATH, '//*[@id="mainNav"]/div/button')
menu_btn.click()
sleep(2)
menu_btn = driver.find_element(By.XPATH, '//*[@id="navbarResponsive"]/ul/li[1]/a')
menu_btn.click()

sleep(2)
post_2 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/a/h3')
driver.execute_script("arguments[0].scrollIntoView();", post_2)
sleep(3)
titulo = driver.find_element(By.XPATH, '/html/body/header/div[2]/div/div/div/h1')
driver.execute_script("arguments[0].scrollIntoView();", titulo)
sleep(3)

driver.maximize_window()


def clear_data():
    with app.app_context():
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            print('Clear table %s' % table)
            db.session.execute(table.delete())
        db.session.commit()


clear_data()

sleep(600)
