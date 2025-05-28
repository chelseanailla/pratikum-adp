
def menu():
    print("Menu:")
    print("1. Tabel perkalian modulo n")
    print("2. Mencari nilai Σ x")
    print("3. Mencari nilai n!")
    print('4. Total dan rata rata data')
    print("5. Keluar")
    print()

def modulo():
    print('Tabel perkalian modulo n')
    while True:
        n = int(input("Masukkan nilai n dengan 0 < n ≤ 10 : "))
        if 0 < n <= 10:
            break
        else: 
            n = int(input("Ulangi, n harus antara 0 - 10: "))
            
    for i in range(n):
        print(f"{i:3}", end="")
    print("\n" + "-" * (n * 3 + 4))
    for i in range(n):
        print(f"{i:2} |", end="")
        for j in range(n):
            print(f"{(i*j)%n:3}", end="")
        print()

def sigma_x():
    print('Mencari nilai Σx ')
    bawah = int(input("Batas bawah: "))
    atas = int(input("Batas atas: "))
    while True:
        if atas >= bawah:
            break

        if atas < bawah:
            print("Batas atas harus lebih besar atau sama dengan batas bawah.")
        
    total = 0
    for i in range(bawah, atas+1):
        total += i
    print("Σx =", total)

def faktorial():
    print('Faktorial')
    n = int(input("Masukkan nilai n: "))
    while True:
        if n>=0:
            break
        else:
            n = int(input("Ulangi, n harus ≥ 0: "))

    hasil = 1
    for i in range(2, n+1):
        hasil *= i
    print(f"{n}! =", hasil)

def total_ratarata():
    print(f'Mencari nilai rata-rata')
    while True:
        jumlah = int(input("Masukkan banyak data : "))
        if jumlah > 0:
            break
        else:
            print("Jumlah data harus lebih dari 0.")
        
    data = []
    for i in range(jumlah):
        while True:
            nilai = float(input(f"Data ke-{i+1}: "))
            data.append(nilai)
            break

    total = 0
    for nilai in data:
        total += nilai
    rata = total / jumlah
    print("Total =", total)
    print("Rata-rata =", rata)

def main():
    while True:
        menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            modulo()
        elif pilihan == '2':
            sigma_x()
        elif pilihan == '3':
            faktorial()
        elif pilihan == '4':
            total_ratarata()
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            print()
            break

        else:
            print("Pilihan tidak valid. Ulangi.")
            break
        print()


main()
