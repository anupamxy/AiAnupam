# gil in python
# example of how to use gil in python
import threading
import time

def task1():
    for i in range(5):
        print("Task 1")
        time.sleep(1)
        
        

 