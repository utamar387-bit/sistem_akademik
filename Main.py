"""Program Pengelolaan Data Mahasiswa Sistem Akademik."""

# ============================================================
# PROGRAM UTAMA
# ============================================================
# File ini berisi:
# 1. Menu
# 2. Input pengguna
# 3. Menjalankan fitur sistem akademik
# ============================================================


# Mengambil class SistemAkademik
from sistem_akademik import SistemAkademik

def tampilkan_mahasiswa(mahasiswa):
	print("NIM: {} | Nama: {} | Prodi: {}".format(
		mahasiswa["nim"], mahasiswa["nama"], mahasiswa["prodi"]
	))


def tampilkan_menu():
	print("\n========================================")
	print("       SISTEM AKADEMIK MAHASISWA")
	print("========================================")
	print("1. Tambah Data Mahasiswa")
	print("2. Lihat Data Mahasiswa")
	print("3. Cari Mahasiswa Berdasarkan NIM")
	print("4. Hapus Data Mahasiswa")
	print("5. Undo Perubahan")
	print("6. Tambah Mahasiswa ke Antrean")
	print("7. Proses Antrean")
	print("8. Keluar")
	print("========================================")


def jalankan_program():
	sistem = SistemAkademik()
	print("Data contoh Andi, Budi, dan Citra sudah tersedia.")

	while True:
		tampilkan_menu()
		try:
			pilihan = input("Pilih menu: ").strip()
		except EOFError:
			print("\nProgram selesai.")
			break

		if pilihan == "1":
			nim = input("Masukkan NIM: ").strip()
			nama = input("Masukkan nama: ").strip()
			prodi = input("Masukkan program studi: ").strip()
			if not nim or not nama or not prodi:
				print("Semua kolom wajib diisi.")
			elif sistem.tambah_mahasiswa(nim, nama, prodi):
				print("Data mahasiswa berhasil ditambahkan.")
			else:
				print("NIM sudah terdaftar. Gunakan NIM yang berbeda.")

		elif pilihan == "2":
			print("\nData mahasiswa (List):")
			if not sistem.data_mahasiswa:
				print("Belum ada data mahasiswa.")
			else:
				for nomor, mahasiswa in enumerate(sistem.data_mahasiswa, start=1):
					print("{}. ".format(nomor), end="")
					tampilkan_mahasiswa(mahasiswa)
			urutan_nim = [m["nim"] for m in sistem.linked_list.tampilkan()]
			print("Urutan NIM pada Linked List: {}".format(
				" -> ".join(urutan_nim) if urutan_nim else "(kosong)"
			))

		elif pilihan == "3":
			nim = input("Masukkan NIM yang dicari: ").strip()
			mahasiswa = sistem.indeks_nim.get(nim)
			if mahasiswa is None:
				print("Mahasiswa dengan NIM tersebut tidak ditemukan.")
			else:
				print("Mahasiswa ditemukan:")
				tampilkan_mahasiswa(mahasiswa)

		elif pilihan == "4":
			nim = input("Masukkan NIM yang akan dihapus: ").strip()
			mahasiswa = sistem.hapus_mahasiswa(nim)
			if mahasiswa is None:
				print("Mahasiswa dengan NIM tersebut tidak ditemukan.")
			else:
				print("Data berikut berhasil dihapus:")
				tampilkan_mahasiswa(mahasiswa)

		elif pilihan == "5":
			hasil_undo = sistem.undo()
			if hasil_undo is None:
				print("Belum ada perubahan data yang dapat di-Undo.")
			else:
				print(hasil_undo + ".")

		elif pilihan == "6":
			nim = input("Masukkan NIM yang akan masuk antrean: ").strip()
			mahasiswa = sistem.indeks_nim.get(nim)
			if mahasiswa is None:
				print("NIM belum terdaftar; mahasiswa tidak dimasukkan ke antrean.")
			else:
				sistem.antrean.enqueue(nim)
				print("{} berhasil ditambahkan ke antrean.".format(mahasiswa["nama"]))
				print("Antrean NIM: {}".format(" -> ".join(sistem.antrean.tampilkan())))

		elif pilihan == "7":
			nim = sistem.antrean.dequeue()
			if nim is None:
				print("Antrean masih kosong.")
			else:
				mahasiswa = sistem.indeks_nim.get(nim)
				if mahasiswa is None:
					print("Antrean diproses untuk NIM {}, tetapi datanya sudah dihapus.".format(nim))
				else:
					print("Memproses mahasiswa paling depan:")
					tampilkan_mahasiswa(mahasiswa)

		elif pilihan == "8":
			print("Terima kasih. Program selesai.")
			break

		else:
			print("Pilihan tidak valid. Masukkan angka 1 sampai 8.")


if __name__ == "__main__":
	jalankan_program()
