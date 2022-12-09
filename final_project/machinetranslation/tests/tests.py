import unittest
from translator import english_to_french
from translator import french_to_english
class testEtoF(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello, how are you today?"),"Bonjour, comment vous êtes aujourd'hui?")
    def test2(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test3(self):
        self.assertNotEqual(english_to_french("None"),'')
    def test4(self):
        self.assertNotEqual(english_to_french(0),0)


class testFtoE(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour, comment vous êtes aujourd'hui?"),"Hello, how are you today?")
    def test2(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test3(self):
        self.assertNotEqual(french_to_english("None"),'')
    def test4(self):
        self.assertNotEqual(french_to_english(0),0)

unittest.main()