"""Assignment 3: Tweet Analysis"""

from typing import List, Dict, TextIO, Tuple

HASH_SYMBOL = '#'
MENTION_SYMBOL = '@'
URL_START = 'http'

# Order of data in the file
FILE_DATE_INDEX = 0
FILE_LOCATION_INDEX = 1
FILE_SOURCE_INDEX = 2
FILE_FAVOURITE_INDEX = 3
FILE_RETWEET_INDEX = 4

# Order of data in a tweet tuple
TWEET_TEXT_INDEX = 0
TWEET_DATE_INDEX = 1
TWEET_SOURCE_INDEX = 2
TWEET_FAVOURITE_INDEX = 3
TWEET_RETWEET_INDEX = 4

# Helper functions.

def alnum_prefix(text: str) -> str:
    """Return the alphanumeric prefix of text, converted to
    lowercase. That is, return all characters in text from the
    beginning until the first non-alphanumeric character or until the
    end of text, if text does not contain any non-alphanumeric
    characters.

    >>> alnum_prefix('')
    ''
    >>> alnum_prefix('IamIamIam')
    'iamiamiam'
    >>> alnum_prefix('IamIamIam!!')
    'iamiamiam'
    >>> alnum_prefix('IamIamIam!!andMore')
    'iamiamiam'
    >>> alnum_prefix('$$$money')
    ''

    """

    index = 0
    while index < len(text) and text[index].isalnum():
        index += 1
    return text[:index].lower()


def clean_word(word: str) -> str:
    """Return all alphanumeric characters from word, in the same order as
    they appear in word, converted to lowercase.

    >>> clean_word('')
    ''
    >>> clean_word('AlreadyClean?')
    'alreadyclean'
    >>> clean_word('very123mes$_sy?')
    'very123messy'

    """

    cleaned_word = ''
    for char in word.lower():
        if char.isalnum():
            cleaned_word = cleaned_word + char
    return cleaned_word


# Required functions

def extract_mentions(text: str) -> List[str]:
    """Return a list of all mentions in text, converted to lowercase, with
    duplicates included.

    >>> extract_mentions('Hi @UofT do you like @cats @CATS #meowmeow')
    ['uoft', 'cats', 'cats']
    >>> extract_mentions('@cats are #cute @cats @cat meow @meow')
    ['cats', 'cats', 'cat', 'meow']
    >>> extract_mentions('@many @cats$extra @meow?!')
    ['many', 'cats', 'meow']
    >>> extract_mentions('No valid mentions @! here?')
    []

    """
    mention_list = []
    new_text = text.split(" ")
    for word in new_text:
        if len(word) > 1 and MENTION_SYMBOL == word[0] and word[1].isalnum():
            mention_list.append(alnum_prefix(word[1:]))
    return mention_list
    
def extract_hashtags(text: str) -> List[str]:
    """Return a list in the order of all the distinct hashtags in text, 
    converted to lowercase and without the intial hash symbol.
    
    >>> extract_hashtags("I love #CompSci and I want to tweet about #COMPSCI")
    ['compsci']
    >>> extract_hashtags("I do not know if this hashtag is viable #!")
    []
    >>> extract_hashtags("@python check my #code!Please #compile #CODE?")
    ['code', 'compile']
    """
    hashtag_list = []
    new_text = text.split(" ")
    for word in new_text:
        if len(word) > 1 and HASH_SYMBOL == word[0] and word[1].isalnum() and\
           alnum_prefix(word[1:]) not in hashtag_list:
            hashtag_list.append(alnum_prefix(word[1:]))
    return hashtag_list

