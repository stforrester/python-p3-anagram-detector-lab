# your code goes here!

class Anagram:
    
    def __init__(self, word):
        self.word = word
    
    def match(self, anagram_list):
        anagrams = []
        for item in anagram_list:
            item_list = list(item)
            if sorted(item_list) == sorted(self.word):
                anagrams.append(item)
        return anagrams