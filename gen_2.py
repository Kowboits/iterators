nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2,[4,5,['e','r']], None],
]



def flat_generator(nested_list):
    for i in nested_list:
        if isinstance(i, list):
            for j in flat_generator(i):
                yield j
        else:
            yield i

if __name__ == "__main__":
    lst = [item for item in flat_generator(nested_list)]
    print(lst)