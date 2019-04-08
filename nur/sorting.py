#!/usr/bin/env python3

import nur.routines as rt


def quick_sort(values, _low=None, _high=None):
    '''
    Sort an array using the `quick sort` method. This recursively chooses a 
    pivot element and sorts all values on the left and the right of the pivot
    with swapping.

    Sorting is done in place. Pass a copy of the values if you want to keep the
    original ordering.

    Parameters
    ----------
    values : array-like (1D)
        The array of values to be sorted
    '''
    _low = 0 if _low is None else _low
    _high = len(values)-1 if _high is None else _high
    
    if _low < _high:
        pivot = values[_low]
        mid = _low
        for curr in range(_low+1, _high+1):
            if values[curr] < pivot:
                mid += 1
                values[mid], values[curr] = rt.switch(values[mid], values[curr])

        values[_low], values[mid] = rt.switch(values[_low], values[mid])

        quick_sort(values, _low, mid-1)  # left half
        quick_sort(values, mid+1, _high) # right half



''' Attempt at heap sorting. Doesn't work!  '''

class BinaryNode:
    def __init__(self, value=None, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None


    def __str__(self):
        '''
        Print the node value and the values of its pointers in the format:

            P       <- parent value
            C       <- current node value
          L   R     <- left and right node values

        (note this only looks nice for single digit numbers)
        '''
        p = '  ' + str(self.parent.value) + '\n' if self.parent else ''
        c = '  ' + str(self.value) + '\n'
        l = str(self.left.value) + '   ' if self.left else ''
        r = str(self.right.value) if self.right else ''
        return p + c + l + r

    def __repr__(self):
        return '%s:\n%s' %(type(self), self.__str__())


class BinaryTree:
    '''
    An unsorted binary tree
    '''

    def __init__(self, values):
        self.values = values

        self.build_tree()


    def build_tree(self):
        '''
        Recursively construct an (unsorted) binary tree from a list of values
        '''
        def insert(root, i):
            if i < len(self.values):
                curr = BinaryNode(self.values[i], root)
                curr.left = insert(curr, 2*i+1)
                curr.right = insert(curr, 2*i+2)

                root = curr

            return root

        self.root = insert(None, 0)

        return self


class HeapTree(BinaryTree):

    def __init__(self, values):
        super().__init__(values)
        self.build_heap()

    def build_heap(self):
        '''
        Sort the binary tree into a heap where the parent node is always
        larger than either of its two children.
        '''
        def heap_swap(node):
            if node.left and (node.left.value > node.value):
                print('L: %s <-> %s' %(node.left.value, node.value))
                node.left.value, node.value = rt.switch(node.left.value, 
                                                        node.value)
                heap_swap(node.left)

            if node.right and (node.right.value > node.value):
                print('R: %s <-> %s' %(node.right.value, node.value))
                node.right.value, node.value = rt.switch(node.right.value, 
                                                         node.value)
                heap_swap(node.right)

            if node.parent and (node.value >= node.parent.value):
                print('U: %s <-> %s' %(node.value, node.parent.value))
                node.parent.value, node.value = rt.switch(node.parent.value, 
                                                          node.value)
                heap_swap(node.parent)

        heap_swap(self.root)


    def sort(self):
        pass


