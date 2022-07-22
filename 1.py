mas = []
file = open('nomera.txt')
for i in file:
    st = int(i)
    mas.append(st)
count = 0
minr = 100000000000
for i in range(len(mas) - 1):
    if mas[i] % 100 == mas[i+1] % 100:
        count += 1
        minr = min(minr, abs(mas[i]-mas[i+1]))
print(count, minr)
    
