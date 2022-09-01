
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

def flat_generator(nested_list):
    for i in range(len(nested_list)):
        for j in range(len(nested_list[i])):
            yield (nested_list[i][j])

for item in  flat_generator(nested_list):
	print(item)
print(flat_generator(nested_list))
lst = [item for item in flat_generator(nested_list)]
print(lst)