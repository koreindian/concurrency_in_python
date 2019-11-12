def foo(n):
    print('FOO:', n)
    bar(n+1)

def bar(n):
    print('BAR:', n)
    foo(n+2)

foo(0)
