n = int(input('Masukkan nilai n (minimal 4) : '))
#boom = 0
if n<4 :
    print('Nilai n harus minimal 4!')
else :
    boom = 0
    for i in range(n):
        for j in range(n):
            if n%2 == 1 and i == j == n//2:
                 print ('HORE', end='   ')
            elif i==j :
                print(' 1 ',end='   ')
            elif i + j == n-1:
                print(' 2 ', end='   ')
            else :
                print ('BOOM',end='   ')
                boom += 1
        print()
    print(f'Total BOOM yang muncul sebanyak : {boom}')