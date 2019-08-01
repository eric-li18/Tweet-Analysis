'''A3. Tester for the function common_words in tweets.
'''

import unittest
import tweets

class TestCommonWords(unittest.TestCase):
    '''Tester for the function common_words in tweets.
    '''

    def test_empty(self):
        '''Empty dictionary.'''

        arg1 = {}
        arg2 = 1
        exp_arg1 = {}
        tweets.common_words(arg1, arg2)
        
        """ exp_return = None
        act_return = 

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg) """

        msg = ("Expected dictionary to be\n {}, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_one_word_limit_one(self):
        '''Dictionary with one word.'''

        arg1 = {'hello': 2}
        arg2 = 1
        exp_arg1 = {'hello': 2}
        tweets.common_words(arg1, arg2)
        
        """ exp_return = None
        act_return = 

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg) """

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
    
    def test_lesser_limit(self):
        '''Dictionary with a limit less than the length of the total list'''
        arg1 = {"computer": 1, "work":3, "code":5, "program": 6}
        arg2 = 1
        exp_arg1 = {"program": 6}
        tweets.common_words(arg1, arg2)
        
        """ exp_return = None
        act_return = 

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg) """

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
        
        
    def test_greater_limit(self):
        '''Dictionary with a limit greater than the length of the total list'''
        arg1 = {"science": 1, "keyboard": 8, "mouse": 7, "camera": 2}
        arg2 = 8
        exp_arg1 = {"science": 1, "keyboard": 8, "mouse": 7, "camera": 2}
        tweets.common_words(arg1, arg2)
        
        """ exp_return = None
        act_return = 

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg) """

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
    
    def test_limit_equal_length(self):
        '''Dictionary with a limit equal to the length of the total list'''
        arg1 = {"csc": 5, "intro": 3, "laptop":4}
        arg2 = 3
        exp_arg1 = {'csc': 5, 'intro': 3, 'laptop': 4}
        tweets.common_words(arg1, arg2)
        
        """ exp_return = None
        act_return = 

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg) """

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
        
    def test_only_duplicate_past(self):
        '''Dictionary with only duplicate words that extend past the limit'''
        arg1 = {"hello": 5, "intro": 5, "laptop":5, "machine":5}
        arg2 = 3
        exp_arg1 = {}
        tweets.common_words(arg1, arg2)
        
        """ exp_return = None
        act_return = 

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg) """

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
        
    def test_duplicate_before(self):
        '''Dictionary with mix of duplicate words and non-duplicate words at 
        the end that extend past the limit'''
        arg1 = {"hello": 5, "intro": 5, "laptop":5, "machine":5,"robot":4, }
        arg2 = 3
        exp_arg1 = {}
        tweets.common_words(arg1, arg2)
        
        """ exp_return = None
        act_return = 

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg) """

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
       
    def test_duplicate_after(self): 
        '''Dictionary with mix of duplicate words after the non-duplicate 
        words'''
        arg1 = {"learning":6, "ai":7, "hello": 5, "intro": 5, "laptop":5, "a":5}
        arg2 = 3
        exp_arg1 = {"learning":6, "ai":7}
        tweets.common_words(arg1, arg2)
        
        """ exp_return = None
        act_return = 

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg) """

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
       
    def test_numerics(self):
        '''Dictionary with numbers'''
        arg1 = {"123": 4, "555": 3, "222":2, "789":1,"244":6}
        arg2 = 3
        exp_arg1 = {"244":6,"123": 4, "555": 3}
        tweets.common_words(arg1, arg2)
        
        """ exp_return = None
        act_return = 

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg) """

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
       
    def test_(self):
        '''Dictionary with mix of duplicate words and non-duplicate words 
        that extend past the limit'''
        arg1 = {"hello": 5, "intro": 5, "laptop":5, "machine":5,"robot":4, }
        arg2 = 3
        exp_arg1 = {}
        tweets.common_words(arg1, arg2)
        
        """ exp_return = None
        act_return = 

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg) """

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
       
if __name__ == '__main__':
    unittest.main(exit=False)
