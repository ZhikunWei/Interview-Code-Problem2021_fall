#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def cyclicShiftTree(self, root, k):
        # write code here
        import queue
        q1 = queue.Queue()
        q2 = queue.Queue()
        q1.put(root)
        tree = [None]
        layer = 0
        while not q1.empty():
            while not q1.empty():
                q2.put(q1.get())
            finish = True
            while not q2.empty():
                node = q2.get()
                if node:
                    tree.append(node)
                    q1.put(node.left)
                    q1.put(node.right)
                    finish = False
                else:
                    tree.append(None)
                    q1.put(None)
                    q1.put(None)
            if finish:
                break
            layer += 1
        for i in range(1, layer + 1):
            r_layer = layer - i+1
            tmp = []
            for j in range(2 ** r_layer, 2 ** (r_layer + 1)):
                tmp.append(tree[j])
            for j in range(2 ** r_layer, 2 ** (r_layer + 1)):
                tree[j] = tmp[(j - 2 ** r_layer + len(tmp) - k) % len(tmp)]
            for j in range(2 ** r_layer-1, 2 ** (r_layer )):
                if tree[j]:
                    tree[j].left = tree[2 * j]
                    tree[j].right = tree[2 * j + 1]
        
        # tree[1].left = tree[2]
        # tree[1].right = tree[3]
        # for i in range(1, layer + 1):
        #     for j in range(2 ** i, 2 ** (i + 1)):
        #         if tree[j]:
        #             tree[j].left = tree[2 * j]
        #             tree[j].right = tree[2 * j + 1]
        return tree[1]