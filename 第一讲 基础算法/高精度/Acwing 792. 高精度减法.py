from typing import List


def comp(num1: List[int], num2: List[int]):
    if len(num1) != len(num2): return len(num1) > len(num2)
    for i in range(len(num1)-1, -1, -1):
        if num1[i] != num2[i]:
            return num1[i] > num2[i]
    return True


def sub(num1: List[int], num2: List[int]):
    res = []
    t = 0
    for i in range(len(num1)):
        t = num1[i] - t
        if i < len(num2): t -= num2[i]
        res.append((t+10)%10)
        if t<0: t = 1
        else: t= 0
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res


if __name__ == '__main__':
    num1 = input()
    num2 = input()
    num1_l, num2_l = [], []
    for i in range(len(num1)-1, -1, -1): num1_l.append(int(num1[i]))
    for i in range(len(num2)-1, -1, -1): num2_l.append(int(num2[i]))
    if comp(num1_l, num2_l):
        res= sub(num1_l, num2_l)
    else:
        res = sub(num2_l, num1_l)
        print('-', end='')
    for j in res[::-1]:
        print(j, end='')