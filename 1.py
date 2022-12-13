from random import randint
n = int(input('Ввод длины списка \n'))
a = []
for i in range(n):
    a.append(randint(0, 1))
#a = [0, 0, 0, 1, 1, 1]
count_i = 0
a = list(map(str, a))
b = ''.join(a)
for i in range(1, n+1):
    zero_possib_B, one_possib_B = 0, 0
    if ('0' * i) in b or ('1' * i) in b:
        count_i = n - i + 1
        k0 = 0
        k1 = 0
        for j in range(0, n):
            if b[j:j+i] == '0'*i:
                k0 += 1
            if b[j:j+i] == '1'*i:
                k1 += 1
        zero_possib_B = k0/count_i
        one_possib_B = k1/count_i
        print(f"Вероятность {'0' * i} = {zero_possib_B}")
        print(f"Вероятность {'1' * i} = {one_possib_B}")
