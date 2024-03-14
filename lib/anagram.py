class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word):
        matched_words = []
        for _ in word:
            if sorted(_.lower()) == sorted(self.word.lower()):
                matched_words.append(_)
        return matched_words


    