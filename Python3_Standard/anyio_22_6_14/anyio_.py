import httpx
import anyio


async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get('http://www.baidu.com/')
        print(response.text)


anyio.run(main, backend='trio')
