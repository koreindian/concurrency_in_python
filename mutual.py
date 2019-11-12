import asyncio

@asyncio.coroutine
def foo(n):
    print('FOO:', n)
    asyncio.async(bar(n+1))

@asyncio.coroutine
def bar(n):
    print('BAR:', n)
    asyncio.async(foo(n+2))

loop = asyncio.get_event_loop()
asyncio.async(foo(0))
loop.run_forever()
loop.close()
