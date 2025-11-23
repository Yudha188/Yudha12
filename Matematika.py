#Logika matematika 

print("Rumus Matematika!")

def hitung_kecepatan():
    print("Hitung kecepatan ready!")
    jarak = int(input("Masukan nilai jarak : "))
    waktu = int(input("Masukan nilai waktu : "))
    kecepatan = jarak / waktu
    print("kecepatan: ", kecepatan, "\n")

def luas_segitiga():
    print("Hitung luas segitiga ready!")
    alas = int(input("Masukan nilai alas : "))
    tinggi = int(input("Masukan nilai tinggi : "))
    luas = 0.5 * (alas * tinggi)
    print("rumus luas segitiga adalah: ", luas,"\n")

def  luas_balok():
    print("Hitung luas balok ready!")
    panjang = int(input("Masukan nilai panjang : "))
    lebar = int(input("Masukan nilai lebar : "))
    tinggi = int(input("Masukan nilai tinggi : "))
    balok = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
    print("rumus luas nilai balok adalah: ", balok, "\n")

def  luas_bola():
    print("Hitung luas bola ready!")
    r = int(input("Masukan nilai jari-jari : "))
    bola = 4 * 3.14 * (r**2) 
    print("rumus luas bola adalah : ", bola, "\n")   


while True:
    userinput = int(input("Rumus yang akan dipakai: \n\n 1.Hitung kecepatan\n 2.Luas Segitiga\n 3.Luas Balok\n 4.luas Bola\n\n 5.Keluar program\n\n Pilih nomor berapa: "))
    if(userinput == 1):
        print(hitung_kecepatan())
    elif(userinput == 2):
        print(luas_segitiga())
    elif(userinput == 3):
        print(luas_balok())
    elif(userinput == 4):
        print(luas_bola())
    else :
        break


