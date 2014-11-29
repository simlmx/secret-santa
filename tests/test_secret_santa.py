from unittest import TestCase
import os
from secret_santa import parse_yaml, choose_receiver, Person, create_pairs

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

    def test_chooses_legitimate_receiver(self):
        hans  = Person('Hans', 'hans@email.com', 'Uschi')
        uschi = Person('Uschi', 'uschi@email.com', None)
        frank = Person('Frank', 'frank@email.com', None)
        
        receiver = choose_receiver(hans, [uschi, frank])

        self.assertEqual(receiver, frank)
        
    def test_doesnt_always_choose_the_same_receiver(self):
        hans  = Person('Hans',  'hans@email.com',  'None')
        uschi = Person('Uschi', 'uschi@email.com', 'None')
        frank = Person('Frank', 'frank@email.com', 'None')
        
        uschi_received = False
        frank_received = False

        for i in range(100):
            receiver = choose_receiver(hans, [uschi, frank])
            if receiver == uschi:
                uschi_received = True
            if receiver == frank:
                frank_received = True

        self.assertTrue(uschi_received, "Uschi never received anything.")
        self.assertTrue(frank_received, "Frank never received anything.")

    def test_blocks_work_one_way_only(self):
        hans  = Person('Hans', 'hans@email.com', 'Uschi')
        uschi = Person('Uschi', 'uschi@email.com', 'Frank')
        frank = Person('Frank', 'frank@email.com', 'Hans')
        people = [hans, uschi, frank]
        pairs = create_pairs(people, people.copy())
        for pair in pairs:
            if pair.giver == hans:
                self.assertEqual(pair.receiver, frank)
            if pair.giver == uschi:
                self.assertEqual(pair.receiver, hans)
            if pair.giver == frank:
                self.assertEqual(pair.receiver, uschi)

        

