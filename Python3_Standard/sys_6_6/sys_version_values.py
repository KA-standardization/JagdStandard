import sys

print(sys.version)
print(sys.version_info)
print(sys.hexversion)
print(sys.api_version)
print(sys.platform)
print(sys.implementation.name)
print(sys.implementation.version)
print(sys.implementation.cache_tag)

print(sys.flags)

print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())

print(sys.executable)
print(sys.prefix)

print(sys.getrecursionlimit())
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())

print(sys.maxsize)
print(sys.maxunicode)

print(sys.float_info)
print(sys.int_info)

print(sys.byteorder)

# sys.exit(1)
sys.exit(0)
