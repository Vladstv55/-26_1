with open('Задание1.txt') as f:
    mas = [] 
    n = int(f.readline())

for s in f:
    mas.append(int(s)) 
chet = 0
nechet = 0

for i in range(n):
    if mas[i] % 2 == 0 and mas[i] != 0:
        chet += 1 
    else: 
        if mas[i] != 0: 
            nechet += 1

if chet > nechet:
    print('к') 
    print(chet / n) 
else: 
    print('ч') 
    print(chet / n)