file = open('2.txt')
mas = []
for i in file:
    st = int(i)
    mas.append(st)
count = 0
maxs = 0
for i in range(len(mas)-1):
    if mas[i] % 16 == 0 and mas[i] % 24 == 0:
        if mas[i+1] % 18 == 0 and mas[i+1] % 24 == 0 and mas[i+1] % 10 == 8:
            count += 1
            maxs = max(maxs, mas[i] + mas[i+1])
print(count, maxs)

