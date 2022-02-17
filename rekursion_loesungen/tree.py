from dataclasses import dataclass
from msilib import type_binary
from tkinter.messagebox import NO
from typing import Optional


@dataclass
class BinaryNode:
    id: int
    left: Optional["BinaryNode"]
    right: Optional["BinaryNode"]

    def __str__(self) -> str:
        return f"BinaryNode({self.id}, {self.left}, {self.right})"

    def size(self) -> int:
        sz = 1

        if type(self.left) is BinaryNode:
            sz += self.left.size()

        if type(self.right) is BinaryNode:
            sz += self.right.size()

        return sz
        
    def depth(self) -> int:
        dp_left = 0
        dp_right = 0

        if type(self.left) is BinaryNode:
            dp_left = self.left.depth()
        
        if type(self.right) is BinaryNode:
            dp_right = self.right.depth()
        
        return 1 + max(dp_left, dp_right)

    def post_order(self) -> list[int]:
        out = []

        if type(self.left) is BinaryNode:
            out.extend(self.left.post_order())
        
        if type(self.right) is BinaryNode:
            out.extend(self.right.post_order())
        
        out.append(self.id)
        return out

    def flip(self):
        self.left, self.right = self.right, self.left

        if type(self.left) is BinaryNode:
            self.left.flip()

        if type(self.right) is BinaryNode:
            self.right.flip()


def insert(tree: Optional[BinaryNode], id: int):
    match tree:
        case BinaryNode(i, left, _) if id < i:
            tree.left = insert(tree.left, id)
        case BinaryNode(i, _, right) if i < id:
            tree.right = insert(tree.right, id)
        case None:
            tree = BinaryNode(id, None, None)
    
    return tree


def create_tree(ids: list[int]) -> BinaryNode:
    tree = None

    for id in ids:
        tree = insert(tree, id)
    
    return tree


def find(tree: Optional[BinaryNode], id: int) -> bool:
    match tree:
        case BinaryNode(i, _, _) if i == id:
            return True
        case BinaryNode(i, left, _) if id < i:
            return find(left, id)
        case BinaryNode(i, _, right) if i < id:
            return find(right, id)
        case _:
            return False


def select(tree: Optional[BinaryNode], lower: int, upper: int) -> list[int]:
    pass


@dataclass
class Node:
    id: int
    children: list["Node"]
    
    def __str__(self) -> str:
        return f"Node({self.id}, {self.children})"

    def weight(self) -> int:
        w = self.id
        for child in self.children:
            w += child.weight()

        return w


def on_layer(tree: Node, depth: int) -> list[int]:
    if depth == 0:
        return [tree.id]

    out = []
    for child in tree.children:
        out.extend(on_layer(child, depth - 1))

    return out


def leaves(tree):
    pass
