from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from main import app
from model.db import db, User, BlogPost, Comment


class BlogTester:
    def __init__(self, base_url="http://localhost:5000/"):
        options = webdriver.EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('start-maximized')
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
        self.base_url = base_url
        self.driver.get(url=self.base_url)
        sleep(3.5)

    def fill_form(self, elements, values):
        for element, value in zip(elements, values):
            for letter in value:
                element.send_keys(letter)
                sleep(0.25)

    def navegation(self, xpath):
        nav = self.driver.find_element(By.XPATH, xpath)
        sleep(1.75)
        self.driver.execute_script("arguments[0].scrollIntoView();", nav)
        return nav

    def perform_login(self, email, password):
        email_field = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        submit_btn = self.driver.find_element(By.XPATH, '//*[@id="submit"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
        sleep(1.75)
        self.fill_form([email_field, password_field], [email, password])
        sleep(1.25)
        submit_btn.click()
        sleep(1.25)
        submit_btn = self.driver.find_element(By.XPATH, '//*[@id="submit"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_btn)

    def perform_registration_adm(self, email, password, name):
        email_entrada = self.driver.find_element(By.ID, 'email')
        senha_entrada = self.driver.find_element(By.ID, 'password')
        nome_entrada = self.driver.find_element(By.ID, 'name')
        submit_btn = self.driver.find_element(By.ID, 'submit')
        self.driver.execute_script("arguments[0].scrollIntoView();", nome_entrada)
        self.fill_form([email_entrada, senha_entrada, nome_entrada], [email, password, name])
        submit_btn.click()

    def create_post(self, title, subtitle, img_url, content):
        sleep(3.5)
        titulo_entrada = self.driver.find_element(By.XPATH, '//*[@id="title"]')
        subtitulo_entrada = self.driver.find_element(By.XPATH, '//*[@id="subtitle"]')
        url_entrada = self.driver.find_element(By.XPATH, '//*[@id="img_url"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", titulo_entrada)
        self.fill_form([titulo_entrada, subtitulo_entrada, url_entrada], [title, subtitle, img_url])
        sleep(1.25)
        ckeditor_frame = self.driver.find_element(By.TAG_NAME, "iframe")
        self.driver.switch_to.frame(ckeditor_frame)
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys(content)
        self.driver.switch_to.default_content()
        submit_btn = self.driver.find_element(By.ID, 'submit')
        sleep(1.25)
        submit_btn.click()


    def edit_post(self, new_img_url="https://www.example.com/new_image.png"):
        editar_btn = self.driver.find_element(By.XPATH, '/html/body/article/div/div/div/div[1]/a')
        self.driver.execute_script("arguments[0].scrollIntoView();", editar_btn)
        sleep(1)
        editar_btn.click()
        url_entrada = self.driver.find_element(By.XPATH, '//*[@id="img_url"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", url_entrada)
        sleep(1)
        url_entrada.clear()
        sleep(1)
        url_entrada.send_keys('https://cdn.pixabay.com/photo/2023/06/07/18/14/giraffes-8047856_1280.jpg')
        sleep(1)
        submit_btn = self.driver.find_element(By.ID, 'submit')
        submit_btn.click()

    def post_comment(self, comment):
        sleep(5)
        ckeditor_frame = self.driver.find_element(By.TAG_NAME, "iframe")
        self.driver.switch_to.frame(ckeditor_frame)
        body = self.driver.find_element(By.TAG_NAME, "body")
        self.driver.execute_script("arguments[0].scrollIntoView();", body)
        sleep(3)
        body.send_keys(comment)
        self.driver.switch_to.default_content()
        sleep(3)
        submit_btn = self.driver.find_element(By.ID, 'submit')
        submit_btn.click()

    def send_contact_form(self, name, email, phone, message):
        nome_entrada = self.driver.find_element(By.XPATH, '//*[@id="name"]')
        email_entrada = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        n_tel_entrada = self.driver.find_element(By.XPATH, '//*[@id="phone"]')
        mensagem_entrada = self.driver.find_element(By.XPATH, '//*[@id="message"]')
        contato_enviar_btn = self.driver.find_element(By.XPATH, '//*[@id="sendMessageButton"]')
        entradas = [nome_entrada, email_entrada, n_tel_entrada, mensagem_entrada]
        self.driver.execute_script("arguments[0].scrollIntoView();", nome_entrada)
        self.fill_form(entradas, [name, email, phone, message])
        sleep(3)
        contato_enviar_btn.click()

    def delete_post(self):
        sleep(2)
        delete_post = self.navegation('/html/body/div/div/div/div[3]/p/a')
        sleep(2)
        delete_post.click()
        sleep(2)
        nav = self.navegation('/html/body/div/div/div/div[2]/p/a')

    def logout(self):
        nav = self.navegation('//*[@id="navbarResponsive"]/ul/li[2]/a')
        sleep(2)
        nav.click()

    def resposividade(self):
        self.driver.set_window_size(766, 652)
        nav = self.navegation('//*[@id="mainNav"]/div/button')
        nav.click()

    def perform_registration_default(self, email, password, name):
        email_entrada = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        senha_entrada = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        nome_entrada = self.driver.find_element(By.XPATH, '//*[@id="name"]')
        submit_btn = self.driver.find_element(By.XPATH, '//*[@id="submit"]')
        teste = [email, password, name]
        entradas = [email_entrada, senha_entrada, nome_entrada]
        self.fill_form(entradas, teste)
        submit_btn.click()
        sleep(3)

    def post_default(self):
        ckeditor_frame = self.driver.find_element(By.TAG_NAME, "iframe")
        self.driver.switch_to.frame(ckeditor_frame)
        body = self.driver.find_element(By.TAG_NAME, "body")
        self.driver.execute_script("arguments[0].scrollIntoView();", body)
        body.send_keys("Teste de comentario nao adminstrador.")
        self.driver.switch_to.default_content()
        enviar_comentario_btn = self.driver.find_element(By.XPATH, '//*[@id="submit"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", enviar_comentario_btn)
        sleep(2)
        enviar_comentario_btn.click()
        enviar_comentario_btn = self.driver.find_element(By.XPATH, '//*[@id="submit"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", enviar_comentario_btn)

    def default_window_size(self):
        self.driver.maximize_window()

    def clear_data(self):
        with app.app_context():
            meta = db.metadata
            for table in reversed(meta.sorted_tables):
                db.session.execute(table.delete())
            db.session.commit()
        self.driver.refresh()

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    tester = BlogTester()

    while True:
        "Tentativa de login de conta que não existe, para mostrar a prevenção de erros."
        sleep(3)
        nav = tester.navegation('//*[@id="navbarResponsive"]/ul/li[2]/a')
        nav.click()
        tester.perform_login("usuario_adm@teste.com", "123456abc")
        sleep(4)
        nav = tester.navegation('//*[@id="navbarResponsive"]/ul/li[3]/a')
        nav.click()

        "Registrar conta administrador."
        tester.perform_registration_adm("usuario_adm@teste.com", "123456abc", "Administrador")

        "Criar nova postagem"
        routes = ['/html/body/div/div/div/div/a', '/html/body/div/div/div/div[2]/a', '/html/body/div/div/div/div[3]/a']
        for i in range(0, 3):
            nav = tester.navegation(routes[i])
            sleep(1.75)
            nav.click()
            sleep(2)
            tester.create_post(f"Teste de titulo {i+1}", f"Teste de subtitulo {i+1}", "https://www.example.com/image.png", f"Teste conteudo {i+1}")

        "Editar postagem"
        nav = tester.navegation('/html/body/div/div/div/div[1]/a/h2')
        sleep(3)
        nav.click()
        tester.edit_post()

        "Comentar uma postagem"
        tester.post_comment("Teste de comentario")

        "Teste sobre rota"
        nav = tester.driver.find_element(By.XPATH, '//*[@id="navbarResponsive"]/ul/li[3]/a')
        sleep(1)
        nav.click()
        tester.navegation('/html/body/div/div/div/p[2]')

        "Teste contato"
        nav = tester.navegation('//*[@id="navbarResponsive"]/ul/li[4]/a')
        sleep(2)
        nav.click()
        tester.send_contact_form("Teste contato nome", "Teste contato email", "Teste contato telefone", "Teste contato mensagem")

        nav = tester.navegation('//*[@id="navbarResponsive"]/ul/li[1]/a')
        nav.click()

        "Teste delete"
        tester.delete_post()

        "Sair da conta"
        tester.logout()

        "Teste responsividade e conta comum"
        tester.resposividade()

        "Novo Usuario(Comum)"
        nav = tester.navegation('//*[@id="navbarResponsive"]/ul/li[3]/a')
        sleep(2)
        nav.click()
        tester.perform_registration_default("deafautl_user@teste.com", "321cba456", "Usuario Comum")

        "Teste de visualização de postagem"
        nav = tester.navegation('/html/body/div/div/div/div[1]/a/h2')
        sleep(2)
        nav.click()
        tester.navegation('/html/body/article/div/div/div/p')
        sleep(2)

        "Teste de postagem nao adm"
        tester.post_default()

        sleep(2)
        nav = tester.navegation('//*[@id="mainNav"]/div/button')
        nav.click()
        sleep(2)
        nav = tester.navegation('//*[@id="navbarResponsive"]/ul/li[1]/a')
        nav.click()

        sleep(2)
        tester.navegation('/html/body/div/div/div/div[2]/a/h3')
        sleep(3)
        tester.navegation('/html/body/header/div[2]/div/div/div/h1')
        sleep(3)

        "Retornar ao tamanho total de janela"
        tester.default_window_size()

        tester.clear_data()
        sleep(3)

