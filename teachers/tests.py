from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, Client
from django.views.generic.base import TemplateView

from .forms import TeacherSignUpForm
from .views import login
from .models import Teacher

class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_get_login(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_post_login(self):
        response = self.client.post('/login/', {
            'username': 'marek',
            'password': '123'
        })
        self.assertEqual(response.status_code, 302)

    def test_get_signup(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)

    def test_post_signup(self):
        response = self.client.post('/signup/', data={
            "password1": "pass",
            "password2": "pass",
            "username": "teacher",
        })
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        form = TeacherSignUpForm(data={
            "username": "user",
            "password1": "pass",
            "password2": "pass"
        })
        result = form.is_valid()
        self.assertEqual(form.errors['email'], ["This field is required."])
