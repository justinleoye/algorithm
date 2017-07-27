#!/usr/bin/python
#coding: utf8
#########################################################################
# File Name: quick_sort.py
# Author: Justin Leo Ye
# Mail: justinleoye@gmail.com 
# Created Time: Wed Jul 26 08:55:31 2017
#########################################################################


def quick_sort(l, lower, upper):
    if len(l) == 0 or lower >= upper:
        return

    pivot = l[lower]

    left, right = lower + 1, upper

    while left <= right:
        while left <= right and l[left] < pivot:
            left += 1
        while left <= right and l[right] >= pivot:
            right -= 1
        if left > right:
            break
        l[left], l[right] = l[right], l[left]
    l[lower], l[right] = l[right], l[lower]

    quick_sort(l, lower, right - 1)
    quick_sort(l, right + 1, upper)


def test():
    l1 = []
    l2 = [1]
    l3 = [2,1,4,3,5]
    l4 = [2,1,4,3,5,3,3,4,5]

    quick_sort(l1, 0, 0)
    quick_sort(l2, 0, 0)
    quick_sort(l3, 0, 4)
    quick_sort(l4, 0, 8)

    print l1
    print l2
    print l3
    print l4

if __name__ == '__main__':
    test()
