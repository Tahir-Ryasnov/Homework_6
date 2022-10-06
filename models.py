class FlatIterator:
    def __init__(self, some_list):
        self.nested_list = some_list

    def __iter__(self):
        self.item = iter(self.nested_list)
        self.result = []
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.result) == self.cursor:
            self.result = None
            self.cursor = 0
        if not self.result:
            self.result = next(self.item)
        return self.result[self.cursor]


def flat_generator(some_lists):
    for some_list in some_lists:
        for el in some_list:
            yield el
