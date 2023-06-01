import sys
import unittest
from werkzeug.security import generate_password_hash

sys.path.insert(0, '..')

from app import app, db, User


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        with self.app.app_context():
            db.create_all()

        self.test_user = User(email='test@test.com', name='test', password=generate_password_hash('test123', method='pbkdf2:sha256', salt_length=8))
        with self.app.app_context():
            db.session.add(self.test_user)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def teste_registro(self):
        response = self.client.post('/register', data=dict(email='test2@test.com', name='test2', password='test1234', submit='Sign Up'), follow_redirects=True)
        user = User.query.filter_by(email='test2@test.com').first()
        self.assertIsNotNone(user)
        self.assertEqual(response.status_code, 200)

    def test_register_existing_email(self):
        response = self.client.post('/register', data=dict(email='test@test.com', name='test2', password='test1234',
                                                           submit='Sign Up'), follow_redirects=True)
        self.assertIn("Este email já foi cadastrado anteriormente, entre ao inves de cadastrar!",
                      response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_register_invalid_password(self):
        response = self.client.post('/register', data=dict(email='test2@test.com', name='test2', password='123', submit='Sign Up'), follow_redirects=True)
        self.assertIn("Field must be between 4 and 100 characters long.", response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_login_route(self):
        response = self.client.post('/login', data=dict(email='test@test.com', password='test123', submit='Log In'),
                                    follow_redirects=True)

        with self.client.session_transaction() as sess:
            self.assertIn('_user_id', sess)

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
