import matplotlib.pyplot as mat
from random import randint
import recovery_and_creation as rec

visa_original, master_original = [], []
with open('Visa_original.txt') as Visa:
    visa_original = Visa.readlines()
    for i in range(len(visa_original)):
        visa_original[i] = visa_original[i].replace(",", ".").replace("\n", "")
    visa_original = list(map(float, visa_original))
with open('Mastercard_original.txt') as Master:
    master_original = Master.readlines()
    for i in range(len(master_original)):
        master_original[i] = master_original[i].replace(",", ".").replace("\n", "")
    master_original = list(map(float, master_original))

print(f'Visa \n {visa_original} \nMasterCard \n {master_original}')
print('~~~~~~~~~~')


visa_prob = rec.create(visa_original)
master_prob = rec.create(master_original)
print(f'Visa \n {visa_prob} \nMasterCard \n {master_prob}')
print('~~~~~~~~~~')
EV_mastercard = 0
EV_visa = 0
for i in range(len(visa_prob)):
    EV_visa += visa_prob[i][0] * visa_prob[i][1]
    EV_mastercard += master_prob[i][0] * master_prob[i][1]
print(f' Математическое ожидание Visa \n {EV_visa} \nМатематическое ожидание Mastercard \n {EV_mastercard}')

q, w, e = 0, 0, 0
for i in range(len(visa_original)):
    q += (visa_original[i] - EV_visa) * (master_original[i] - EV_mastercard)
    w += (visa_original[i] - EV_visa) * (visa_original[i] - EV_visa)
    e += (master_original[i] - EV_mastercard) * (master_original[i] - EV_mastercard)
r = q/((w*e)**0.5)
print(f'Коэффицент корреляции Пирсона = {r}')
print('~~~~~~~~~~')

visa_damaged, master_damaged, visa_linear, visa_recovery, master_linear, master_recovery= [], [], [], [], [], []
for i in range(len(visa_original)):
    visa_damaged.append(visa_original[i])
    master_damaged.append(master_original[i])

for i in range(len(visa_original)):
    ind = randint(0, len(visa_damaged) - 1)
    if visa_damaged[ind] != []:  visa_damaged[ind] = []
    if master_damaged[ind] != []: master_damaged[ind] = []

for i in range(len(visa_original)):
    visa_linear.append(visa_damaged[i])
    visa_recovery.append(visa_damaged[i])
    master_linear.append(master_damaged[i])
    master_recovery.append(master_damaged[i])

print(f'Visa повреждённый\n {visa_damaged} \nMasterCard повреждённый\n {master_damaged}')
print('~~~~~~~~~~')

rec.vinzoring(visa_damaged)
rec.vinzoring(master_damaged)
print('Винзорирование')
print(f'Visa \n {visa_damaged} \nMasterCard \n {master_damaged}')
print('~~~~~~~~~~')

rec.linear_approximation(visa_linear)
rec.linear_approximation(master_linear)
print('Линейная аппроксимация')
print(f'Visa \n {visa_linear} \nMasterCard \n {master_linear}')
print('~~~~~~~~~~')

rec.correlation_recovery(visa_recovery, master_original)
rec.correlation_recovery(master_recovery, visa_original)
print('Корреляционное восстановление')
print(f'Visa \n {visa_recovery} \nMasterCard \n {master_recovery}')
print('~~~~~~~~~~')


fig, a = mat.subplots(2,4)
a[0,0].set_title("Оригинальные данные Visa")
a[0,0].plot(visa_original, c = 'darkorchid')

a[0,1].set_title("Винзорирование")
a[0,1].plot(visa_damaged, c = 'black')
a[0,1].plot(visa_original, c = 'darkorchid')

a[0, 2].set_title("Линейная аппроксимация")
a[0, 2].plot(visa_linear, c='black')
a[0, 2].plot(visa_original, c='darkorchid')

a[0, 3].set_title("Корреляционное восстановление")
a[0, 3].plot(visa_recovery, c='black')
a[0, 3].plot(visa_original, c='darkorchid')

a[1,0].set_title("Оригинальные данные MasterCard")
a[1,0].plot(master_original, c = 'indigo')

a[1,1].set_title("Винзорирование")
a[1,1].plot(master_damaged, c = 'peru')
a[1,1].plot(master_original, c = 'indigo')

a[1,2].set_title("Линейная аппроксимация")
a[1,2].plot(master_linear, c = 'peru')
a[1,2].plot(master_original, c = 'indigo')

a[1, 3].set_title("Корреляционное восстановление")
a[1, 3].plot(master_recovery, c = 'peru')
a[1, 3].plot(master_original, c = 'indigo')
for a in a.flat:
    a.label_outer()
mat.show()

