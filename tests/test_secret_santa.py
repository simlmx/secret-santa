from unittest import TestCase
import os
from secret_santa import choose_receiver, Person, create_pairs

class TestSecretSanta(TestCase):

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

    def test_creates_right_number_of_pairs(self):
        hans  = Person('Hans', 'hans@email.com', 'Uschi')
        uschi = Person('Uschi', 'uschi@email.com', 'Frank')
        frank = Person('Frank', 'frank@email.com', 'Hans')
        arndt = Person('Arndt', 'arndt@email.com')
        antje = Person('Antje', 'antje@email.com')
        people = [hans, uschi, frank, arndt, antje]
        pairs = create_pairs(people, people.copy())
        self.assertEqual(len(pairs), len(people))
        

