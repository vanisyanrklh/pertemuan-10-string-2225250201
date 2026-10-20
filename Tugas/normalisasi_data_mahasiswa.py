def normalisasi_nama(nama):
    # Hilangkan spasi berlebih dan ubah ke format judul
    return nama.strip().title()

def buat_inisial(nama):
    # Ambil huruf pertama dari setiap kata
    kata = nama.strip().title().split()
    inisial = "".join([k[0] for k in kata])
    return inisial

def normalisasi_kode(kode):
    # Hilangkan spasi berlebih dan ubah ke huruf besar
    return kode.strip().upper()

# Program utama
nama = input("Nama: ")
kode = input("Kode kelas: ")

print("Nama Normalisasi :", normalisasi_nama(nama))
print("Inisial          :", buat_inisial(nama))
print("Kode Normalisasi :", normalisasi_kode(kode))