def count_words(text: str, word_dict: Dict[str, int]) -> None:
    """Modify a dictionary by updating the counts of values whose lowercase 
    string keys show up in the text and if a word is not the dictionary yet, 
    it should be added. Keys, mentions, hashtags, empty strings and URLs are 
    not considered
    
    >>> dictionary = {"nick":0, "frosst":0, "google":0, "brain":0, "researcher"\
    :0, "day":0, "singer":0, "night":0} 
    >>> count_words("#UofT Nick Frosst: Google Brain re-searcher by day, singer\
    @goodkidband by night!", dictionary)
    >>> dictionary == {"nick":1, "frosst":1, "google":1, "brain":1, \
    "researcher":1, "by": 2, "day":1, "singer":1, "night":1}
    True
    
    >>> dictionary = {} 
    >>> count_words("@_AlecJacobson: @UofTCompSci is hiring in \
    ComputationalGeometry. Tell your friends if they love Computational \
    Geometry!", dictionary)
    >>> dictionary == {'is': 1, 'hiring': 1, 'in': 1, 'computational': 2,\
    'geometry': 2, 'tell': 1, 'your': 1, 'friends': 1, 'if': 1, 'they': 1, \
    'love': 1} 
    False
    """
    new_text = text.split(" ")
    for word in new_text:
        if (len(word) > 1 and not(HASH_SYMBOL in word[0] or MENTION_SYMBOL 
                                  in word[0] or URL_START in word[0])):
            new_word = clean_word(word)
            if new_word not in word_dict and new_word != "":
                word_dict[new_word] = 1
            elif new_word in word_dict and new_word != "":
                word_dict[new_word] += 1
            
def common_words(dictionary: Dict[str, int], num: int) -> None:
    """Update the given dictionary so that it only includes the highest
    frequency words. At most num words should be kept in the dictionary. If
    including all words with a particular word count would result in a
    dictionary with more than num words, then none of the words with that
    word count should be included.
    
    Precondition: num > 0
    
    >>> dictionary = {"computer": 1, "work":3, "code":5, "program": 5}
    >>> common_words(dictionary, 1)
    >>> dictionary == {}
    True
    
    >>> dictionary_1 = {"csc": 5, "intro": 3, "laptop":4}
    >>> common_words(dictionary_1, 3)
    >>> dictionary_1 == {'csc': 5, 'intro': 3, 'laptop': 4}
    True
    
    >>> dictionary_2 = {"science": 1, "keyboard": 8, "mouse": 7, "camera": 2}
    >>> common_words(dictionary_2, 8)
    >>> dictionary_2 == {'science': 1, 'keyboard': 8, 'mouse': 7, 'camera': 2}
    True
    """
    count_list = []
    for word in dictionary:
        count_list.append(dictionary[word])
    count_list.sort()
    count_list.reverse()
    if len(count_list) > num and count_list[num] == count_list[num-1]:
        duplicate = count_list.index(count_list[num])
        count_list = count_list[0: duplicate]
    else: 
        count_list = count_list[0:num]
    word_list = []
    for word in dictionary:
        if dictionary[word] not in count_list:
            word_list.append(word)
    if len(word_list) != 0:
        for deleted_word in word_list:
            del dictionary[deleted_word]

def read_tweets(file: TextIO) -> Dict[str, List[tuple]]:
    """ Return a dictionary with the key as the lowercase username of each 
    tweeter and the values as a list of tuples with information of each tweet
    that the user has tweeted given file, which contains tweets.
    """
    new_file = file.readlines()
    dictionary = {}
    index = -1
    for tweet in new_file:
        index += 1
        if len(tweet) > 3 and " " not in tweet and ":" == tweet[-2]:
            tweet = tweet.strip()            
            user = tweet[0:-1]
            dictionary[user.lower()] = []
        elif index != 0 and new_file[index - 1] == "<<<EOT\n" \
             or (user + ":") in new_file[index - 1]:
            tweet = tweet.strip()            
            tweet_prop = data_list(tweet)
        elif index != 0 and tweet != "<<<EOT\n" and type(tweet_prop) != tuple: 
            end_of_text = new_file.index("<<<EOT\n", index)
            for tweet_text in new_file[index:end_of_text]:
                if tweet_text not in tweet or tweet_text == '\n':
                    tweet = tweet + tweet_text
            tweet_prop = correct_tweet(tweet, tweet_prop)
            dictionary[user.lower()].append(tweet_prop)  
    return dictionary

