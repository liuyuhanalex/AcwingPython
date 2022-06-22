from typing import List


def multiple(num1: List[int], num2: List[int]) -> object:
    res = []
    pass

if __name__ == '__main__':
    num1 = '1345'
    num2 = '2697'
    num1_l, num2_l = [], []
    for i in range(len(num1)-1, -1, -1): num1_l.append(num1[i])
    for i in range(len(num2)-1, -1, -1): num2_l.append(num2[i])
    multiple(num1_l, num2_l)
