# class types
from typing import Optional


class Hello:
    def world(self) -> int:
        return 7


class World:
    pass


hello: Hello = Hello()
world: World = World()


def foo(ins: "Hello") -> int:
    return ins.world()


print(foo(hello))


class Node:
    def __init__(self, data: int, next_node: Optional["Node"]):
        self.data = data
        self.next = next_node


node = Node(12, None)

node2 = Node(27, node)
