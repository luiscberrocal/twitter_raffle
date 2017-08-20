from django.core.management import call_command
from django.test import TestCase
from django_test_tools.mixins import TestCommandMixin


class TestHelloTweepyCommand(TestCommandMixin, TestCase):

    def test_command(self):

        call_command('hellotweepy', stdout=self.content)
        self.assertTrue(len(self.get_results()) > 20)
