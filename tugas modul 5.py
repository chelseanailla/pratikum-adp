nilai_x = list(range (-7,8))
f=[]
n = len(nilai_x)

for i in nilai_x :
    if i>0:
       f.append(i**3-i)
    elif i<0:
       f.append(1/i**2)
    elif i==0:
        f.append(1)

print(f'|  x  |    f(x)     |')
print(f'|-----|-------------|')

for x in range(0,n):              
    print(f'| {nilai_x[x]:>3} | {f[x]:>11.5f} |')
   