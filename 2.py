f = open('2.txt')
mas = []
for i in f:
    s = int(i)
    mas.append(s)
k = 0
maxx = 0
for i in range(len(mas)-1):
    zm = mas[i]
    gr = mas[i+1]
    if zm % 16 == 0 and zm % 24 == 0:
        if gr % 18 == 0 and gr % 24 == 0 and gr % 10 == 8:
            k += 1
            maxx = max(maxx, zm + gr)
print(k, maxx)
