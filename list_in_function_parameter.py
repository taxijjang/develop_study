# https://web.archive.org/web/20200221224620/http://effbot.org/zone/default-values.htm
# 아주 적절한 설명

# mutable한 객체를 기본값으로 사용할 때 문제가 발생 한다.
# 즉 list나 사전같은 type
def func(data=[]):
    data.append(1)
    return data

print(func(), id(func))
print(func(), id(func))
print(func(), id(func))
print(func(), id(func))

# [1]           140581601572768
# [1, 1]        140581601572768
# [1, 1, 1]     140581601572768
# [1, 1, 1, 1]  140581601572768


"""
- python에서는 모든 것이 object이다. function 또한 마찬가지이다. 돌아가는 것은 함수처럼 돌아가지만 그냥 class라고 봐도 무방하다.
- 그리고, prameter는 함수 func1의 parameter data는 class attribute로 존재한다. 즉, 매 함수를 콜 할때마다
  새로운 instance를 만들어주는 것이 아니고, 동일한 값을 class 내부에 지정해두고 같은 값을 공유하게 된다. 
"""

"""
왜 그렇게 하느냐? 비효율적인것 아닌가?Permalink
  그럴 수도 있습니다만, 이는 오히려 여러 instance를 만든다고 할때 그 강점이 부각되죠. 예를 들어봅시다. 다음의 코드가 있다고 할게요. parameter value가 “함수”죠. 만약, 각 instance들에 대해서 따로따로 member attribute로 해당 값을 정의해준다면, 어떤 일이 발생할까요? 모든 함수별로 따로 함수를 정의하게 됩니다. 따라서, 함수 콜이 발생할대마다 해당 함수는 복제되고, 메모리는 터지게 되겠죠.
  특히, 이렇게 parameter를 하나로서 관리하는 것은, recursion을 사용할 때 매우 탁월하게 사용될 수 있습니다.
"""
import numpy
def func1(sin=np.sin, cos=np.cos):
    pass

"""
따라서, 만약 parameter가 함수가 실행될때마다 매번 초기화되는 것을 원한다면, 함수 내부에 다음과 같이 작성해주는 것이 좋습니다.
"""
def func(a=None):
    if a is None:
        a = []