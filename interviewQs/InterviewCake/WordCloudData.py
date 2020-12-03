# Write code that takes a long string and builds its word cloud data in a dictionary, where the keys are words and the values are the number of times the words occurred.


import unittest


class WordCloudData(object):

    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)

    def populate_words_to_counts(self, input_string):
        # Iterates over each char in the input string, splitting 
        # words and passing them to add_words_to_dictionary()
        current_word_head_index = 0
        current_word_length = 0
        for i, character in enumerate(input_string):
            
            # If end of string check for last letter
            if i == len(input_string) - 1:
                if character.isalpha():
                    current_word_length += 1
                if current_word_length > 0:
                    current_word = input_string[current_word_head_index:\
                        current_word_head_index + current_word_length]
                    self.add_word_to_dictionary(current_word)
                    
            # If we reached space or em dash, end of word so add word to dict
            elif character == ' ' or character == '\u2014':
                if current_word_length > 0:
                    current_word = input_string[current_word_head_index:\
                        current_word_head_index + current_word_length]
                    self.add_word_to_dictionary(current_word)
                    current_word_length = 0
            
            # If ellipsis, then split on them and add word to dictionary
            elif character ==  '.':
                if i < len(input_string) - 1 and input_string[i + 1] == '.':
                    if current_word_length > 0:
                        current_word = input_string[current_word_head_index:\
                            current_word_head_index + current_word_length]
                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0
    
            # If char or apostrophe, add it to current word
            elif character.isalpha() or character == '\'':
                if current_word_length == 0:
                    current_word_head_index = i
                current_word_length += 1
            
            # If hyphen and surrounded by letters add to dict
            elif character == '-':
                if i > 0 and input_string[i - 1].isalpha() and \
                    input_string[i + 1].isalpha():
                    if current_word_length == 0:
                        current_word_head_index = i
                    current_word_length += 1
                else:
                    if current_word_length > 0:
                        current_word = input_string[current_word_head_index:\
                            current_word_head_index + current_word_length]
                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0
        
    def add_word_to_dictionary(self, word):
        # If word already in dictionary, increment count
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1
            
        # If a lowercase version present in dictionary, input is uppercase
        # increment its count
        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1
        
        # If uppercase versent present in dictionary, input is lowercase
        # change dict version to lowercase and increment
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]

        # Otherwise the word doesn't exist, add to dictionary
        else:
            self.words_to_counts[word] = 1














# Tests

# There are lots of valid solutions for this one. You
# might have to edit some of these tests if you made
# different design decisions in your solution.

class Test(unittest.TestCase):

    def test_simple_sentence(self):
        input = 'I like cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'I': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input = 'Chocolate cake for dinner and pound cake for dessert'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'Chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input = 'Strawberry short cake? Yum!'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Strawberry': 1, 'short': 1, 'Yum': 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input = 'Dessert - mille-feuille cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Dessert': 1, 'mille-feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = 'Mmm...mmm...decisions...decisions'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input = "Allie's Bakery: Sasha's Cakes"

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {"Bakery": 1, "Cakes": 1, "Allie's": 1, "Sasha's": 1}
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)