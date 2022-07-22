f = open('2.txt')
mas = []
for i in f:
    s = int(i)
    mas.append(s)
k = 0
maxx = 0
for i in range(len(mas)-1):
    if mas[i] % 16 == 0 and mas[i] % 24 == 0:
        if mas[i+1] % 18 == 0 and mas[i+1] % 24 == 0 and mas[i+1] % 10 == 8:
            count += 1
            maxs = max(maxs, mas[i] + mas[i+1])
print(count, maxs)

