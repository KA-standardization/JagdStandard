import httpx
import trio


async def main(url):
    async with httpx.AsyncClient() as client:
        response = await client.get('http://www.baidu.com/')
        print(response.text)


trio.run(main)
