def devyat(n):
    st = ''
    while n > 0:
        c = n % 9
        st = str(c) + st
        n = n // 9
    return st
def summa(n):
    s = 0
    ch = devyat(n)
    for i in ch:
        s += int(i)
    return s
file = open('3.txt')
mas = []
for i in file:
    st = int(i)
    mas.append(st)
count = 0
maxs = 0
for i in range(len(mas)-2):
    if summa(mas[i]) + summa(mas[i+1]) + summa(mas[i+2]) <= 72:
        flag = 0
        if mas[i] % 13 == 0:
            flag += 1
        if mas[i+1] % 13 == 0:
            flag += 1
        if mas[i+2] % 13 == 0:
            flag += 1
        if flag == 1:
            count += 1
            maxs = max(maxs, mas[i] + mas[i+1] + mas[i+2])
print(count, maxs)
