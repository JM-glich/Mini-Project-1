# Program jasa layanan produksi musik untuk user atau pembeli

# Nama: Jemis Movid
# NIM : 2409116070

# Bagian ini buat persiapan mau bikin akun usernya nanti
sigh_up = 0

# variable ini untuk di menu admin nantinya
transaksi = []
saldo = 0 
# Ini kata sandinya
sandi = "admin123"

# Nah, ini program untuk menu adminnya
def admin_menu():
        while True:
            print("-" * 64)
            menu = input("""\nMenu Admin:
1) Lihat seluruh transaksi (Gacor kang)
2) Tambah produk baru
3) Hapus produk :(
4) Keluar
Pilihan Anda: 
""")
            if menu == "1":
                print("\nRiwayat Transaksi: Rp. ")
                for trx in transaksi:
                    print(trx)
            elif menu == "2":
                print("\nTambah produk... (fitur ini masih dalam pengembangan)")
            elif menu == "3":
                print("\nHapus produk... (fitur ini masih dalam pengembangan)")
            elif menu == "4":
                print("\nAnda keluar dari menu admin.")
                break
            else:
                print("Pilihan tidak valid.")

# Bagian ini untuk verifikasi kata sandi admin
def admin_login():
        password = input("Masukkan kata sandi admin:  ")
        if password == sandi:
            print("\nLogin admin berhasil!")
            admin_menu()
        else:
            print("\nKata sandi salah. Akses ditolak. Kamu hacker ya? ")

# Kata-kata sambutan
print("-"*64)
print("Halo para kreator musik! Selamat datang di Jasa layanan produksi musik")

# Menu Sigh up dan login sederhana dengan mengunakan looping
while True:
    print("-"*64)
    print("\nPilih menu yang diinginkan.")
    A = input("""1) Sigh Up
2) Login
3) Admin
4) keluar
Pilihanmu:
""")
    print("-"*64)
    if A == "1":
        email1 = input("silahkan masukan akun email anda: ")
        password1 = input("Silahkan masukan password anda: ")
        print("\nAnda telah membuat akun, silahkan lakukan login ulang.")
        sigh_up += 1

# Menu untuk verifikasi akun dan atau jika user ingin login
    if A == "2":

# Dari baris . . .adalah commend jika usernya belum punya akun
        if sigh_up == 0:
            print("Anda belum memiliki akun. Silahkan untuk membuatnya terlebih dahulu.")
            break

# Nah, kalau sudah punya akun maka akan lanjut ke menu login dan jika berhasil maka akan lanjut ke menu selanjutnya
        else:
            email2 = input("\nSilahkan login ke akun anda: ")
            password2 = input("Silahkan masukan password anda: ")
            if email1 == email2 and password1 == password2:
                print("\nAnda telah berhasil login!")
                print("-"*64)

# Menu bagian produk yang ditawarkan dengan menggunakan commend loop supaya lebih mudah digunakan oleh user. Selain itu juga ada operasi perhitungan jika uang yang dibayarkan kelebihan
                while True:
                    B = input("""\nSilahkan pilih jasa:
1) Produksi musik dan lagu \t Rp. 1,400,000
2) Pembuatan lirik original \t Rp. 200,000
3) Aransemen lagu       \t Rp. 500,000
4) Mixing dan mastering \t Rp. 800,000
5) Kembali
Pilihan anda:

""")
                    

# Ini bagian produk 1
                    if B == "1":
                        print("-"*64)
                        print("""produksi musik dan lagu.
Yang didapat:
1) Full produksi

Yang disiapkan customer:
1) Gambaran mengenai lirik
2) Referensi musik
3) Informasi genre
4) Apakah ingin menggunakan vokal sendiri atau tidak""")
                        harga = 1400000
                        #1 bagian ini untuk memastikan apakah customer memang ingin membeli jasanya atau tidak
                        k = input("""\nIngin lanjut atau kembali? Ya = lanjut, Tidak = kembali: 
""") 
                        if k == "Tidak":
                            break
                        print("-"*64)
                        beli = int(input("\nMasukan jumlah harga: Rp. "))
                        if beli < harga:
                            print("Jumlah uang anda tidak cukup")
                            break
                        else:
                            #2 kalau yang ini untuk menghitung kembalian jika uang yang dibayar customer kelebihan
                            ansulan = beli - harga
                            transaksi.append(f"Dibayar: Rp. {beli} | Kembalian: Rp. {ansulan}")
                            print(f"Terima kasih telah menggunakan jasa kami! Kembalian Anda: Rp. {ansulan}")
                        print("-"*64)

