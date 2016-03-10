# !user/bin/env/ python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

def invertTree(self, root):
    if not root or root.left==root.right==None: return root

    parent = [root]
    while len(parent):
        children = []
        for node in parent:
            node.left, node.right = node.right, node.left
            if node.left: children.append(node.left)
            if node.right: children.append(node.right)
        parent = children
    return root
