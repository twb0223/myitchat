# -*- coding: utf-8 -*-
# L1 = ['Hello', 'World', 18, 'Apple', None]

# L2=[s.lower() for s in L1 if isinstance(s,str)]

# print(L2)


import asyncio

async def hello():
    print("hi")
    r=await asyncio.sleep(1)
    print("again")

hello()