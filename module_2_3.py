my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
len_my_list = len(my_list)
cycle_ = 0
while cycle_ <= len_my_list - 1:
    num = my_list[cycle_]
    cycle_ = cycle_ + 1
    if num > 0:
        print(num)
    elif num == 0:
        continue
    else:
        break