def correct_tweet(tweet: str, tweet_prop: List) -> tuple:
    """ Return a tuple with the tweet inserted correctly into the 
    TWEET_TEXT_INDEX in tweet_prop.
    
    >>> correct_tweet("hello", [20181108132750, 'Twitter for Android', 0, 50])
    ('hello', 20181108132750, 'Twitter for Android', 0, 50)
    
    >>> correct_tweet("here", [20181103122515, 'Twitter for Android', 5, 0])
    ('here', 20181103122515, 'Twitter for Android', 5, 0)
    """
    tweet = tweet.strip()                    
    tweet_prop.insert(0, tweet) 
    tweet_prop = tuple(tweet_prop)    
    return tweet_prop

def create_file(file: TextIO) -> List[str]:
    """ Return a list created from the text data in file with all the newline
    characters stripped, and all empty lines removed.
    """
    file = file.readlines()
    new_file = []
    for line in file:
            new_file.append(line)
    return new_file

def data_list(tweet_data: str) -> List:
    """ Return a list of string and int of the tweet properties arranged in
    the order specified in the assignment outline when given the comma
    separated string tweet_data.
    
    >>> data_list("20181108132750,Unknown Location,Twitter for Android,0,50")
    [20181108132750, 'Twitter for Android', 0, 50]
    
    >>> data_list("20181103122515,Toronto Ontario,Twitter for Android,5,0")
    [20181103122515, 'Twitter for Android', 5, 0]
    """
    tweet_data = tweet_data.split(",")
    new_tweet_data = []
    
    tweet_data[FILE_RETWEET_INDEX] = int(tweet_data[FILE_RETWEET_INDEX])
    tweet_data[FILE_FAVOURITE_INDEX] = int(tweet_data[FILE_FAVOURITE_INDEX])
    tweet_data[FILE_DATE_INDEX] = int(tweet_data[FILE_DATE_INDEX])
    
    new_tweet_data.insert(TWEET_DATE_INDEX, tweet_data[FILE_DATE_INDEX])
    new_tweet_data.insert(TWEET_SOURCE_INDEX, tweet_data[FILE_SOURCE_INDEX])
    new_tweet_data.insert(TWEET_FAVOURITE_INDEX,
                          tweet_data[FILE_FAVOURITE_INDEX])
    new_tweet_data.insert(TWEET_RETWEET_INDEX, tweet_data[FILE_RETWEET_INDEX])
    return new_tweet_data

def most_popular(dictionary: Dict[str, List[tuple]], start_date: int,
                 end_date: int) -> str:
    """ Return the tweeter, from a dictionary of all the users who have
    tweeted, who has the most retweets and favourites between the time of
    start_date and end_date, inclusive, or return the string tie if no tweets
    are in that range or there is a tie between users.
    
    Precondition: start_date <= end_date
    
    >>> most_popular({'utsc':[('welcome to utsc',20181110133750,'Twitter\
    for Android',0,3),('university',20181112135240,'Twitter for\
    Android',0,1)], 'amacss':[('join amacss',20181109181012,'Twitter for\
    Android',9,7),('event',20181110134750,'Twitter for\
    Android',0,1)]},20181012135240 , 20181210133700)
    'amacss'
    
    >>> most_popular({'cms':[('department',20181110133750,'Twitter for\
    Android',0,1),('math',20181110152750,'Twitter for Android',0,1)],\
    'csec':[('computer science club',20181110133750,'Twitter for\
    Android',0,1),('machine learning',20181110133700,'Twitter for\
    Android',0,1)]}, 20171110133750, 20191110133750)
    'tie'
    """
    count_list = []
    popularity = {}
    for user in dictionary:
        total = 0
        for data in dictionary[user]:
            if start_date <= data[TWEET_DATE_INDEX] and\
               data[TWEET_DATE_INDEX] <= end_date:
                total += data[TWEET_FAVOURITE_INDEX] +\
                    data[TWEET_RETWEET_INDEX]
        popularity[user] = total
        if total != 0:
            count_list.append(total)
    if len(count_list) != 0 and count_list.count(max(count_list)) == 1:
        popular = max(count_list)
        for name in popularity:
            number = popularity.get(name)
            if number == popular:
                return name
        return "tie"
    else:
        return "tie"

