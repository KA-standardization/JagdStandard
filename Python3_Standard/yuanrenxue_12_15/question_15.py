import pywasm


def env_abort(_: pywasm.Ctx):
    return


vm = pywasm.load(r'C:\Users\Administrator\Desktop\main.wasm', {
    'env': {
        'abort': env_abort,
    }
})
r = vm.exec('encode', [803226584, 803226580])
print(r)