"""
Interrupting a thread with threading.Event().
"""

import threading
import time

WAIT_INTERVAL = 10 # seconds

def worker(stop_event):
    while 1:
        print "doing some work in worker"
        if stop_event.wait(WAIT_INTERVAL):
            print "received stop event!"
            break

def main():
    t0 = time.time()
    stop_event = threading.Event()
    thread = threading.Thread(target=worker, args=(stop_event,))
    thread.start()

    # send stop event after 3 seconds
    time.sleep(3)
    stop_event.set()

    # wait until worker thread is done
    thread.join()

    # calculate time elapsed
    elapsed = time.time() - t0

    # proof that we could interrupt the thread
    assert elapsed < WAIT_INTERVAL

if __name__ == "__main__":
    main()
