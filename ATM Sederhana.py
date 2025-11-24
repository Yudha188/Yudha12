print("==== Selamat Datang di ATM IndoApril")

saldo = 2000000
pin = 123456
input_pin = int(input("Masukan PIN Anda : "))
if(input_pin == pin):
    while True:
        print("Menu")
        print("1. Cek Saldo")
        print("2. Setor Tunai")
        print("3. Tarik Tunai")
        print("4. Keluar")
        pilihan = int(input("Silahkan Pilih Transaksi: "))

        if pilihan == 1:
             print(f"Rp {saldo:,}")
        elif pilihan == 2:
            setor = int(input("Jumlah Setor: "))
            if setor > 0:
                saldo += setor
                print(f"Transaksi Berhasil. Saldo Anda {saldo:,}")
        elif pilihan == 3:
            tarik = int(input("Jumlah Tarik: "))
            if tarik > 0:
                saldo -= tarik
                print(f"Transaksi Berhasil. Saldo Anda {saldo:,}")
        elif pilihan == 4:
            print("Terima Kasih telah bertransaksi")
            break
else:
    print("PIN Anda Salah!")
