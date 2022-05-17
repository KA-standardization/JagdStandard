import codecs

with codecs.open('./text.txt', 'r', encoding='utf-32') as f:
    print(f.read())
