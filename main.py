def nElements(n):
    seq = ''
    for i in range(1, int(n)+1):
        seq += str(i) * i
    return seq

n = input('Введите число n: ')
print('Последовательность: ' + nElements(n))