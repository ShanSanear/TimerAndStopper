import time


def timer(seconds, granularity):
    remaining = seconds
    while remaining > 0:
        time.sleep(granularity)
        print("Remaining: {:.2f}".format(remaining))
        remaining -= granularity


if __name__ == '__main__':
    start = time.time()
    timer(10, 0.5)
    print(f"It took {time.time() - start} seconds")
