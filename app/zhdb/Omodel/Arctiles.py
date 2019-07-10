import time


class Arctiles(object):
    def __init__(self, classify=None, title=None, text=None, author=None):
        self.classify = classify
        self.title = title
        self.text = text
        self.date = str(time.time())
        self.author = author

    def to_dict(self):
        # self.__dict__.pop('password')
        return self.__dict__
