tmp = []


def emit(d):
    yield d


def map_(key, line):
    for word in line.split():
        t = emit((word, 1))
        shuffle(t)


def shuffle(t):
    tmp.append(next(t))


def reducer(t):
    # type: (t) -> Iterator[_T]
    return sorted(dict(t).items(), key=lambda x: x[0])



if __name__ == '__main__':
    # data = [
    #     (1, "To execute this mapper and associated reducer on Hadoop Streaming use the"),
    #     (2, "Outputs statistical aggregations per key from a striped mapper a"),
    # ]
    # emit(data[0])
    # for d in data:
    #     map_(d[0], d[1])
    #
    # a = shuffle(shuffle_tmp)
    # b = reducer(a)
    # c = sorted(b.items(), key=lambda x: x[1], reverse=True)
    # print(c)

    s = "To execute this mapper and associated reducer on Hadoop Streaming use the"
    map_(1, s)
    print(reducer(tmp))
