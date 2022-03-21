def function(arg):
    arg += " in function"
    print(arg)


immutable = "hello"
function(immutable)
print(immutable)

mutable = list('hello')
function(mutable)
print(mutable)
