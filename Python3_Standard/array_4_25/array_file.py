import array
import binascii
import tempfile


a = array.array('i', range(10))

output = tempfile.NamedTemporaryFile()
a.tofile(output.file)
output.flush()

with open(output.name, 'rb') as input:
    data = input.read()
    # seek() 方法用于移动文件读取指针到指定位置。
    # offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
    # whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
    input.seek(0)
    a2 = array.array('i')
    a2.fromfile(input, len(a))
    print(a2)

a3 = array.array('i', range(10))
print(a3)
a3_bytes = a3.tobytes()
print(a3_bytes)
a4 = array.array('i')
a4.frombytes(a3_bytes)
print(a4)
