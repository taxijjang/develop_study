# decorator

def copyright2(func):
    def new_func():
        func()
        print('@@ taxijjang')

    return new_func

def copyright(func):
    def new_func():
        func()
        print('@ taxijjang')

    return new_func


@copyright2
@copyright
def smile():
    print('a')

@copyright2
@copyright
def angry():
    print('b')

@copyright2
@copyright
def love():
    print('c')


# 함수에 @를 이용하여 decorator를 이용하지 않는다면 아래와 같이 사용 가능
# smile = copyright(smile)
# angry = copyright(angry)
# love = copyright(love)

smile()
angry()
love()
