#!/usr/bin/python
#coding: utf8
#########################################################################
# File Name: pop_sort.py
# Author: Justin Leo Ye
# Mail: justinleoye@gmail.com 
# Created Time: Tue Jul 25 23:50:19 2017
#########################################################################


def pop_sort(l):
    n = len(l)
    for i in range(0, n):
        for j in range(1, n-i):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]


def test():
    l1 = []
    l2 = [1]
    l3 = [2,1,4,3,5]
    l4 = [2,1,4,3,5,3,3,4,5]

    pop_sort(l1)
    pop_sort(l2)
    pop_sort(l3)
    pop_sort(l4)

    print l1
    print l2
    print l3
    print l4

if __name__ == '__main__':
    test()
