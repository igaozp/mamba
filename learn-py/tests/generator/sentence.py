import unittest
from generator import sentence


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = sentence.Sentence('"The time ha... Walrus said,')
        for word in s:
            print(word)
        print(list(s))


if __name__ == '__main__':
    unittest.main()
