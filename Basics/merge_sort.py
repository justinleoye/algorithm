#!/usr/bin/python
#coding: utf8
#########################################################################
# File Name: merge_sort.py
# Author: Justin Leo Ye
# Mail: justinleoye@gmail.com 
# Created Time: Wed Jul 26 00:24:32 2017
#########################################################################


def merge_sort(l):
    n = len(l)
    if n <= 1:
        return l

    mid = n >> 1

    sorted_l1 = merge_sort(l[0:mid])
    sorted_l2 = merge_sort(l[mid:n])

    n1 = len(sorted_l1)
    n2 = len(sorted_l2)
    idx1 = 0
    idx2 = 0
    sorted_l = []

    while idx1 < n1 and idx2 < n2:
        if sorted_l1[idx1] < sorted_l2[idx2]:
            sorted_l.append(sorted_l1[idx1])
            idx1 += 1
        else:
            sorted_l.append(sorted_l2[idx2])
            idx2 += 1

    while idx1 < n1:
        sorted_l.append(sorted_l1[idx1])
        idx1 += 1

    while idx2 < n2:
        sorted_l.append(sorted_l2[idx2])
        idx2 += 1

    return sorted_l


def test():
    l1 = []
    l2 = [1]
    l3 = [2,1,4,3,5]
    l4 = [2,1,4,3,5,3,3,4,5]

    l1 = merge_sort(l1)
    l2 = merge_sort(l2)
    l3 = merge_sort(l3)
    l4 = merge_sort(l4)

    print l1
    print l2
    print l3
    print l4

if __name__ == '__main__':
    test()
