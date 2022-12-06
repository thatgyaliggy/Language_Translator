"""Unit test file for Translator.py"""
import unittest
from translator import english_to_french
from translator import english_to_german

class TestE2F(unittest.TestCase):
    """English to French tests"""
    def test1(self):
        """Test Hello returns Bonjour"""
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # Test Hello does not return Hello
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        # Test None returns empty string
        self.assertNotEqual(english_to_french("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(english_to_french(0), 0)

class TestE2G(unittest.TestCase):
    """English to German tests"""
    def test1(self):
        """Test Hello returns Hallo"""
        self.assertEqual(english_to_german('Hello'), 'Hallo')
        # Test Hello does not return Hello
        self.assertNotEqual(english_to_german('Hello'), 'Hello')
        # Test None returns empty string
        self.assertNotEqual(english_to_german("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(english_to_german(0), 0)

unittest.main()
