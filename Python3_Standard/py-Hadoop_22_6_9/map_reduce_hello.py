shuffle_tmp = []


def map_(key, line):
    for word in line.split():
        # print(word)
        shuffle_tmp.append((word, 1))


def shuffle(word_list):
    tmp_dict = dict()
    for item in word_list:
        flag = tmp_dict.get(item[0])
        if flag:
            flag.append(1)
            continue
        tmp_dict[item[0]] = [1]
    # print(tmp_dict)
    return sorted(tmp_dict.items(), key=lambda x: x[0])


def reducer(sort_list):
    tmp_dict = dict()
    for k, v in sort_list:
        tmp_dict[k] = sum(v)
    return tmp_dict


if __name__ == '__main__':
    data = [
        (1, "To execute this mapper and associated reducer on Hadoop Streaming use the"),
        (2, "Outputs statistical aggregations per key from a striped mapper a"),
    ]

    for d in data:
        map_(d[0], d[1])

    a = shuffle(shuffle_tmp)
    b = reducer(a)
    c = sorted(b.items(), key=lambda x: x[1], reverse=True)
    print(c)
