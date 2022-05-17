import textwrap

t = '''
    Shall I compare thee to a summer's day?
    Thou art more lovely and more temperate:
    Rough winds do shake the darling buds of May,
    And summer's lease hath all too short a date:
    Sometime too hot the eye of heaven shines,
    And often is his gold complexion dimm'd;
    And every fair from fair sometime declines,
    By chance or nature's changing course untrimm'd
    But thy eternal summer shall not fade
    Nor lose possession of that fair thou owest;
    Nor shall Death brag thou wander'st in his shade,
    When in eternal lines to time thou growest:
    So long as men can breathe or eyes can see,
    So long lives this and this gives life to thee.
'''

print(t)
dedent_text = textwrap.dedent(t)
print(dedent_text)

fill_text = textwrap.fill(dedent_text, 90)
print(fill_text)

fill_text_2 = textwrap.fill(dedent_text, initial_indent='', subsequent_indent=' ' * 4, width=50)
print(fill_text_2)

indent_text = textwrap.indent(fill_text, '->>')
print(indent_text)


def pre_indent(line):
    return len(line) % 2 == 0


indent_text_2 = textwrap.indent(fill_text, '<<-', predicate=pre_indent)
print(indent_text_2)
t2 = '泰阿泰德 泰阿泰德 泰阿泰德 泰阿泰德 泰阿泰德'

shorten_text = textwrap.shorten(t2, 10, placeholder='')
print(shorten_text)

print(len(t2))
print(bytes(t2, 'utf8'))
print(len(bytes(t2, 'utf8')))

t3='abc'
print(len(t3))
print(bytes(t3, 'utf8'))
print(len(bytes(t3, 'utf8')))

