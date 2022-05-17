import string
import itertools
import collections
import multiprocessing


class SimpleMapReduce:

    def __init__(self, map_func, reduce_func, num_workers=None):
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_workers)

    def partition(self, mapped_values):
        partitioned_data = collections.defaultdict(list)
        for k, v in mapped_values:
            partitioned_data[k].append(v)
        return partitioned_data.items()

    def __call__(self, inputs, chunksize=1):
        map_responses = self.pool.map(self.map_func, inputs, chunksize=chunksize)
        partitioned_data = self.partition(itertools.chain(*map_responses))
        reduced_values = self.pool.map(self.reduce_func, partitioned_data)
        return reduced_values


def file_to_words(filename):
    STOP_WORDS = set([
        'a', 'an', 'and', 'are', 'as', 'be', 'by', 'for', 'if',
        'in', 'is', 'it', 'of', 'or', 'py', 'rst', 'that', 'the',
        'to', 'with',
    ])
    TR = str.maketrans({p: ' ' for p in string.punctuation})
    print('{} reading {}'.format(multiprocessing.current_process().name, filename))
    output = []
    with open(filename, 'rt') as f:
        for line in f:
            if line.lstrip().startswith('..'):
                continue
            line = line.translate(TR)
            for word in line.split():
                word = word.lower()
                if word.isalpha() and word not in STOP_WORDS:
                    output.append((word, 1))
    return output


def count_words(item):
    word, occurences = item
    return (word, sum(occurences))


if __name__ == '__main__':
    import glob
    import operator

    input_file = glob.glob('../main.py')
    print(input_file)

    mapper = SimpleMapReduce(file_to_words, count_words)
    word_counts = mapper(input_file)
    word_counts.sort(key=operator.itemgetter(1))
    word_counts.reverse()

    top20 = word_counts[:20]
    longest = max(len(word) for word, count in top20)
    for word, count in top20:
        print('{word:<{len}}: {count:5}'.format(len=longest + 1, word=word, count=count))
