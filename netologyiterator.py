class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.lengths = [len(inner_list) for inner_list in list_of_list]
        self.item = []

    def __iter__(self):
        self.count = 0
        self.count2 = 0
        return self

    def __next__(self):
        if self.count >= len(self.list_of_list):
            raise StopIteration
        elif self.count2 >= self.lengths[self.count]:
            self.count += 1
            self.count2 = 0
            return self.__next__()
        else:
            self.item = self.list_of_list[self.count][self.count2]
            self.count2 += 1
            return self.item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
