# nama_siswa = ('buzz', 'andy', 'woody')
# nilai = (12, 13, 14)

# print ("Nama Siswa: ", *nama_siswa)

# nama_siswa = frozenset(['woody', 'buzz', 'andy'])
# nilai = frozenset([12, 13, 14])
# hari = {
#     "sen": "senin",
#     "sel": "selasa",
#     "rab": "rabu"
# }
# nama = input("masukkan nama ")
# print("selamat pagi ", nama)

# nama = "kuncoro"
# # menampikan isi value dari nama terlebih dahulu
# print(nama)
# nama = input("masukkan nama ")
# print("di variabel nama sekarang adalah ", nama)

# cuaca = "cerah"
# if cuaca == "hujan":
#     print("gunakan payung")
# # menggunakan fungsi elif
# elif cuaca == "cerah":
#     print("tidak menggunakan payung")

# b = 5

# while b >= 1:
#     print(b)
#     b -= 1

# c = 1

# while c <= 5:
#     print(c)
#     if c == 3:
#         break
#     c += 1
# d = 0

# while d < 5:
#     d += 1
#     if d == 3:
#         continue
#     print(d)

# nama_maintainer = ("majed", "permen", "kelvin", "hen")
# show = iter(nama_maintainer)
# print(next(show))
# print(next(show))
# print(next(show))
# print(next(show))

# class AngkaSaya:
#   def __iter__(self):
#     self.angka = 1
#     return self

#   def __next__(self):
#     nomor = self.angka
#     self.angka += 1
#     return nomor

# kelas_angka = AngkaSaya()
# test_iter = iter(kelas_angka)

# print(next(test_iter))
# print(next(test_iter))
# print(next(test_iter))

# x = 300

# def myfunc():
#     # ini adalah variabel x yang berbeda dengan yang diatas
#     x = 200
#     print(x)

# myfunc()

# print(x)

# def myfunc():
#     global x
#     x = 300

# myfunc()

# print(x)
# class Merk(object):
#     def __init__(self):
#         self.nama = "calvin klein"

# class Panggil(Merk):
#     def __init__(self):
#         Merk.__init__(self)

#     def tampilkan(self):
#         print(self.nama)

# data = Panggil()
# data.tampilkan()

# try:
#     # karena pembaginya adalah nol, maka tangani error di except
#     hasil = 5 / 0
#     print('Hasil pembagian adalah =', hasil)
# except ZeroDivisionError:
#     # tangani error di sini
#     print('Bilangan tidak dapat dibagi dengan nol')

# Bentuk 1
# try:
#     hasil = 5 / "2"
#     print("Hasil pembagian adalah =", hasil)
# except ZeroDivisionError as err:
#     print(err) # division by zero
# except TypeError as err:
#     print(err) # unsupported operand type(s) for /: 'int' and 'str'

# # Bentuk 2
# try:
#     hasil = 3 / 0
#     print('Hasil pembagian adalah =', hasil)
# except (ZeroDivisionError, TypeError) as err:
#     # cetak pesan error tergantung jenis error yang ditangkap
#     print(err)

# import re

# text = "@robot9 "

# print(re.findall(r"\d", text))
# print(re.findall(r"\w", text))
# print(re.findall(r"\s", text))

# angka = "1234"

# text = "Budi suka makan buah apel"

# print(re.findall(r"\d+", angka))
# print(re.findall(r"\w+", text))

# text = "Poseidon dan Zeus"

# print(re.findall(r"[aiueo]", text))

# text = "Air, api, tanah, udara"

# print(re.findall(r"Air|Water", text))

# type casting adalah metode merubah tipe data dari
# suatu variable atau value yang sudah dideklarasikan
# contoh dibawah ini
# kita bisa melihat dengan menggunakan fungsi "type()"


# merubah ke bilangan koma ke bilangan bulat
# angka = int(30.12)
# print(type(angka))

# # merubah ke bilangan bulat ke bilangan koma
# angka_float = float(20)
# print(type(angka_float))

# # merubah dari bilangan bulat ke string
# angka_string = str(30)
# print(type(angka_string))

# contoh lain (tipe data float)
# float(1)
# float("2")
# float(3.14)


# contoh lain (tipedata string)
# str(1)
# str("2")
# str(3.14)

# def tambah(angka1, angka2):
#     return angka1 + angka2


# def kurang(angka1, angka2):
#     return angka1 - angka2


# def kali(angka1, angka2):
#     return angka1 * angka2


# def bagi(angka1, angka2):
#     return angka1 / angka2
# def salam(waktu="Pagi"):
#     greet = "Selamat " + str(waktu)
#     return greet


# print(salam("Siang")) # Selamat Siang
# print(salam("Malam")) # Selamat Malam
# print(salam("Sore")) # Selamat Sore
# print(salam()) # Selamat Pagi
# class AngkaSaya:
#   def __iter__(self):
#     self.angka = 1
#     return self

#   def __next__(self):
#     nomor = self.angka
#     self.angka += 1
#     return nomor

# kelas_angka = AngkaSaya()
# test_iter = iter(kelas_angka)

# print(next(test_iter))
# print(next(test_iter))
# print(next(test_iter))
# print(next(test_iter))

# mendifinisikan fungsi bernama 'dekorator_huruf_kecil'
# def dekorator_huruf_kecil(kata_besar):
#     # membuat fungsi nested yang kita sebut 'wrapper'
#     def wrapper():
#         # memanggil yang diteruskan dekorator_huruf_kecil
#         # dan kemudian dimasukkan ke dalam variabel
#         # 'kata_message'
#         kata_message = kata_besar()
#         # menggunakan fungsi 'lower()' untuk membuat
#         # variabel dari kata_message menjadi kecil
#         # dan kemudian ditugaskan dalam variabel
#         # buat_kata_kecil
#         buat_kata_kecil = kata_message.lower()
#         # mengembalikan nilai dari 'wrapper'
#         return buat_kata_kecil
#     # mengembalikan fungsi dari wrapper
#     return wrapper

# @dekorator_huruf_kecil
# def kata():
#     return "Deep Dive"
# kata()

# def myfunc():
#     x = 300
#     def myinnerfunc():
#         print(x)
#     myinnerfunc()

# myfunc()

def myfunc():
    global x
    x = 300

myfunc()

print(x)