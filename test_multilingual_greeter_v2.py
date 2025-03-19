from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import multilingual_greeter_v2

class MultilingualGreeterTestV2(TestCase):

    @patch('builtins.input', return_value="Harry Potter")
    def test_new_greeting_option(self, user_input):
        self.assertEqual("Harry Potter", multilingual_greeter_v2.new_greeting_option())

    
    @patch('builtins.input', return_value= 4)
    def test_new_key_input(self, user_input):
        languages = {
            1: "English",
            2: "Spanish",
            3: "Portuguese"
        }

        actual = multilingual_greeter_v2.new_key_input(languages)
        self.assertEqual(4, actual)

    @patch('builtins.input', return_value= "German")
    def test_new_language_input(self, user_input):
        languages = {
            1: "English",
            2: "Spanish",
            3: "Portuguese"
        }

        actual = multilingual_greeter_v2.new_language_option_input(languages)
        self.assertEqual("German", actual)