"""
Killing a worker with using multiprocessing instead of threading. You can kill
processed on Windows and Unix. Using processes instead of threads is thus a
good option if you need to terminate your workers.

The only downside is that it's harder to exchange data. Using threads you would
use Queue.Queue. For multiprocessing see this section in the docs:

https://docs.python.org/2/library/multiprocessing.html#sharing-state-between-processes
"""

import multiprocessing
import time

def worker():
    # this in run in a separate process and can be safely terminated.
    while 1:
        print "doing work in worker"
        time.sleep(1)

def main():
    process = multiprocessing.Process(target=worker)
    process.start()

    # kill subprocess after 5 seconds
    time.sleep(5)

    process.terminate()

if __name__ == "__main__":
    main()
