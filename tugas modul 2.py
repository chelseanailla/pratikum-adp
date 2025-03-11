print ('PESANAN MAKAN ONLINE')
print ('DAFTAR MENU :')
print ('Ayam = Rp20.000')
print ('Sapi = Rp35.000')
print ('Cumi-cumi = Rp45.000')
input("Atas nama :")
makanan = str(input('Masukkan pesanan anda: ')).lower()
if makanan == 'ayam':
    harga = 20000
elif makanan == 'sapi':
    harga = 35000
else :
    harga = 45000

jarak = float(input('Masukkan jarak dari rumah ke restoran :'))
if jarak<1:
    ongkir = 0
elif 1<=jarak<=3:
    ongkir = 7000
else:
    ongkir = 15000

biaya_total = harga + ongkir
print(f'Jadi total biaya pesanan anda adalah {biaya_total} ')
