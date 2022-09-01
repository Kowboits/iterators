nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2,[4,5,['e','r']], None],
]



def flat_generator(nested_list):
    for elem in nested_list:
        if isinstance(elem, list):
            for lst in flat_generator(elem):
                yield lst
        else:
            yield elem

if __name__ == "__main__":
    lst = [item for item in flat_generator(nested_list)]
    print(lst)