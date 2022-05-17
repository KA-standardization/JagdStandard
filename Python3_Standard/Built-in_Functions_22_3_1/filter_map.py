abc = "ABCD"
b = [ord(s) for s in abc if ord(s) > 65]
print(b)
b2 = list(filter(lambda x: x > 65, map(ord, abc)))
print(b2)
