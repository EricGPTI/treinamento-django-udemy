from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.dados = {
            'nome': 'Eric Gomes',
            'email': 'ericgpt@gmail.com',
            'assunto': 'Testando views',
            'mensagem': 'Esta é uma mensagem de teste'
        }

        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Eric Gomes',
            'assunto': 'Testando views',
            'mensagem': 'Esta é uma mensagem de teste'
        }
        request = self.client.post(reverse_lazy('index'))
        self.assertEqual(request.status_code, 200)
