from ast import Str
from dataclasses import dataclass, field
from turtle import st
from typing import Any, Optional


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

    def size(self) -> int:
        # left.size() + 1 + right.size()
        sz = 1

        if self.left:
            sz += self.left.size()

        if type(self.right) is BinaryNode:
            sz += self.right.size()

        return sz

    def depth(self) -> int:
        # 1 + max(self.left.depth(), self.right.depth())
        tiefe_links = 0
        tiefe_rechts = 0

        if type(self.left) is BinaryNode:
            tiefe_links = self.left.depth()
        
        if self.right:
            tiefe_rechts = self.right.depth()


        return 1 + max(tiefe_links, tiefe_rechts)

    def post_order(self) -> list[int]:
        out =[]
        #bearbeitung links
        if self.left:
            out.extend(self.left.post_order())
        #bearbeitung rechts
        if self.right:
            out.extend(self.right.post_order())

        #selbst bearbeiten
        out.append(self.id)
        return out

    def flip(self):
        self.left, self.right = self.right, self.left
        if type(self.left) is BinaryNode:
            self.left.flip()
        
        if self.right:
            self.right.flip()


def insert(tree: Optional[BinaryNode], id: int) -> BinaryNode:
    match tree:
        case None:
            return BinaryNode(id, None, None)
        case BinaryNode(current_id, left, _) if id < current_id:
            tree.left = insert(left, id)
        case BinaryNode(current_id, _, right) if id > current_id:
            tree.right = insert(right, id)

    return tree


def create_tree(ids: list[int]) -> Optional[BinaryNode]:
    tree = None

    for id in ids:
        tree = insert(tree, id)
    
    return tree


def find(tree: Optional[BinaryNode], id: int) -> bool:
    # match tree:
    #     case BinaryNode(current_id, _, _) if id == current_id:
    #         return True
    #     case BinaryNode(current_id, left, _) if id < current_id:
    #         return find(left)
    #     case BinaryNode(current_id, _, right) if id > current_id:
    #         return find(right)
    #     case _:
    #         return False

    if type(tree) is not BinaryNode:
        return False

    if tree.id == id:
        return True

    elif tree.id < id:
        return find(tree.right, id)

    elif tree.id > id:
        return find(tree.left, id)


def select(tree: Optional[BinaryNode], lower: int, upper: int) -> list[int]:
    l = []

    if tree is None:
        return l
    
    l.extend(select(tree.left, lower, upper))
    if lower <= tree.id and tree.id < upper:
        l.append(tree.id)
    
    l.extend(select(tree.right, lower, upper))

    return l


@dataclass(order=True)
class Node:
    id: int
    children: "list[Node]" = field(default_factory=list, compare=False)
    
    def __str__(self) -> str:
        s = ""
        for child in self.children:
            s += str(child) + ", "
        return f"Node({self.id}, [{s[:-2]}])"
    
    def __repr__(self) -> str:
        return str(self)

    def weight(self) -> int:
        w = self.id
        for child in self.children:
            w += child.weight()
        
        return w


def on_layer(tree: Node, depth: int) -> list[int]:
    l = []
    if depth != 0:
        for child in tree.children:
            l+= on_layer(child, depth - 1)
    else:
        l.append(tree.id)
    return sorted(l)

def leaves(tree: Node) -> list[Node]:
    l = []
    if tree.children:
        for child in tree.children:
            l.extend(leaves(child))
    else:
        l.append(tree)
    # lambda is not needed if order=True is set in the dataclass proberty
    return sorted(l, key=lambda n: n.id)


# demo to show how extend() might be implemented.
def my_extend(lst_to: list[Any], lst_add_from: list[Any]):
    for element in lst_add_from:
        lst_to.append(element)



if __name__ == "__main__":
    tree = BinaryNode(1, BinaryNode(2, None, BinaryNode(3, None, None)), None)
    assert str(tree) == "BinaryNode(1, BinaryNode(2, None, BinaryNode(3, None, None)), None)"

    print(f"{tree.size()=}")

    tree = BinaryNode(1, None, None)

    print(f"{tree.depth()=}")

    tree = BinaryNode(1, BinaryNode(2, None, None), BinaryNode(3, None, BinaryNode(4, None, None)))

    print(f"{tree.depth()=}")

    print(f"{tree.post_order()=}")

    tree.flip()

    print(tree)

    tree = insert(None, 5)
    tree = insert(tree, 3)
    tree = insert(tree, 4)
    tree = insert(tree, 7)

    print(f"insert_tree = {tree}")

    tree = create_tree([5, 3, 4, 7])

    print(f"create_tree = {tree}")

    tree = create_tree([8, 3, 25, 1, 5, 7, 100, 11])

    print(f"{find(tree, 11)=}")

    print(f"{find(tree, 42)=}")

    tree = create_tree([8, 3, 25, 1, 5, 7, 100, 11])
    print(f"{select(tree, 5, 11)=}")
    print(f"{select(tree, 200, 300)=}")

    tree = Node(4, [Node(5, []), Node(6, [Node(2, [])]), Node(3, [])])
    print("tree = " + str(tree))

    print(f"{tree.weight()=}")

    tree = Node(4, [Node(5, []), Node(6, [Node(2, [])]), Node(3, [])])
    print(f"{on_layer(tree, 0)=}")
    print(f"{on_layer(tree, 1)=}")
    print(f"{on_layer(tree, 2)=}")

    tree = Node(4, [Node(5, []), Node(6, [Node(2, [])]), Node(3, [])])
    print(f"{leaves(tree)=}")
    print(leaves(tree) == [Node(2 ,[]), Node(3, []), Node(5, [])])