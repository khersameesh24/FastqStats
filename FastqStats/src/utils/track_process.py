import time
import os
import psutil


def elapsed_since(start):
    return time.strftime("%H:%M:%S", time.gmtime(time.time() - start))


def get_process_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss


def track(func):
    def wrapper(*args, **kwargs):
        mem_before = get_process_memory()
        start = time.time()
        result = func(*args, **kwargs)
        elapsed_time = elapsed_since(start)
        mem_after = get_process_memory()
        # print("\n{}: Memory usage before: {:.2f} MB, after: {:.2f} MB, consumed: {:.2f} MB; exec time: {}".format(
        #     func.__name__.title(),
        #     (mem_before/(1024*1024)),
        #     (mem_after/(1024*1024)),
        #     (mem_after/(1024*1024) - mem_before/(1024*1024)),
        #     elapsed_time))
        return result
    return wrapper
