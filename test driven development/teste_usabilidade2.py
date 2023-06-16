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

sleep(3.5)

entrar_btn = driver.find_element(By.XPATH, '//*[@id="navbarResponsive"]/ul/li[2]/a')
entrar_btn.click()

sleep(1.75)

email_entrada = driver.find_element(By.XPATH, '//*[@id="email"]')
senha_entrada = driver.find_element(By.XPATH, '//*[@id="password"]')
submit_btn = driver.find_element(By.XPATH, '//*[@id="submit"]')
driver.execute_script("arguments[0].scrollIntoView();", submit_btn)

sleep(1.75)

palavras_de_teste = ["teste@teste.com", "123"]
entradas = [email_entrada, senha_entrada]

for index, teste in enumerate(palavras_de_teste):
    for letra in teste:
        entradas[index].send_keys(letra)
        sleep(0.25)

sleep(1.25)
submit_btn.click()

sleep(1.25)

submit_btn = driver.find_element(By.XPATH, '//*[@id="submit"]')
driver.execute_script("arguments[0].scrollIntoView();", submit_btn)

sleep(3)

registrar_link = driver.find_element(By.XPATH, '//*[@id="navbarResponsive"]/ul/li[3]/a')
driver.execute_script("arguments[0].scrollIntoView();", registrar_link)

sleep(1.75)

registrar_link.click()

email_entrada = driver.find_element(By.ID, 'email')
senha_entrada = driver.find_element(By.ID, 'password')
nome_entrada = driver.find_element(By.ID, 'name')
submit_btn = driver.find_element(By.ID, 'submit')

driver.execute_script("arguments[0].scrollIntoView();", nome_entrada)

palavras_de_teste = ["teste@teste.com", "123", "Tester"]
entradas = [email_entrada, senha_entrada, nome_entrada]

for index, teste in enumerate(palavras_de_teste):
    for letra in teste:
        entradas[index].send_keys(letra)
        sleep(0.25)

submit_btn.click()

create_post_btn = driver.find_element(By.XPATH, '/html/body/div/div/div/div/a')
driver.execute_script("arguments[0].scrollIntoView();", create_post_btn)

sleep(3.5)

create_post_btn.click()

sleep(3.5)

titulo_entrada = driver.find_element(By.XPATH, '//*[@id="title"]')
subtitulo_entrada = driver.find_element(By.XPATH, '//*[@id="subtitle"]')
url_entrada = driver.find_element(By.XPATH, '//*[@id="img_url"]')

sleep(3.5)

driver.execute_script("arguments[0].scrollIntoView();", titulo_entrada)

palavras_de_teste = ["Teste de titulo", "Teste de subtitulo",
                     "https://www.google.com/url?sa=i&url=https%3A%2F%2Frevistagalileu.globo.com%2FCiencia%2FBiologia%2Fnoticia%2F2018%2F02%2Fespecie-de-macaco-tem-vida-sexual-influenciada-pelo-tamanho-de-nariz.html&psig=AOvVaw3Nal3eoxYDUMldCn94A8IY&ust=1686930018215000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCLiqsJbOxf8CFQAAAAAdAAAAABAE"]
entradas = [titulo_entrada, subtitulo_entrada, url_entrada]

for index, teste in enumerate(entradas):
    if index != 2:
        for letra in palavras_de_teste[index]:
            teste.send_keys(letra)
            sleep(0.25)
    else:
        teste.send_keys(palavras_de_teste[index])

sleep(1.25)

ckeditor_frame = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(ckeditor_frame)

body = driver.find_element(By.TAG_NAME, "body")

body.send_keys("Olá, CKEditor!")

driver.switch_to.default_content()

submit_btn = driver.find_element(By.ID, 'submit')

sleep(1.25)

submit_btn.click()

sleep(3)

submit_btn = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/a')

driver.execute_script("arguments[0].scrollIntoView();", submit_btn)

submit_btn.click()

sleep(3.5)

titulo_entrada = driver.find_element(By.XPATH, '//*[@id="title"]')
subtitulo_entrada = driver.find_element(By.XPATH, '//*[@id="subtitle"]')
url_entrada = driver.find_element(By.XPATH, '//*[@id="img_url"]')

sleep(3.5)

driver.execute_script("arguments[0].scrollIntoView();", titulo_entrada)

