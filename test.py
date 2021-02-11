
from  palindrome import isPalindrome
#from moveZero import moveZero
#from sentence import sentences
import  unittest


class TestPalindrome(unittest.TestCase):
    def test_blank(self):
        self.assertTrue(isPalindrome(''))

    def test_multipleWhiteSpace(self):
        self.assertTrue(isPalindrome('A   Santa         at Nasa'))

    def test_singleChar(self):
        self.assertTrue(isPalindrome('a'))

    def test_punctuation(self):
        self.assertFalse(isPalindrome('An.  Ana'))      

    def test_alphaNumeric(self):
        self.assertTrue(isPalindrome('an1n1na'))   

    def test_validPalindrome(self):
        self.assertTrue(isPalindrome('No lemon no melon'))  

    def test_invalidPalindrome(self):
        self.assertFalse(isPalindrome('No banana no melon'))  

if __name__ == '__main__':
    unittest.main()
