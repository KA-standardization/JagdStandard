import time
import asyncio
import aiohttp


async def parse(url):
    # print(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            response = response.decode('gbk')
            filename = url.split('=')[-1]

            # await asyncio.create_task(save(response, filename))
            save(response, filename)

            # print(url, '+++++++++++')


def save(response, filename):
    # await asyncio.sleep(5)
    with open(f'./{filename}.txt', 'w+', encoding='utf-8') as fp:
        fp.write(response)
        # print(filename, 'success')
    # def foo():
    #     # a = open(f'./{filename}.txt', 'w+', encoding='utf-8')
    #     # yield a.write(response)
    #     # a.close()
    #     # yield with open(f'./{filename}.txt', 'w+', encoding='utf-8') as fp:
    #     #     fp.write(response)
    #     #     print(filename, 'success')
    #     a = open(f'./{filename}.txt', 'w+', encoding='utf-8')
    #     a.write(response)
    #     a.close()
    #     yield a
    #
    #
    # foo()


if __name__ == '__main__':

    tasks = []
    for i in range(20):
        url = f'https://pic.netbian.com/e/search/result/?searchid={i}'
        task = asyncio.ensure_future(parse(url))
        tasks.append(task)

    t = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - t)
