import string

data = {'something': 100}

t = string.Template('num:$something+111')
print(t.substitute(data))

t2 = string.Template("""
a=$something
b=$val
""")
print(t2.safe_substitute(data))


class MyTemplate(string.Template):
    delimiter = '&'
    idpattern = r'\w+|[0-9]+'


data2 = {'a': 100, 'b': 'GYj'}
t3 = MyTemplate('''
hello:&a
world:&b
''')
print(t3.safe_substitute(data2))

t4 = string.Template('$a')
print(t4.pattern.pattern)


class MyTemplate2(string.Template):
    delimiter = '{{'
    pattern = r'''
    \{\{(?:
      (?P<escaped>\{\{) |   # Escape sequence of two delimiters
      (?P<named>(?a:[_a-z][_a-z0-9]*))\}\}      |   # delimiter and a Python identifier
      {(?P<braced>(?a:[_a-z][_a-z0-9]*))\}\}  |   # delimiter and a braced identifier
      (?P<invalid>)              # Other ill-formed delimiter exprs
    )
    '''


t5 = MyTemplate2('''
{{{{
{{var}}
''')
data5 = {'var': '32'}
print(t5.safe_substitute(data5))
