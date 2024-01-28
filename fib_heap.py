from __future__ import annotations

class Node:
    def __init__(self, val: float, children: [Node], parent: Node, degree: int):
        self.val = val
        self.children = children
        self.parent = parent
        self.degree = degree

class FibHeap:
    def __init__(self):
        self.min_ind = 0
        self.roots = []
        self.degree = 0

    def add(self, val: float) -> None:
        node = Node(val, [], None, 0)
        self.roots.append(node)
        if len(self.roots):
            if node.val < self.roots[self.min_ind].val:
                self.min_ind = len(self.roots) - 1
            self.degree = max(self.degree, node.degree)

    def merge(self, heap: FibHeap) -> None:
        prev_len = len(self.roots)
        self._merge_list(heap.roots)
        if heap.roots[heap.min_ind].val < self.roots[self.min_ind].val:
            self.min_ind = heap.min_ind + prev_len
        self.degree = max(self.degree, heap.degree)

    def extract_min(self) -> float | None: 
        if self.empty():
            return None
        val = self.roots[self.min_ind].val
        self._merge_list(self.roots[self.min_ind].children)
        del self.roots[self.min_ind]
        self._consolidate()
        return val
    
    def empty(self) -> bool:
        return len(self.roots) == 0

    def _merge_list(self, list: [Node]) -> None:
        self.roots = self.roots + list

    def _consolidate(self) -> None:
        cons_list = [None] * (len(self.roots) + self.degree)
        for tree in self.roots:
            self._push_to_cons_list(cons_list, tree)
        self.roots = []
        self.min_ind = 0
        self.degree = 0
        for tree in cons_list:
            if tree != None:
                self.roots.append(tree)
                if tree.val < self.roots[self.min_ind].val:
                    self.min_ind = len(self.roots) - 1
                self.degree = max(self.degree, tree.degree)

    def _push_to_cons_list(self, cons_list: list, node: Node) -> None:
        if cons_list[node.degree] != None:
            new_tree = self._merge_node(cons_list[node.degree], node)
            cons_list[new_tree.degree - 1] = None
            self._push_to_cons_list(cons_list, new_tree)
        else:
            cons_list[node.degree] = node

    def _merge_node(self, node1: Node, node2: Node) -> Node | None:
        if node1.degree != node2.degree:
            return None
        if node1.val < node2.val: 
            min_node = node1
            another_node = node2
        else:
            min_node = node2
            another_node = node1
        min_node.children.append(another_node)
        another_node.parent = min_node
        min_node.degree += 1
        return min_node
