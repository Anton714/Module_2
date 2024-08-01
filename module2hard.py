import random
def lottery():
    numbers_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    win1 = random.choice(numbers_)
    return win1

cycle_ = 0
while cycle_ < 1:
    print('Введите число из представленного ряда:  ')
    print('3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20')
    print(' или 0 для выбора случайного числа.')
    in_num = int(input('Ваше число: '))
    numbers_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    if in_num == 0:
        num_ = int(lottery())
        print('Выпало число: ', num_)
        cycle_ += 1
    elif in_num not in numbers_:
        print('Вы ошиблись, начните заново')
    else:
        num_ = in_num
        cycle_ += 1
password = []
num_1 = []
num_1.append(num_)
for i in num_1:

    num_ = i
    for i in range(num_):
        if i == 0:
            continue

        for j in range(num_):
            if j == 0 or i == j:
                continue
            if num_ % (i + j) == 0:
                password.append([i, j])

    u = len(password)
    i = 0
    while i < (u):

        a, b = password[i]
        j = i + 1
        while j < u:

            if i == j:
                print()
            else:

                c, d = password[j]

            if a == d and b == c:
                password.remove([c, d])
                u -= 1
            else:
                j += 1

        i += 1

print ('Ваш пароль :', *password)
