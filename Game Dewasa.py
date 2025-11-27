#Mencoba Permainan Logika
print("Selamat Datang di Game Dewasa!")

bermain = input("Mulai Permainan? ")

if bermain == "Tidak".lower():
    quit
print("Ayo Mulai!")
nilai = 0

jawaban = input("Apa profesi seorang Mia Khalifa? ")
if jawaban == "Bintang Porno".lower():
    print("Kamu Benar")
    nilai += 1
else :
    print("Salah")

jawaban = input("Apa kepanjangan dari MILF? ")
if jawaban == "Mom I'd Like to Fuck".lower():
    print("Kamu Benar")
    nilai += 1
else:
    print("Salah")

jawaban == input(
    "Siapa artif MILF yang paling populer di dunia? ")
if jawaban == "Lisa Ann".lower():
    print("Kamu Benar")
    nilai += 1
else:
    print("Salah")

jawaban == input("Apa posisi dalam sex yang menyerupai anjing? ")
if jawaban == "Doggy Style".lower():
    print("Kamu Benar")
    nilai += 1
else:
    print("Salah")

print(f"Selamat, Kamu mendapatkan {nilai} poin ")