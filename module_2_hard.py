

# В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.
# Во вторую вставку нужно было написать те пары чисел друг за другом,
# чтобы число из первой вставки было кратно(делилось без остатка) сумме их значений.

import random


def window_1():
    list_1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    win = random.choice(list_1)
    return win


win = window_1()
print(f'Число из первой вставки: {win}')
list_2 = []
list_3 = []
is_prime = True
for i in range(1, win):
    if is_prime:
        for j in range(i, win):
            if i > j:
                is_prime = False
                break
            elif win % (i + j) == 0 and j != i:
                list_2.append(i)
                list_2.append(j)
                list_3.append([i, j])
    else:
        break
print('Пароль по заданию:', list_2)
print('Пароль для удобства восприятия:', list_3)
