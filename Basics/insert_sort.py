#!/usr/bin/python
#coding: utf8
#########################################################################
# File Name: insert_sort.py
# Author: Justin Leo Ye
# Mail: justinleoye@gmail.com 
# Created Time: Tue Jul 25 23:20:26 2017
#########################################################################


def insert_sort(l):
    n = len(l)
    if n <= 1:
        return l

    for i in range(1, n):
        curr_num = l[i]
        idx = i
        while idx >0 and l[idx - 1] > curr_num:
            l[idx], l[idx-1] = l[idx - 1], l[idx]
            idx -= 1


def test():
    l1 = []
    l2 = [1]
    l3 = [2,1,4,3,5]
    l4 = [2,1,4,3,5,3,3,4,5]

    insert_sort(l1)
    insert_sort(l2)
    insert_sort(l3)
    insert_sort(l4)

    print l1
    print l2
    print l3
    print l4

if __name__ == '__main__':
    test()
