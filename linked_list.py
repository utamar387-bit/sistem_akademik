# ============================================================
# LINKED LIST
# ============================================================
# File ini berisi:
# 1. Node
# 2. LinkedList
#
# Linked List digunakan untuk menyimpan data mahasiswa
# secara dinamis.
# ============================================================


class Node:
	"""Simpul untuk Linked List dan Queue."""

    # Inisialisasi simpul dengan data dan pointer ke simpul berikutnya.
	def __init__(self, data):
		
		# Data yang disimpan dalam simpul
		self.data = data
		
		# Pointer ke simpul berikutnya (default None)
		self.next = None


class LinkedList:
	"""Linked List sederhana untuk menyimpan urutan mahasiswa."""

    # Inisialisasi Linked List dengan head dan tail.
	def __init__(self):

        # Head adalah simpul pertama dalam Linked List
		self.head = None

        # Tail adalah simpul terakhir dalam Linked List
		self.tail = None


	def tambah(self, data):
		"""Menambahkan data di akhir Linked List dalam O(1)."""

        # Membuat simpul baru dengan data yang diberikan
		simpul_baru = Node(data)

        # Jika Linked List kosong, head dan tail menunjuk ke simpul baru
		if self.head is None:

            # Head menunjuk ke simpul baru karena ini adalah simpul pertama
			self.head = simpul_baru

            # Tail juga menunjuk ke simpul baru karena ini adalah satu-satunya simpul
			self.tail = simpul_baru

        # Jika Linked List tidak kosong, tambahkan simpul baru di akhir
		else:

            # Tail menunjuk ke simpul baru karena ini adalah simpul terakhir
			self.tail.next = simpul_baru

            # Tail diperbarui untuk menunjuk ke simpul baru karena ini sekarang adalah simpul terakhir
			self.tail = simpul_baru


	def sisipkan(self, indeks, data):
		"""Menyisipkan data pada indeks tertentu, misalnya saat Undo."""

        # Membuat simpul baru dengan data yang diberikan
		simpul_baru = Node(data)

        # Jika indeks <= 0 atau Linked List kosong, sisipkan di awal
		if indeks <= 0 or self.head is None:

            # Jika Linked List kosong, head dan tail menunjuk ke simpul baru
			simpul_baru.next = self.head
			self.head = simpul_baru

            # Jika Linked List kosong, tail juga menunjuk ke simpul baru
			if self.tail is None:
				self.tail = simpul_baru
				
            # Jika indeks > 0, sisipkan di posisi yang sesuai
			return

		simpul_sebelumnya = self.head
		posisi = 0
		while posisi < indeks - 1 and simpul_sebelumnya.next is not None:
			simpul_sebelumnya = simpul_sebelumnya.next
			posisi += 1

		simpul_baru.next = simpul_sebelumnya.next
		simpul_sebelumnya.next = simpul_baru
		if simpul_baru.next is None:
			self.tail = simpul_baru

	def hapus(self, nim):
		"""Menghapus mahasiswa berdasarkan NIM; mengembalikan data atau None."""
		simpul_sekarang = self.head
		simpul_sebelumnya = None

		while simpul_sekarang is not None:
			if simpul_sekarang.data["nim"] == nim:
				if simpul_sebelumnya is None:
					self.head = simpul_sekarang.next
				else:
					simpul_sebelumnya.next = simpul_sekarang.next

				if simpul_sekarang is self.tail:
					self.tail = simpul_sebelumnya
				return simpul_sekarang.data

			simpul_sebelumnya = simpul_sekarang
			simpul_sekarang = simpul_sekarang.next
		return None

	def tampilkan(self):
		"""Menghasilkan data dengan menelusuri node dari head ke tail."""
		data_mahasiswa = []
		simpul_sekarang = self.head
		while simpul_sekarang is not None:
			data_mahasiswa.append(simpul_sekarang.data)
			simpul_sekarang = simpul_sekarang.next
		return data_mahasiswa