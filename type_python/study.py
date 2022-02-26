class Cal:
    # 생성자: 메모리에 올라오는 순간 즉시 실행된다.
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


# Instancef
cal1 = Cal(1, 2)
cal2 = Cal(3, 4)

print(cal1.a)
print(cal1.b)
print(cal1.add())

cal1.a = 7

print(cal2.a)
print(cal2.b)
