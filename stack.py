# ============================================================
# STACK
# ============================================================
# File ini digunakan untuk membuat Stack.
#
# Stack digunakan untuk fitur Undo.
#
# Prinsip:
# LIFO = Last In First Out
#
# Data yang terakhir masuk akan keluar terlebih dahulu.
# ============================================================


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