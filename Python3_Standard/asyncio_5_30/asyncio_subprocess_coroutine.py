import asyncio
import asyncio.subprocess


def _parse_results(output):
    print('parsing results')
    if not output:
        return []
    lines = output.splitlines()
    headers = lines[0].split()
    devices = lines[1:]
    results = [dict(zip(headers, line.split())) for line in devices]
    return results


async def run_df():
    print('in run df')
    buffer = bytearray()
    create = asyncio.create_subprocess_exec('df', '-hl', stdout=asyncio.subprocess.PIPE)
    proc = await create
    print('process started {}'.format(proc.pid))

    while True:
        line = await proc.stdout.readline()
        print('read {!r}'.format(line))
        if not line:
            print('no more output from command')
            break

        buffer.extend(line)
    await proc.wait()

    return_code = proc.returncode
    print('return code {}'.format(return_code))
    if not return_code:
        cmd_output = bytes(buffer).decode()
        results = _parse_results(cmd_output)
    else:
        results = []

    return (return_code, results)


event_loop = asyncio.get_event_loop()
try:
    return_code, results = event_loop.run_until_complete(run_df())
finally:
    event_loop.close()

if return_code:
    print('error exit{}'.format(return_code))
else:
    for res in results:
        print('{Mounted:25}: {Avail}'.format(**res))

