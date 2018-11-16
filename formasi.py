# Siku Siku
for i in range(10):
     for j in range(i+1):
        print('*', end='')
     print()

#siku siku terbalik
for i in reversed(range(10)):
    for j in range(i+1):
        print('*', end='')
    print()

#sama kaki
for i in range(10):
    print(('*'*(1+2*i)).center(1+2*10))

# hanya border
bantu=0
kosong=0
for i in reversed(range(10)):
    for j in range(i+1):
        print(' ', end='')
    for k in range(bantu+1):
        if k==0:
            print('*', end='')
        else:
            print(' ', end='')
    for l in range(bantu):
        if l==kosong:
            print('*', end='')
            kosong+=1
        else:
            print(' ', end='')
    bantu+=1
    print()
for i in range(11):
    print('* ', end='')
