# Given a words.txt file containing a newline-delimited list of dictionary
#  words, please implement the Anagrams class so that the get_anagrams() method
#  returns all anagrams from words.txt for a given word.
#
# ## Bonus requirements:
#   - Optimise the code for fast retrieval
#   - Write more tests
#   - Thread safe implementation
#
import unittest
import threading
from collections import defaultdict

class Anagrams:

    def __init__(self):
        self.anagramDict = defaultdict(list)
        lock = threading.Lock()
        # Locking the thread while reading the text file and  adding to the dictionary to make it thread safe
        with lock:
            self.words = open('words.txt').readlines()
            # Creating a dictionary of lists where the key is the word sorted in alphabetical order
            # and the value is a list of anagrams for that word
            for word in self.words:
                word = word.lower().replace('\r', '').replace('\n', '')
                sortedWord=''.join(sorted(word))
                self.anagramDict[sortedWord].append(word)

    def get_anagrams(self, word):
        # Dictionary lookup is the fastest for retrieval i.e the  average time complexity is  O(1).
        listOfAnagrams=self.anagramDict[''.join(sorted(word.lower()))]
        return listOfAnagrams

class TestAnagrams(unittest.TestCase):

    def test_anagrams(self):
        anagrams = Anagrams()
        self.assertEquals(anagrams.get_anagrams('plates'), ['palest', 'pastel', 'petals', 'plates', 'staple'])
        self.assertEquals(anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])
        self.assertEquals(anagrams.get_anagrams('andrew'), ['andrew', 'wander', 'warden', 'warned'])
        self.assertEquals(anagrams.get_anagrams('present'),['present', 'repents', 'serpent'])
        self.assertEquals(anagrams.get_anagrams('repents'), ['present', 'repents', 'serpent'])
        self.assertEquals(anagrams.get_anagrams(''), [])
        self.assertEquals(anagrams.get_anagrams('WordNotInList'), [])
        self.assertNotEquals(anagrams.get_anagrams('andrew'), ['andrew1', 'wander', 'warden', 'warned'])

if __name__ == '__main__':
    unittest.main()