from animal_shelter import Animal, Animal_Shelter
import unittest

class Test_Case_Animal_Shelter(unittest.TestCase):
    def test_animal_shelter(self):
        shelter = Animal_Shelter()
        shelter.enqueue(Animal('felix', 'cat'))
        shelter.enqueue(Animal('woof', 'dog'))
        self.assertEqual(shelter.deque_any().name, 'felix')
        shelter.enqueue(Animal('woof2', 'dog'))
        self.assertEqual(shelter.deque_any().name, 'woof')
        shelter.enqueue(Animal('felix', 'cat'))
        shelter.enqueue(Animal('woof', 'dog'))
        shelter.enqueue(Animal('felix', 'cat'))
        shelter.enqueue(Animal('woof', 'dog'))
        self.assertEqual(shelter.deque_any().name, 'woof2')
