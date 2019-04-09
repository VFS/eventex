from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(
            name="Henrique Bastos",
            cpf="33333333333",
            email="henrique@bastos.net",
            phone="11-99999-9999",
        )
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = "Confirmação de Inscrição"
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = "contato@eventex.labs.vfs.io"
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.labs.vfs.io', "henrique@bastos.net"]
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            "Henrique Bastos",
            "33333333333",
            "henrique@bastos.net",
            "11-99999-9999",
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
