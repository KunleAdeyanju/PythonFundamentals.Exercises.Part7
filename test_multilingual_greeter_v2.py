from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import multilingual_greeter_v2

class MultilingualGreeterTestV2(TestCase):

    @patch('builtins.input', return_value="Harry Potter")
    def test_new_greeting_option(self, user_input):
        self.assertEqual("Harry Potter", multilingual_greeter_v2.new_greeting_option())