nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]
class FlatIterator:

	def __init__(self, n_list):
		self.list = n_list
		self.cursor = -1
		self.cursor2 = 0
		self.list_len = len(self.list)

	def __iter__(self):
		self.cursor += 1
		self.cursor2 = 0
		return self

	def __next__(self):
		while self.cursor - self.list_len and self.cursor2== len(self.list[self.cursor]):
			iter(self)
		if self.cursor == self.list_len:
			raise StopIteration
		self.cursor2 += 1
		return self.list[self.cursor][self.cursor2 - 1]


if __name__ == "__main__":


	for item in FlatIterator(nested_list):
		print(item)
	flat_list = [item for item in FlatIterator(nested_list)]
	print(flat_list)