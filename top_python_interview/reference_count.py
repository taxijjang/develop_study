class RefExam():
    def __init__(self):
        print('create objects')

    def __del__(self):
        print(f'destroy {id(self)}')


a = RefExam()
print(id(a))
a = 0
print(id(a))

print("-------------")

class RefExam():
    def __init__(self):
        print('create object')
        self.me = self

    def __del__(self):
        print(f'destroy {id(self)}')


a = RefExam()
a = 0
print('end .....')
