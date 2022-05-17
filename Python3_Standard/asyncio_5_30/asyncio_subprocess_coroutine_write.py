import asyncio
import asyncio.subprocess


async def to_upper(input):
    print('in to upper')
    create = asyncio.create_subprocess_exec('tr', '[:lower:]', '[:upper:]', stdout=asyncio.subprocess.PIPE,
                                            stdin=asyncio.subprocess.PIPE)
    print('launching process')
    proc = await create
    print('pid {}'.format(proc.pid))

    print('communicating with process')
    stdout, stderr = await proc.communicate(input.encode())
    print('waiting for process to complete')
    await proc.wait()

    return_code = proc.returncode
    print('return code {}'.format(return_code))

    if not return_code:
        res = bytes(stdout).decode()
    else:
        res = ''
    return (return_code, res)


MESSAGE = '''
this message will be converted
to all caps
'''

event_loop = asyncio.get_event_loop()
try:
    return_code, results = event_loop.run_until_complete(to_upper(MESSAGE))
finally:
    event_loop.close()

if return_code:
    print('error exit {}'.format(return_code))
else:
    print('old: {!r}'.format(MESSAGE))
    print('new: {!r}'.format(results))
