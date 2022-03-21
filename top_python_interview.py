import array as arr


"""
arr.arr(type, [values])

type 
_IntTypeCode = Literal["b", "B", "h", "H", "i", "I", "l", "L", "q", "Q"]
_FloatTypeCode = Literal["f", "d"]
_UnicodeTypeCode = Literal["u"]
"""
my_array = arr.array('f', [1,2,3,4])
my_list = [1, 'abc', 20]

print(my_array)
print(my_list)
