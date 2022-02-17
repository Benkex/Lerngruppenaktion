from dataclasses import dataclass
from typing import Optional


@dataclass
class BinaryNode:

    def __str__(self):
        pass

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
