import time
import asyncio


async def start_strongmen(name, power):
    print(f'Силач {name} начал соревнования.')
    time_per_lift = 1 / power
    for i in range(5):
        await asyncio.sleep(time_per_lift)
        print(f'Силач {name} поднял {i + 1} шар.')
    print(f'Силач {name} закончил соревнование.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongmen('Pasha', 3))
    task2 = asyncio.create_task(start_strongmen('Denis', 4))
    task3 = asyncio.create_task(start_strongmen('Apollon', 5))

    await task1
    await task2
    await task3

asyncio.run(start_tournament())
