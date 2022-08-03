import asyncio


async def f(name):
    print(f'({name})')
    await asyncio.sleep(1)
    await f(f'(spawned_from_{name})')


async def m(): await asyncio.gather(f('a'), f('b'), f('c'))


asyncio.run(m())