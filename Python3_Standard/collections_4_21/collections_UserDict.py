import collections

userdict = collections.UserDict(args='Kaiser', kwargs={'a': 11})

print(userdict.__repr__())
