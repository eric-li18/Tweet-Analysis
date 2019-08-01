'''A3. Tester for the function extract_mentions in tweets.
'''

import unittest
import tweets

class TestExtractMentions(unittest.TestCase):
    '''Tester for the function extract_mentions in tweets.
    '''

    def test_empty(self):
        '''Empty tweet.'''

        arg = ''
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_no_mention(self):
        '''Non-empty tweet with no mentions.'''

        arg = 'tweet test case'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_mentions_behind(self):
        '''Mentions directly behind text'''
        arg = 'many@cats@meow'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_lower_uppercase(self):
        '''Duplicate mentions of different cases'''
        arg = '@wing, @WING'
        actual = tweets.extract_mentions(arg)
        expected = ['wing', 'wing']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_nonempty_single(self): 
        '''Nonempty mention with one single character'''
        arg = '@i'
        actual = tweets.extract_mentions(arg)
        expected = ['i']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_double(self):
        '''Double @ character with an invalid mention'''
        arg = '@@hello'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
        
    def test_at_end(self):
        '''Invalid mention with an at symbol at the end'''
        arg = 'hello my name is @'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
    
    def test_invalid_single(self):
        '''Invalid single mention with a single not valid character'''
        arg = '@!'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)       
        
    def test_single_mention(self):
        '''Nonempty mention with one single mention'''
        arg = '@ohio'
        actual = tweets.extract_mentions(arg)
        expected = ['ohio']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_multiple_mentions(self):
        '''Nonempty mention with multiple mentions'''
        arg = '@ohio @vermont @nyc'
        actual = tweets.extract_mentions(arg)
        expected = ['ohio', 'vermont', 'nyc']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
if __name__ == '__main__':
    unittest.main(exit=False)
