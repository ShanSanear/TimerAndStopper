import time


def stopwatch(granulity):
    curr_time = 0
    while True:
        yield curr_time
        curr_time += granulity
        time.sleep(granulity)


if __name__ == '__main__':
    watch = stopwatch(0.1)
    for x in watch:
        print(x)
        if x > 10:
            break
