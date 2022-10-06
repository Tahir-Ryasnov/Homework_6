from models import FlatIterator, flat_generator


if __name__ == '__main__':

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]  # generator comprehension
    print(flat_list)

    for item in flat_generator(nested_list):
        print(item)
        