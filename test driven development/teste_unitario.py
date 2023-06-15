import sys
import unittest
from datetime import datetime
from werkzeug.security import generate_password_hash

sys.path.insert(0, '..')

from main import app
from model.db import User, db, BlogPost, Comment


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        with self.app.app_context():
            db.create_all()

        self.test_user = User(email='test@test.com', name='test',
                              password=generate_password_hash('test123', method='pbkdf2:sha256', salt_length=8))
        with self.app.app_context():
            db.session.add(self.test_user)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def teste_registro(self):
        response = self.client.post('/register', data=dict(email='test2@test.com', name='test2', password='test1234',
                                                           submit='Sign Up'), follow_redirects=True)
        with self.app.app_context():
            user = User.query.filter_by(email='test2@test.com').first()
            self.assertIsNotNone(user)
        self.assertEqual(response.status_code, 200)

    def teste_registro_email_ja_utilizado(self):
        response = self.client.post('/register', data=dict(email='test@test.com', name='test2', password='test1234',
                                                           submit='Sign Up'), follow_redirects=True)
        self.assertIn("Este email já foi cadastrado anteriormente, entre ao inves de cadastrar!",
                      response.data.decode())
        self.assertEqual(response.status_code, 200)

    def teste_registro_senha_incorreta(self):
        self.client.post('/register',
                         data=dict(email='test2@test.com', name='test2', password='123', submit='Sign Up'),
                         follow_redirects=True)
        response = self.client.post('/login',
                                    data=dict(email='test2@test.com', password='senha_errada', submit='Log In'),
                                    follow_redirects=True)
        self.assertIn('Senha incorreta! Por favor, tente novamente.', response.data.decode())
        self.assertEqual(response.status_code, 200)

    def teste_rota_de_login(self):
        response = self.client.post('/login', data=dict(email='test@test.com', password='test123', submit='Log In'),
                                    follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_post(self):
        date_now = datetime.now()
        post = BlogPost(id=1, title="Titulo teste", subtitle="Subtitulo teste", img_url="https://teste.com",
                        body="Corpo teste", date=date_now)
        with self.app.app_context():
            db.session.add(post)
            db.session.commit()

        response = self.client.get('/post/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_add_new_post(self):
        self.client.post('/login', data=dict(email='test@test.com', password='test123', submit='Log In'),
                         follow_redirects=True)

        response = self.client.post('/new-post',
                                    data=dict(title='Titulo teste', subtitle='Subtitulo teste', body='Corpo teste',
                                              img_url="https://test.com", submit='Submit Post'),
                                    follow_redirects=True)

        with self.app.app_context():
            post = BlogPost.query.filter_by(title='Titulo teste').first()
        self.assertIsNotNone(post)

        self.assertEqual(response.status_code, 200)

    def test_edit_post(self):
        self.client.post('/login', data=dict(email='test@test.com', password='test123', submit='Log In'),
                         follow_redirects=True)

        date_now = datetime.now()
        post = BlogPost(id=1, title="Titulo original", subtitle="Subtitulo original", img_url="https://teste.com",
                        body="Corpo original", date=date_now)
        with self.app.app_context():
            db.session.add(post)
            db.session.commit()

        response = self.client.post('/edit-post/1',
                                    data=dict(title='Titulo editado', subtitle='Subtitulo editado',
                                              body='Corpo editado',
                                              img_url="https://teste.com", submit='Submit Post'),
                                    follow_redirects=True)

        with self.app.app_context():
            post = BlogPost.query.get(1)
            self.assertEqual(post.title, 'Titulo editado')
            self.assertEqual(post.subtitle, 'Subtitulo editado')
            self.assertEqual(post.body, 'Corpo editado')

        self.assertEqual(response.status_code, 200)

    def test_delete_post(self):
        self.client.post('/login', data=dict(email='test@test.com', password='test123', submit='Log In'),
                         follow_redirects=True)

        date_now = datetime.now()
        post = BlogPost(id=1, title="Titulo original", subtitle="Subtitulo original", img_url="https://teste.com",
                        body="Corpo original", date=date_now)
        with self.app.app_context():
            db.session.add(post)
            db.session.commit()

        response = self.client.get('/delete/1', follow_redirects=True)
        with self.app.app_context():
            post = BlogPost.query.get(1)
            self.assertIsNone(post)

        self.assertEqual(response.status_code, 200)

    def test_post_comment(self):
        date_now = datetime.now()
        post = BlogPost(id=1, title="Titulo Teste", subtitle="Subtitulo Teste", img_url="https://test.com",
                        body="Corpo teste", date=date_now)
        with self.app.app_context():
            db.session.add(post)
            db.session.commit()

        user = User(email='test3@test.com', name='test3',
                    password=generate_password_hash('test1234', method='pbkdf2:sha256', salt_length=8))
        with self.app.app_context():
            db.session.add(user)
            db.session.commit()

        self.client.post('/login', data=dict(email='test3@test.com', password='test1234', submit='Log In'),
                         follow_redirects=True)

        response = self.client.post('/post/1',
                                    data=dict(comment_text='Teste de comentario', submit='Submit Comment'),
                                    follow_redirects=True)

        with self.app.app_context():
            comment = Comment.query.filter_by(text='Teste de comentario').first()
        self.assertIsNotNone(comment)

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
