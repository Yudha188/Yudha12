# Nilai akhir mahasiswa

nama = input("Masukan Nama Mahasiwa: ")
nim = int(input("Masukan Nim Mahasiswa: "))

nilai_tugas = float(input("Masukan Nilai Tugas\t: "))
nilai_uts= float(input("Masukan Nilai UTS\t: "))
nilai_uas = float(input("Masukan Nilai UAS\t: "))

nilai_akhir = (nilai_tugas * 0.20) + (nilai_uts * 0.40) + (nilai_uas * 0.40)

print(f"\nNama Mahasiswa\t: {nama}")
print(f"Nilai Akhir\t: {nilai_akhir:.2f}")

if nilai_akhir >= 85:
    print("Nilai= A")
elif nilai_akhir >= 75:
    print("Nilai= B")
elif nilai_akhir >= 65:
    print("Nilai = C")
elif nilai_akhir >=55:
    print("Nilai = D")
else:
    print("Nilai= E")
