import time
import asyncio

# #Örnek 1
# async def selamla(mesaj):
#     print("start")
#     await asyncio.sleep(2)
#     print(mesaj)

# donen_obje = selamla("merhaba dünya")
# print(donen_obje)

# asyncio.run(donen_obje)

# #Örnek 2
# async def job(name, sec):
#     print(f"{name} başladı")
#     await asyncio.sleep(sec)
#     print(f"{name} bitti")

# async def main():
#     t1 = asyncio.create_task(job("A", 3))
#     t2 = asyncio.create_task(job("B", 2))

#     await t1
#     await t2


# asyncio.run(main()) 

# #Örnek 3
# async def fetch_data(delay):
#     print("Veri alınıyor...")
#     await asyncio.sleep(delay)
#     print("Veri alındı")
#     return {"data": "bazı veriler alındı"}


# async def main():
#     print("start")
#     task = fetch_data(3)
#     print("end")
#     result = await task
#     print("dönen couritiune objesinin içi: ", result)
#     print("end2")

# asyncio.run(main())

# Örnek 4
async def fetch_data(id, delay):
    print("Veri alınıyor...")
    await asyncio.sleep(delay)
    print("Veri alındı id:", id)
    return {"id": id, "data":"bazı veriler alındı"}

async def main():
    task1 = asyncio.create_task(fetch_data(1, 3))
    task2 = asyncio.create_task(fetch_data(2, 1))
    task3 = asyncio.create_task(fetch_data(3, 2))
    
    result1 = await task1
    result2 = await task2
    result3 = await task3
    print(result1)
    print(result2)
    print(result3)

t = time.time()
asyncio.run(main())    
print("Toplam süre:", time.time() - t)