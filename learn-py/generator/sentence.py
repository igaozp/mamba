import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


class SentenceIterator:
    def __init__(self, text):
        self.words = RE_WORD.findall(text)
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


class SentenceGenerator:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'SentenceGenerator(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word


class SentenceLazyGenerator:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'SentenceLazyGenerator(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()


class SentenceGeneratorExp:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'SentenceGeneratorExp(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))