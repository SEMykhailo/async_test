import asyncio
from time import sleep

async def A():
    while True:
        print("AAAAAAAA")
        sleep(1)
        await C()

async def B():
    while True:
        print("BBBBBBB")
        sleep(1)
        await A()

async def C():
    while True:
        print("CCCCCCC")
        sleep(1)
        await B()


async def main():
    tasks = [
        A(),
        B(),
        C()
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())

