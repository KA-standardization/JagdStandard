from pympler import muppy, summary

# 内存
all_objects = muppy.get_objects()
print(len(all_objects))
suml = summary.summarize(all_objects)
summary.print_(suml)
