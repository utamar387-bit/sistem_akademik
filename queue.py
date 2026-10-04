# ============================================================
# QUEUE
# ============================================================
# File ini digunakan untuk membuat Queue.
#
# Queue digunakan untuk antrean mahasiswa.
#
# Prinsip:
# FIFO = First In First Out
#
# Mahasiswa yang masuk pertama akan diproses pertama.
# ============================================================


# Mengambil Node dari file linked_list.py
from linked_list import Node


class Queue:
	"""Queue berbasis node untuk melayani mahasiswa dengan prinsip FIFO."""


	def __init__(self):
		
		# Mahasiswa paling depan
		self.depan = None
		
		# Mahasiswa paling belakang
		self.belakang = None


	def enqueue(self, nilai):
		
		# ENQUEUE = menambahkan data ke belakang antrean.
		simpul_baru = Node(nilai)
		
		# Jika antrean masih kosong
		if self.belakang is None:
			# Node baru menjadi depan dan belakang
			self.depan = simpul_baru
			self.belakang = simpul_baru
		
        # Jika antrean tidak kosong, tambahkan simpul baru di belakang	
		else:
			# Node belakang menunjuk ke Node baru
			self.belakang.next = simpul_baru
			
			# Node baru menjadi belakang
			self.belakang = simpul_baru


    # DEQUEUE = mengambil data dari depan antrean.
	def dequeue(self):
		
		# Jika antrean kosong, kembalikan None
		if self.depan is None:
			return None
		
		# Simpan data paling depan
		nilai = self.depan.data
		
		# Geser depan ke Node berikutnya
		self.depan = self.depan.next
		
		# Jika antrean menjadi kosong
		if self.depan is None:
			
			# Set belakang menjadi None juga
			self.belakang = None
		
		# Kembalikan data yang diambil dari depan antrean
		return nilai
	


    # FRONT = melihat data paling depan antrean tanpa menghapusnya.
	def front(self):
		
		# Jika antrean kosong, kembalikan None
		if self.depan is None:
			return None

        # Jika antrean tidak kosong, kembalikan data paling depan
		return self.depan.data


    # TAMPILKAN = menampilkan semua data dalam antrean.
	def tampilkan(self):
		
        # Buat daftar untuk menyimpan data antrean
		daftar_antrean = []
		
        # Mulai dari simpul paling depan
		simpul_sekarang = self.depan
		
        # Telusuri semua simpul dalam antrean hingga akhir
		while simpul_sekarang is not None:
			
            # Tambahkan data simpul saat ini ke daftar antrean
			daftar_antrean.append(simpul_sekarang.data)
			
            # Pindah ke simpul berikutnya
			simpul_sekarang = simpul_sekarang.next
            
        # Kembalikan daftar antrean
		return daftar_antrean

