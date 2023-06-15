class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, words):
        matching_words = [word for word in words if sorted(word) == sorted(self.word)]
        return matching_words
