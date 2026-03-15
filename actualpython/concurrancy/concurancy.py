# concurrency and parallelism
# example of concurrency
import time

def task1():
    for i in range(5):
        print("Task 1")
        time.sleep(1)

def task2():
    for i in range(5):
        print("Task 2")
        time.sleep(3)
# create threads for the tasks
import threading
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)
# start the threads
thread1.start()
thread2.start()
# wait for the threads to finish
thread1.join()
thread2.join()
# example of parallelism
import multiprocessing
def task3():
    for i in range(5):
        print("Task 3")
        time.sleep(1)
def task4():
    for i in range(5):
        print("Task 4")
        time.sleep(1)
# create processes for the tasks
process1 = multiprocessing.Process(target=task3)
process2 = multiprocessing.Process(target=task4)
# start the processes
process1.start()
process2.start()
# wait for the processes to finish
process1.join()
process2.join()