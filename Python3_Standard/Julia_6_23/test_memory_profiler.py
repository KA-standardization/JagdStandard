@profile
def foo():
    for i in range(100):
        i += 1


@profile
def bar():
    with profile.timestamp("calculate_output"):
        for j in range(10000):
            j += 1
            for k in range(1000000):
                k += 1


if __name__ == '__main__':
    bar()
