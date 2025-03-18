print('===KALKULATOR SEDERHANA===')

while True :
    angka1 = float(input('Masukkan angka pertama: '))
    angka2= float(input('Masukkan angka kedua: '))

    print('      --PILIH OPERASI--      ')
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Perkalian')
    print('4. Pembagian')
    print('5. Keluar')

    operasi = (input('Masukkan operasi yang diinginkan : '))

    if operasi == '5':
        print('Keluar dari kalkulator')
        break

     

    if operasi == '1':
        hasil = angka1 + angka2
        print(f'Hasilnya adalah : {hasil}')

    elif operasi == '2':
        hasil = angka1 - angka2
        print(f'Hasilnya adalah: {hasil}')


    elif operasi == '3':
        hasil = angka1*angka2
        print(f'Hasilnya adalah: {hasil}')

    elif operasi == '4':
        if angka2 == 0:
            print(f'error')
        else:
            hasil = angka1/angka2
            print(f'Hasilnya adalah: {hasil}')



    else:
        print('Pilihan operasi tidak sesuai, silahkan ulangi kembali.')
        break
    
    #ulang = input(' Ulangi? Yes/No : ').lower()
    #if ulang != 'yes':
     #   print('Selesai.')
    #break