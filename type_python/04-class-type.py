# class types


class Hello:
    def world(self) -> int:
        return 7


hello: Hello = Hello()


def foo(ins: Hello) -> int:
    return ins.world()


print(foo(hello))