palavras_de_teste = ["Teste de titulo2", "Teste de subtitulo2",
                     "https://www.google.com/imgres?imgurl=https%3A%2F%2Flookaside.fbsbx.com%2Flookaside%2Fcrawler%2Fmedia%2F%3Fmedia_id%3D2089183424458895&tbnid=1D6nuhL3H-t_mM&vet=12ahUKEwiTz4f51sX_AhXlB9QKHZSoBnAQMygAegUIARDTAQ..i&imgrefurl=https%3A%2F%2Fwww.facebook.com%2Fpescarepreservar%2Fposts%2Frecebi-essa-imagem-peixe-gota-psychrolutes-marcidus-uma-esp%25C3%25A9cie-do-pac%25C3%25ADfico-que-%2F2089183441125560%2F&docid=nwgoxITbTzF9JM&w=480&h=480&q=Peixe-gota&ved=2ahUKEwiTz4f51sX_AhXlB9QKHZSoBnAQMygAegUIARDTAQ"]
entradas = [titulo_entrada, subtitulo_entrada, url_entrada]

for index, teste in enumerate(entradas):
    if index != 2:
        for letra in palavras_de_teste[index]:
            teste.send_keys(letra)
    else:
        teste.send_keys(palavras_de_teste[index])

sleep(1.25)

ckeditor_frame = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(ckeditor_frame)

body = driver.find_element(By.TAG_NAME, "body")

body.send_keys("Olá, CKEditor!")

driver.switch_to.default_content()

submit_btn = driver.find_element(By.ID, 'submit')

sleep(1.25)

submit_btn.click()

sleep(1.25)

submit_btn = driver.find_element(By.XPATH, '/html/body/div/div/div/div[3]/a')

driver.execute_script("arguments[0].scrollIntoView();", submit_btn)

submit_btn.click()

sleep(3.5)

titulo_entrada = driver.find_element(By.XPATH, '//*[@id="title"]')
subtitulo_entrada = driver.find_element(By.XPATH, '//*[@id="subtitle"]')
url_entrada = driver.find_element(By.XPATH, '//*[@id="img_url"]')

sleep(3.5)

driver.execute_script("arguments[0].scrollIntoView();", titulo_entrada)

palavras_de_teste = ["Teste de titulo3", "Teste de subtitulo3",
                     "https://www.google.com/imgres?imgurl=https%3A%2F%2Fs2.glbimg.com%2FvFDzTNriZbsi3YmijfdwojQS62s%3D%2F0x0%3A992x552%2F924x0%2Fsmart%2Ffilters%3Astrip_icc()%2Fi.s3.glbimg.com%2Fv1%2FAUTH_7d5b9b5029304d27b7ef8a7f28b4d70f%2Finternal_photos%2Fbs%2F2022%2F0%2FG%2FSzRD4YR4S6xbDkBNPWtA%2Fqsq.jpg&tbnid=kp0vB0QM2AYgkM&vet=12ahUKEwi4r-2-18X_AhWxDNQKHY2ODm0QMygBegUIARDNAQ..i&imgrefurl=https%3A%2F%2Fumsoplaneta.globo.com%2Fbiodiversidade%2Fnoticia%2F2022%2F12%2F24%2Fcientistas-descobrem-como-sapos-de-vidro-ficam-transparentes.ghtml&docid=kxygCOWUzrgZOM&w=924&h=514&q=Sapo-de-vidro&ved=2ahUKEwi4r-2-18X_AhWxDNQKHY2ODm0QMygBegUIARDNAQ"]
entradas = [titulo_entrada, subtitulo_entrada, url_entrada]

for index, teste in enumerate(entradas):
    if index != 2:
        for letra in palavras_de_teste[index]:
            teste.send_keys(letra)
    else:
        teste.send_keys(palavras_de_teste[index])

sleep(1.25)

ckeditor_frame = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(ckeditor_frame)

body = driver.find_element(By.TAG_NAME, "body")

body.send_keys("Olá, CKEditor!")

driver.switch_to.default_content()

submit_btn = driver.find_element(By.ID, 'submit')

sleep(1.25)

submit_btn.click()

post_1 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/a/h2')
post_1.click()

editar_btn = driver.find_element(By.XPATH, '/html/body/article/div/div/div/div[1]/a')
driver.execute_script("arguments[0].scrollIntoView();", editar_btn)
sleep(1)
editar_btn.click()

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
