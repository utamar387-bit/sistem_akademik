
# ============================================================
# SISTEM AKADEMIK
# ============================================================
# File ini menggabungkan:
#
# 1. List
# 2. Linked List
# 3. Dictionary
# 4. Stack
# 5. Queue
# ============================================================


# Mengambil LinkedList dari file linked_list.py
from linked_list import LinkedList

# Mengambil Stack dari file stack.py
from stack import Stack

# Mengambil Queue dari file queue.py
from queue import Queue

class SistemAkademik:
	"""Mengatur data mahasiswa dan menyinkronkan struktur datanya."""
	def __init__(self):
		# List menjadi penyimpanan berurutan; dua struktur lain adalah indeks/mirror.
		self.data_mahasiswa = []
		self.linked_list = LinkedList()
		self.indeks_nim = {}
		self.riwayat_undo = Stack()
		self.antrean = Queue()

		data_contoh = [
			{"nim": "231001", "nama": "Andi", "prodi": "Teknik Informatika"},
			{"nim": "231002", "nama": "Budi", "prodi": "Teknik Informatika"},
			{"nim": "231003", "nama": "Citra", "prodi": "Sistem Informasi"},
		]
		for mahasiswa in data_contoh:
			self._simpan(mahasiswa, len(self.data_mahasiswa))

	def _simpan(self, mahasiswa, indeks):
		"""Menyimpan data pada List, Linked List, dan Dictionary."""
		self.data_mahasiswa.insert(indeks, mahasiswa)
		self.linked_list.sisipkan(indeks, mahasiswa)
		self.indeks_nim[mahasiswa["nim"]] = mahasiswa

	def tambah_mahasiswa(self, nim, nama, prodi):
		if nim in self.indeks_nim:
			return False

		mahasiswa = {"nim": nim, "nama": nama, "prodi": prodi}
		indeks = len(self.data_mahasiswa)
		self._simpan(mahasiswa, indeks)
		self.riwayat_undo.push(("tambah", mahasiswa, indeks))
		return True

	def hapus_mahasiswa(self, nim):
		mahasiswa = self.indeks_nim.get(nim)
		if mahasiswa is None:
			return None

		indeks = self.data_mahasiswa.index(mahasiswa)
		self.data_mahasiswa.pop(indeks)
		self.linked_list.hapus(nim)
		del self.indeks_nim[nim]
		self.riwayat_undo.push(("hapus", mahasiswa, indeks))
		return mahasiswa

	def undo(self):
		aksi = self.riwayat_undo.pop()
		if aksi is None:
			return None

		jenis_aksi, mahasiswa, indeks = aksi
		if jenis_aksi == "tambah":
			self.data_mahasiswa.pop(indeks)
			self.linked_list.hapus(mahasiswa["nim"])
			del self.indeks_nim[mahasiswa["nim"]]
			return "Penambahan mahasiswa {} dibatalkan".format(mahasiswa["nim"])

		self._simpan(mahasiswa, indeks)
		return "Data mahasiswa {} dipulihkan".format(mahasiswa["nim"])