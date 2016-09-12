from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Lucas Gondim', cpf='12345678901',
                    email='lucascgondim@gmail.com', phone='34-99150-5026')
        self.response = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'lucascgondim@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = (
            'Lucas Gondim',
            '12345678901',
            'lucascgondim@gmail.com',
            '34-99150-5026'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)