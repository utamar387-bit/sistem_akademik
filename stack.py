class Stack:
	"""Stack berbasis list untuk menyimpan riwayat Undo (LIFO)."""

	def __init__(self):
		self.data = []

	def push(self, nilai):
		self.data.append(nilai)

	def pop(self):
		if not self.data:
			return None
		return self.data.pop()

	def peek(self):
		if not self.data:
			return None
		return self.data[-1]

	def kosong(self):
		return len(self.data) == 0