# Ini bagian produk 2
                    elif B == "2":
                        print("-"*64)
                        print("""Pembuatan lirik original
Yang didapat:
1) Lirik original
2) Irama lirik

Yang disiapkan customer:
1) Gambaran mengenai lirik
2) Irama atau nada dari lirik""")
                        harga = 200000
                        k = input("""\nIngin lanjut atau kembali? Ya = lanjut, Tidak = kembali: 
""")
                        if k == "Tidak":
                            break
                        print("-"*64)
                        beli = int(input("\nMasukan jumlah harga: Rp. "))
                        if beli < harga:
                            print("Jumlah uang anda tidak cukup")
                            break
                        else:
                            ansulan = beli - harga
                            transaksi.append(f"Dibayar: Rp. {beli} | Kembalian: Rp. {ansulan}")
                            print(f"Terima kasih telah menggunakan jasa kami! Kembalian Anda: Rp. {ansulan}")
                        print("-"*64)

# Ini bagian produk 3
                    elif B == "3":
                        print("-"*64)
                        print("""Aransemen Lagu
Yang didapat:
1) Full Aransemen

Yang disiapkan customer:
1) Rekaman kotor lagu yang akan diproses
2) Sampaikan mengenai genre dan referensi
3) Berikan catatan mengenai Aransemennya, seperti "Saya ingin dinamikanya lebih bervariasi""")
                        harga = 500000
                        k = input("""\nIngin lanjut atau kembali? Ya = lanjut, Tidak = kembali: 
""")
                        if k == "Tidak":
                            break
                        print("-"*64)
                        beli = int(input("\nMasukan jumlah harga: Rp. "))
                        if beli < harga:
                            print("Jumlah uang anda tidak cukup")
                            break
                        else:
                            ansulan = beli - harga
                            transaksi.append(f"Dibayar: Rp. {beli} | Kembalian: Rp. {ansulan}")
                            print(f"Terima kasih telah menggunakan jasa kami! kembalian anda adalah: Rp. {ansulan}")
                        print("-"*64)

# Ini bagian produk 4
                    elif B == "4":
                        print("-"*64)
                        print("""Mixing dan Mastering
Yang didapat:
1) Mixing balancing
2) Mastering

Yang disiapkan customer:
1) Infokan jumlah track data
2) Hasil render masing-masing track
3) Infokan tempo/BPM""")
                        harga = 800000
                        k = input("""\nIngin lanjut atau kembali? Ya = lanjut, Tidak = kembali: 
""")
                        if k == "Tidak":
                            break
                        print("-"*64)
                        beli = int(input("\nMasukan jumlah harga: Rp. "))
                        if beli < harga:
                            print("Jumlah uang anda tidak cukup")
                            break
                        else:
                            ansulan = beli - harga
                            transaksi.append(f"Dibayar: Rp. {beli} | Kembalian: Rp. {ansulan}")
                            print(f"Terima kasih telah menggunakan jasa kami! kembalian anda adalah: Rp. {ansulan}")
                        print("-"*64)

# Jika user ingin kembali ke menu sebelumnya
                    elif B == "5":
                            break

# Disini adalah berbagai command jika ada kesalahan nantinya
                    else:
                        print("\nPilihan anda tidak valid")
            else:
                print("\nData anda tidak sesuai, silahkan login ulang")

# Program untuk memanggil atau login ke menu adminnya
    elif A == "3":
        admin_login()

# Jika user ingin keluar dari program
    elif A == "4":
        print("Terima kasih telah mengunjungi kami! Sampai jumpa!")
        break