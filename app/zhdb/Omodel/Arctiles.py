import time


class Arctiles(object):
    def __init__(self, classify=None, title=None, text=None):
        self.classify = classify
        self.title = title
        self.text = text
        self.date = time.time()

    def to_dict(self):
        # self.__dict__.pop('password')
        return self.__dict__

