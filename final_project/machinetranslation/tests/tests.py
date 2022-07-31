""" This Test File tests the translate functions 
    written in "../translator.py" 
"""

import unittest
import sys, os

sys.path.append("..")
from translator import english_to_french, french_to_english


class TestFrenchToEnglish(unittest.TestCase):
    def testNull(self):
        self.assertIsNone(french_to_english(None), msg="Something went wrong.")
    def testBonjour(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello", msg="Something went wrong.")



class TestEnglishToFrench(unittest.TestCase):
    def testNull(self):
        self.assertIsNone(english_to_french(None), msg ="Something went wrong.")
    def testHello(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour", msg ="Something went wrong.")



if __name__ == "__main__":
    unittest.main()