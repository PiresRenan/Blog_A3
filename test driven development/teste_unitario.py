import sys
import unittest
from werkzeug.security import generate_password_hash

sys.path.insert(0, '..')

from main import app, db, User


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register_route(self):
        response = self.client.post('/register',
                                    data=dict(email='test@test.com', name='test', password='test123', submit='Sign Up'),
                                    follow_redirects=True)
        user = User.query.filter_by(email='test@test.com').first()
        self.assertIsNotNone(user)
        self.assertEqual(response.status_code, 200)

    def test_login_route(self):
        hashed_password = generate_password_hash('test123', method='pbkdf2:sha256', salt_length=8)
        user = User(email='test@test.com', name='test', password=hashed_password)
        db.session.add(user)
        db.session.commit()

        response = self.client.post('/login', data=dict(email='test@test.com', password='test123', submit='Log In'),
                                    follow_redirects=True)

        with self.client.session_transaction() as sess:
            self.assertIn('_user_id', sess)

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
