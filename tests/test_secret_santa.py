from unittest import TestCase
import os
from secret_santa import parse_yaml

class TestSecretSanta(TestCase):

    def test_parse_yaml(self):
        CONFIG_PATH = os.path.join(os.path.dirname(__file__), '../config.yml.template')
        parsed = parse_yaml(yaml_path=CONFIG_PATH)
        self.assertTrue(parsed['MESSAGE'])
        self.assertTrue(parsed['PASSWORD'])
        self.assertTrue(parsed['TIMEZONE'])
        self.assertTrue(parsed['SMTP_PORT'])
        self.assertTrue(parsed['DONT_PAIR'])
        self.assertTrue(parsed['PARTICIPANTS'])
        self.assertTrue(parsed['SUBJECT'])
        self.assertTrue(parsed['FROM'])
        self.assertTrue(parsed['SMTP_SERVER'])
        self.assertTrue(parsed['USERNAME'])
        
