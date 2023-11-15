class WordCounter:
    def __init__(self, sentence):
        self.sentence = sentence
        self.shortest_word = None
        self.longest_word = None

    def  count_words(self):
        list = self.sentence.split()
        self.length = len(list)
        for word in list:
            word_length = len(word)
            if self.shortest_word is None or word_length < self.shortest_word:
                self.shortest_word = word_length
            if self.longest_word is None or word_length > self.longest_word:
                self.longest_word = word_length
    def get_word_count(self):
        return self.length
    def get_shortest_word(self):
        return self.shortest_word
    def get_longest_word(self):
        return self.longest_word