# coding: utf-8

import multiprocessing
import time

def fader():
    while 1:
        for i in range(10):
            print "fading light to intensity", i
            time.sleep(0.5)
        for i in range(10, 0, -1):
            print "fading light to intensity", i
            time.sleep(0.5)
        time.sleep(5)

def light_on():
    while 1:
        print "light is on"
        time.sleep(1)

	
def light_out():
    print "light switch turned off"

class Scheduler(object):
    def __init__(self):
        self.current_process = None

    def run_process(self, process):
        if self.current_process is not None:
            self.current_process.terminate()

        self.current_process = multiprocessing.Process(target=process)
        self.current_process.start()

    def shutdown(self):
        if self.current_process is not None:
            self.current_process.terminate()

def main():
    processes = [light_on, light_out, fader]
    scheduler = Scheduler()

    try:
        while 1:
            print
            print "Which process do you want to run?"
            for idx, process in enumerate(processes):
                print idx, "for process", process
            choice = None
            while choice is None:
                try:
                    choice = int(raw_input())
                except ValueError:
                    print "invalid input"
                if choice not in range(len(processes)):
                    print "invalid input, enter a number between 0 and", len(processes)
                    choice = None

            process = processes[choice]
            scheduler.run_process(process)
    finally:
        scheduler.shutdown()

if __name__ == "__main__":
    main()
