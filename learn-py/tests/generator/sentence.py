import unittest
from generator import sentence


class MyTestCase(unittest.TestCase):
    def test_sentence():
        s = sentence.Sentence('"The time ha... Walrus said,')
        for word in s:
            print(word)
        print(list(s))

    def test_sentence_iter(self):
        s = sentence.SentenceIterator('"The time ha... Walrus said,')
        for word in s:
            print(word)
        # print nothing
        print(list(s))
        # print list by reset iterator
        s = sentence.SentenceIterator('"The time ha... Walrus said,')
        print(list(s))

    def test_sentence_generator(self):
        s = sentence.SentenceGenerator('"The time ha... Walrus said,')
        for word in s:
            print(word)
        print(list(s))

    def test_sentence_lazy_generator(self):
        s = sentence.SentenceLazyGenerator('"The time ha... Walrus said,')
        for word in s:
            print(word)
        print(list(s))

    def test_sentence_generator_exp(self):
        s = sentence.SentenceGeneratorExp('"The time ha... Walrus said,')
        for word in s:
            print(word)
        print(list(s))


if __name__ == '__main__':
    unittest.main()
