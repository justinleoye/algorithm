#!/usr/bin/python
#coding: utf8
#########################################################################
# File Name: heap_sort.py
# Author: Justin Leo Ye
# Mail: justinleoye@gmail.com 
# Created Time: Thu Jul 27 09:04:30 2017
#########################################################################


def heap_sort(l):
    n = len(l)
    first = n / 2 - 1 # 最后一个非叶子结点

    for start in range(first, -1, -1): # 创建大根堆
        adjust_heap(l, start, n-1)

    for end in range(n-1, 0, -1): # 排序，根结点依次出堆
        l[0], l[end] = l[end], l[0]
        adjust_heap(l, 0, end-1)


def adjust_heap(l, start, end): # 调整堆
    root = start
    while True: # 递归调整堆
        child = root * 2 + 1
        if child > end: break # 已经遍历最后一个非叶子结点
        if child+1 <= end and l[child] < l[child+1]: # 如果存在右子结点，则比较左右子结点，取较大者
            child += 1
        if l[child] > l[root]: # 比较结点和其较大子结点，如果结点小于其子结点，则调整位置
            l[child], l[root] = l[root], l[child]
            root = child # 调整位置后，继续递归调整
        else: # 如果结点大于等于子结点，则说明堆调整完毕
            break


def test():
    l1 = []
    l2 = [1]
    l3 = [2,1,4,3,5]
    l4 = [2,1,4,3,5,3,3,4,5]

    heap_sort(l1)
    heap_sort(l2)
    heap_sort(l3)
    heap_sort(l4)

    print l1
    print l2
    print l3
    print l4

if __name__ == '__main__':
    test()
