import numpy as np
import matplotlib.pyplot as mat
import random as R
from math import sqrt


a, M, dispersia = [], 0, 0
n = int(input('ввод длины списка\n'))
for i in range(n):
    a.append(R.randint(0, 100))

print(f"Первые 20 элементов {a[:21]}")
dev = False
if dev: # тестовый режим, исользуются готовые данные
    a = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
    n = len(a)
    maxA = 3

for i in range(0, max(a)+1):
    M += i * a.count(i)/len(a)

for i in range(0, max(a)+1):
    dispersia += a.count(i)*(i-M)**2
dispersia /= n
sr_otklon = sqrt(dispersia)
print(f"Мат. ожидание = {M}, дисперсия = {dispersia}, отклонение = {sr_otklon}")

k = R.randint (0,100)
b = R.randint (0,100)
f = np.array([k*i+b for i in range (n)])
y = f+np.random.normal(M, sr_otklon, n)
x = np.array(range (n))
mx = x.sum()/n
my = y.sum()/n
a2 = np.dot(x.T, x)/n
a11 = np.dot(x.T, y)/n
k_teor = (a11 - mx*my)/(a2 - mx**2)
b_teor = (my - k_teor*mx)
f1 = np.array([k_teor*i+b_teor for i in range(n)])


mat.suptitle("Линейная функция методом наименьших квадратов")
mat.plot(f)
mat.plot(f1)
mat.scatter(x, y)
mat.grid()
mat.show()