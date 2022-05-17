import json

data = {'a': 11, 'b': 12, 'c': 'abc', 'd': '山岚云岫'}
print(json.dumps(data))
print(json.dumps(data, separators=(':', ',')))
print(json.dumps(data, ensure_ascii=False, separators=(':', ',')))
print(json.dumps(data, ensure_ascii=False, indent=5, sort_keys=True))