def detect_author(dictionary: Dict[str, List[tuple]], text: str) -> str:
    """ Return the lowercase username of the most likely author of the tweet
    text based on their used hashtags from dictionary, and if all hashtags
    are uniquely used by one user, return that username, else return string
    unknown.
    
    >>> detect_author({'utsc':[('welcome to utsc #utsc \
    #welcome',20181110133750,'Twitter for Android',0,3),('university #utsc\
    #uni',20181112135240,'Twitter for Android',0,1)], 'amacss':[('join\
    amacss #club #social',20181109181012,'Twitter for Android',9,7),('event\
    #event #club',20181110134750,'Twitter for Android',0,1)]}, '#Welcome to\
    the school! We hope you enjoy your time at #UTSC and place at this\
    #uni!') 
    'utsc'
    
    >>> detect_author({'cms':[('department #cms',20181110133750,'Twitter\
    for Android',0,1),('math #math',20181110152750,'Twitter for\
    Android',0,1)], 'csec':[('computer science club\
    #club',20181110133750,'Twitter for Android',0,1),('machine learning\
    #math',20181110133700,'Twitter for Android',0,1)]}, "#cms is the\
    department to look for if you need information on #math degrees")
    'unknown'
    
    >>> detect_author({'cms':[('department #cms',20181110133750,'Twitter\
    for Android',0,1),('math #math', 20181110152750,'Twitter for\
    Android',0,1)], 'csec':[('computer science club\
    #club', 20181110133750,'Twitter for Android',0,1),('machine\
    learning', 20181110133700,'Twitter for Android',0,1)]}, "#cms is the\
    department to look for if you need information on #math degrees") 
    'cms'
    
    >>> detect_author({'cms':[('department #cms', 20181110133750,'Twitter\
    for Android',0,1),('math #math', 20181110152750,'Twitter for\
    Android',0,1)], 'csec':[('computer science club\
    #club',20181110133750,'Twitter for Android',0,1),('machine\
    learning',20181110133700,'Twitter for Android',0,1)]}, "#asc is the\
    department to look for if you need information on #math degrees")
    'unknown'
    """
    unique_user = []
    hashtag_text = extract_hashtags(text)
    if len(hashtag_text) == 0:
        return "unknown"
        
    for hashtag in hashtag_text:
        for user in dictionary:
            user_hashtags = all_hashtags(dictionary[user])
            if hashtag in user_hashtags:
                if unique_user == [] or user in unique_user:
                    unique_user.append(user)
                elif user not in unique_user:
                    return "unknown"
    if len(unique_user) == len(hashtag_text):
        return unique_user[0]
    return "unknown"
              
def all_hashtags(tweets: List[tuple]) -> List[str]:
    """ Return a list of string containing the hashtags from the given tuple
    of tweets.
    
    >>> all_hashtags([('department #cms', 20181110133750,'Twitter for Android'\
    ,0,1),('math #math', 20181110152750,'Twitter for\
    Android',0,1)])
    ['cms', 'math']
    
    >>> all_hashtags([('computer science club #club',20181110133750, \
    'Twitter for Android',0,1),('machine learning #math', 20181110133700,\
    'Twitter for Android',0,1)])
    ['club', 'math']
    """
    hashtag_list = []
    for data in tweets:
        hashtag_list.extend(extract_hashtags(data[TWEET_TEXT_INDEX]))
    return hashtag_list
            
if __name__ == '__main__':
    pass

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    import doctest
    doctest.testmod()