import matplotlib.pyplot as mat
from random import randint
import recovery_and_creation as rec

visa_original, master_original = [], []
with open('Visa_original.txt') as Visa:
    visa_original = Visa.readlines()
    for i in range(len(visa_original)):
        visa_original[i] = visa_original[i].replace(",", ".").replace("\n", "")
    visa_original = list(map(float, visa_original))
with open('Mastercard_original.txt') as Master:
    master_original = Master.readlines()
    for i in range(len(master_original)):
        master_original[i] = master_original[i].replace(",", ".").replace("\n", "")
    master_original = list(map(float, master_original))

print(f'Visa \n {visa_original} \nMasterCard \n {master_original}')
print('~~~~~~~~~~')


visa_prob = rec.create(visa_original)
master_prob = rec.create(master_original)
print(f'Visa \n {visa_prob} \nMasterCard \n {master_prob}')
print('~~~~~~~~~~')
EV_mastercard = 0
EV_visa = 0
for i in range(len(visa_prob)):
    EV_visa += visa_prob[i][0] * visa_prob[i][1]
    EV_mastercard += master_prob[i][0] * master_prob[i][1]
print(f' Математическое ожидание Visa \n {EV_visa} \nМатематическое ожидание Mastercard \n {EV_mastercard}')

q, w, e = 0, 0, 0
for i in range(len(visa_original)):
    q += (visa_original[i] - EV_visa) * (master_original[i] - EV_mastercard)
    w += (visa_original[i] - EV_visa) * (visa_original[i] - EV_visa)
    e += (master_original[i] - EV_mastercard) * (master_original[i] - EV_mastercard)
r = q/((w*e)**0.5)
print(f'Коэффицент корреляции Пирсона = {r}')
print('~~~~~~~~~~')

visa_damaged, master_damaged, visa_linear, visa_recovery, master_linear, master_recovery= [], [], [], [], [], []
for i in range(len(visa_original)):
    visa_damaged.append(visa_original[i])
    master_damaged.append(master_original[i])

for i in range(len(visa_original)):
    ind = randint(0, len(visa_damaged) - 1)
    if visa_damaged[ind] != []:  visa_damaged[ind] = []
    if master_damaged[ind] != []: master_damaged[ind] = []

for i in range(len(visa_original)):
    visa_linear.append(visa_damaged[i])
    visa_recovery.append(visa_damaged[i])
    master_linear.append(master_damaged[i])
    master_recovery.append(master_damaged[i])

print(f'Visa повреждённый\n {visa_damaged} \nMasterCard повреждённый\n {master_damaged}')
print('~~~~~~~~~~')

rec.vinzoring(visa_damaged)
rec.vinzoring(master_damaged)
print('Винзорирование')
print(f'Visa \n {visa_damaged} \nMasterCard \n {master_damaged}')
print('~~~~~~~~~~')

rec.linear_approximation(visa_linear)
rec.linear_approximation(master_linear)
print('Линейная аппроксимация')
print(f'Visa \n {visa_linear} \nMasterCard \n {master_linear}')
print('~~~~~~~~~~')

rec.correlation_recovery(visa_recovery, master_original)
rec.correlation_recovery(master_recovery, visa_original)
print('Корреляционное восстановление')
print(f'Visa \n {visa_recovery} \nMasterCard \n {master_recovery}')
print('~~~~~~~~~~')


fig, a = mat.subplots(2,4)
a[0,0].set_title("Оригинальные данные Visa")
a[0,0].plot(visa_original, c = 'darkorchid')

a[0,1].set_title("Винзорирование")
a[0,1].plot(visa_damaged, c = 'black')
a[0,1].plot(visa_original, c = 'darkorchid')

a[0, 2].set_title("Линейная аппроксимация")
a[0, 2].plot(visa_linear, c='black')
a[0, 2].plot(visa_original, c='darkorchid')

a[0, 3].set_title("Корреляционное восстановление")
a[0, 3].plot(visa_recovery, c='black')
a[0, 3].plot(visa_original, c='darkorchid')

a[1,0].set_title("Оригинальные данные MasterCard")
a[1,0].plot(master_original, c = 'indigo')

a[1,1].set_title("Винзорирование")
a[1,1].plot(master_damaged, c = 'peru')
a[1,1].plot(master_original, c = 'indigo')

a[1,2].set_title("Линейная аппроксимация")
a[1,2].plot(master_linear, c = 'peru')
a[1,2].plot(master_original, c = 'indigo')

a[1, 3].set_title("Корреляционное восстановление")
a[1, 3].plot(master_recovery, c = 'peru')
a[1, 3].plot(master_original, c = 'indigo')
for a in a.flat:
    a.label_outer()
mat.show()