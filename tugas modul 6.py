kasus = []
konstanta = []

while True:
    print("==Penyelesai Sistem Persamaan Linier==")
    n = int(input("masukkan jumlah persamaan (2/3) : "))
    m = int(input("masukkan jumlah variabel (1/2/3) : "))
    if n not in [2, 3] or m not in [1,2, 3]:
        print("input tidak valid, hanya terdapat 2 atau 3")
        continue

    A = []
    B = []

    for j in range(n):
        row = []
        for k in range(m):
            row.append(float(input(f"koefisien x{k+1} di persamaan {j+1} : ")))
        A.append(row)
        B.append(float(input(f"konstanta di persamaan {j+1} : ")))
    
    kasus.append(A)
    konstanta.append(B)



    print("==hasil==")
    for l in range(len(kasus)):
        A = kasus[l]
        B = konstanta[l]
        print(f" solusi untuk SPL ke {l+1}: ")

        n = len(A)
        m = len(A[0])

        if n != m:
            if n > m:
                print("SPL tidak ada solusi")
            else:
                print("SPL memiliki tak hingga solusi")
            continue

        if m == 2:
            det_A = A[0][0]*A[1][1] - A[0][1]*A[1][0]
        else:
            det_A = (
                A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1]) -
                A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0]) +
                A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0])
            )

        if det_A == 0:
            print("SPL tidak ada solusi")
            continue

        solusi = []
        for j in range(m):
            baris_baru = []
            for k in range(n):
                baris = A[k][:]
                baris[j] = B[k]
                baris_baru.append(baris)

            if m == 2:
                det_Aj = baris_baru[0][0]*baris_baru[1][1] - baris_baru[0][1]*baris_baru[1][0]
            else:
                det_Aj = (
                    baris_baru[0][0]*(baris_baru[1][1]*baris_baru[2][2] - baris_baru[1][2]*baris_baru[2][1]) -
                    baris_baru[0][1]*(baris_baru[1][0]*baris_baru[2][2] - baris_baru[1][2]*baris_baru[2][0]) +
                    baris_baru[0][2]*(baris_baru[1][0]*baris_baru[2][1] - baris_baru[1][1]*baris_baru[2][0])
                )
            solusi.append(det_Aj / det_A)

        for j in range(m):
            print(f"x{j+1} = {solusi[j]}, solusi tunggal")