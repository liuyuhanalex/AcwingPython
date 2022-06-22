from typing import List


def add(num1: List[int], num2: List[int]):
    if len(num2) > len(num1): return add(num2, num1)
    t = 0
    final  = []
    for i in range(len(num1)):
        t += num1[i]
        if i < len(num2):
            t += num2[i]
        final.append(t%10)
        t = t//10
    if t: final.append(t)
    return final


if __name__ == '__main__':
    num1 = input()
    num2 = input()
    num1_l, num2_l = [], []
    for i in range(len(num1)-1, -1, -1): num1_l.append(int(num1[i]))
    for i in range(len(num2)-1, -1, -1): num2_l.append(int(num2[i]))
    final = add(num1_l, num2_l)
    for i in range(len(final)-1, -1, -1):
        print(final[i], end='')