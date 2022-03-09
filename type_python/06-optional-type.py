from typing import Union, Optional

# 아래의 두 코드는 같다
xxx: Union[str, None] = 'amamov'
yyy: Optional[str] = 'amamov'


def foo(name: str) -> Optional[str]:
    if name == 'taxijjang':
        return None
    else:
        return name


zzz: Optional[str] = foo('taxijjang')
