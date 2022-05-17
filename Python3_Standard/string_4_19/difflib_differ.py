import difflib

text1 = '''abc bcd 123 456'''

text2 = '''abc, bcd 123 456'''

d = difflib.Differ()
diff = d.compare(text1, text2)
print('\n'.join(diff))
