from dataclasses import dataclass
from typing import Optional


@dataclass
class BinaryNode:
    id: int
    left: "Optional[BinaryNode]"
    right: "Optional[BinaryNode]"

    # bNode = BinaryNode(1, None, None)
    # print(str(bNode))
    def __str__(self) -> str:
        # print(f"{id} {id}")
        # print(str(id)+" "+str(id))
        return "BinaryNode("+str(self.id)+", "+self.left.__str__()+", "+str(self.right)+")"

    def size(self):
        pass

    def depth(self):
        pass

    def post_order(self):
        pass

    def flip(self):
        pass


def insert(tree: Optional[BinaryNode], id: int):
    pass


def create_tree(ids):
    pass


def find(tree, id):
    pass


def select(tree, lower, upper):
    pass


@dataclass
class Node:
    
    def __str__(self):
        pass

    def weight(self):
        pass


def on_layer(tree, depth):
    pass


def leaves(tree):
    pass
