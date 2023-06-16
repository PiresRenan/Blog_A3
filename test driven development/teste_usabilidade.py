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

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def fill_form(self, elements, values):
        for element, value in zip(elements, values):
            for letter in value:
                element.send_keys(letter)
                sleep(0.25)

    def navegation(self, xpath):
        nav = self.find_element(By.XPATH, xpath)
        sleep(1.75)
        self.driver.execute_script("arguments[0].scrollIntoView();", nav)
        return nav

    def perform_login(self, email, password):
        email_field = self.find_element(By.XPATH, '//*[@id="email"]')
        password_field = self.find_element(By.XPATH, '//*[@id="password"]')
        submit_btn = self.find_element(By.XPATH, '//*[@id="submit"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
        sleep(1.75)
        self.fill_form([email_field, password_field], [email, password])
        sleep(1.25)
        submit_btn.click()
        sleep(1.25)
        submit_btn = self.find_element(By.XPATH, '//*[@id="submit"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_btn)

    def perform_registration_adm(self, email, password, name):
        email_entrada = self.driver.find_element(By.ID, 'email')
        senha_entrada = self.driver.find_element(By.ID, 'password')
        nome_entrada = self.driver.find_element(By.ID, 'name')
        submit_btn = self.driver.find_element(By.ID, 'submit')
        self.driver.execute_script("arguments[0].scrollIntoView();", nome_entrada)
        self.fill_form([email_entrada, senha_entrada, nome_entrada], [email, password, name])
        submit_btn.click()

    def create_post(self, title, subtitle="Teste de subtitulo",
                    img_url="https://www.example.com/image.png", content="Olá, CKEditor!"):
        create_post_btn = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/a')
        self.driver.execute_script("arguments[0].scrollIntoView();", create_post_btn)
        sleep(3.5)
        create_post_btn.click()
        sleep(3.5)

    def edit_post(self, new_img_url="https://www.example.com/new_image.png"):
        # Restante do código omitido por motivos de espaço
        pass

    def post_comment(self, comment="Teste de comentario"):
        # Restante do código omitido por motivos de espaço
        pass

    def visit_about(self):
        # Restante do código omitido por motivos de espaço
        pass

    def send_contact_form(self, name="Teste contato nome", email="Teste contato email", phone="Teste contato telefone",
                          message="Teste contato mensagem"):
        # Restante do código omitido por motivos de espaço
        pass

    def clear_data(self):
        with app.app_context():
            meta = db.metadata
            for table in reversed(meta.sorted_tables):
                print('Clear table %s' % table)
                db.session.execute(table.delete())
            db.session.commit()

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    tester = BlogTester()
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
    nav = tester.navegation('/html/body/div/div/div/div/a')
    sleep(1.75)
    nav.click()
    for i in range(0,3)
    tester.create_post("Teste de titulo")

    # tester.edit_post()
    # tester.post_comment()
    # tester.visit_about()
    # tester.send_contact_form()
    tester.clear_data()
    sleep(600)
    tester.quit()
