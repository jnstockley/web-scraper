from unittest import TestCase

from main import main


class TestStartup(TestCase):
    def test_startup(self):
        main()
        assert True
