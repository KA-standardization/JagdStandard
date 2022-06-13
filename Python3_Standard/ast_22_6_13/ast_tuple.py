import ast

s = ("abc", 123, "true")
# s2 = str(s)
s2 = repr(s)
s3 = ast.literal_eval(s2)
print(type(s3), s3)
