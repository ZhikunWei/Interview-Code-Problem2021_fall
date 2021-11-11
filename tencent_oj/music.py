#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

class node():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def f(root):
    import queue
    Q = queue.Queue()
    Q.put(root)
    while not Q.empty():
        t = Q.get()
        if t.left is not None and t.left.left is None and t.left.left.left is not None and t.left.left.right is None:
            t.left = None
        elif t.left is not None:
            Q.put(t.left)
            
        if t.right is not None and t.right.left is None and t.right. t.right.right is None:
            t.right = None
        elif t.right is not None:
            Q.put(t.right)
    return root