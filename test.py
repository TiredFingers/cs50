import time

test = [i for i in range(100000000)]


def calc_time(f):

    def wraper(*args):
        starttime = time.process_time_ns()
        f(*args)
        endtime = time.process_time_ns()
        print(endtime - starttime)

    return wraper


@calc_time
def test_pop(t):
    t.pop(-1)
    print('pop')


@calc_time
def test_slice(t):

    data = t[-1]
    t = t[:-1]
    print('slice')


for i in range(10):
    test_slice(test)



#print(test_pop(test))
#print(test_slice(test))


