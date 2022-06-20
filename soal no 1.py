data = [["42130056", "Yohani Clarita Felcy", "Farmasi"], ["421313246", "Agustini Degni Melsy Grren Kewa Luon", "Teknologi Informasi"],
        ["42130254", "Erwin Arizon Lamanepa", "Akuntansi"]]
x = 0
print("Silahkan Pilih nama mahasiswa berikut : ")
for i in data:
    print(f"{x+1}. {data[x][1]}")
    x = x + 1

user = int(input("Pilihan anda : "))

if user == 1:
    print(data[0])
elif user == 2:
    print(data[1])
elif user == 3:
    print(data[2])
