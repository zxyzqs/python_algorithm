# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 20:43

d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
d0_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]  # 正确排序

while True:
    state = 0
    for i in range(len(d0) - 1):
        if d0[i] > d0[i+1]:
            d0[i], d0[i+1] = d0[i+1], d0[i]
            state = 1
    if not state:
        break

print(d0)
print(d0_out)


