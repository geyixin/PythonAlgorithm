#!/usr/bin/env python
# -*- coding:utf-8 -*-


def main():
    seq = [1,3,2,0,6,5]
    ins_sort_rec(seq, len(seq)-1)
    print(seq)
    print('----------------------------------------')
    seq = [1, 3, 2, 0, 6, 5]
    ins_sort(seq)
    print(seq)
    print('----------------------------------------')
    seq = [1, 3, 2, 0, 6, 5]
    sel_sort_rec(seq, len(seq)-1)
    print(seq)
    print('----------------------------------------')
    seq = [1, 3, 2, 0, 6, 5]
    sel_sort(seq)
    print(seq)


"""
插入排序，这儿是从头开始，把小的尽量往前移动
"""


# 递归版的插入排序
def ins_sort_rec(seq, i):
    if i == 0:
        return
    ins_sort_rec(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        print(seq)
        j -= 1


# 迭代版的插入排序
def ins_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            print(seq)
            j -= 1


"""
选择排序，这儿是先把最大的移动最后，然后是倒数第二大的
对于每一位而言，每一次排序结束，它前面再无比它大的数
"""


# 递归版的选择排序
def sel_sort_rec(seq, i):
    if i == 0: return
    max_j = i
    for j in range(i):
        if seq[j] > seq[max_j]: max_j = j
    seq[i], seq[max_j] = seq[max_j], seq[i]
    print(seq)
    sel_sort_rec(seq, i-1)


# 迭代版的选择排序
def sel_sort(seq):
    for i in range(len(seq)-1, 0, -1):
        max_j = i
        for j in range(i):
            if seq[j] > seq[max_j]: max_j = j
        seq[i], seq[max_j] = seq[max_j], seq[i]
        print(seq)


if __name__ == '__main__':
    main()