import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking stock for {item}...")
    time.sleep(2)
    print(f"{item} is in stock!")
    return True

async def main():
    items = ["tea", "milk", "sugar"]

    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as executor:
        tasks = [
            loop.run_in_executor(executor, check_stock, item)
            for item in items
        ]
        await asyncio.gather(*tasks)

asyncio.run(main())
# let me explain what this code does. It defines a function check_stock that simulates checking the stock of an item by sleeping for 2 seconds. The main function creates a list of items and uses a ThreadPoolExecutor to run the check_stock function for each item in a separate thread. The loop.run_in_executor method is used to submit the check_stock function to the executor, and asyncio.gather is used to wait for all the tasks to complete. Finally, asyncio.run is called to execute the main function.
#let me explain in more detail. The check_stock function is a synchronous function that simulates a time-consuming operation by sleeping for 2 seconds. The main function is an asynchronous function that creates a list of items and uses a ThreadPoolExecutor to run the check_stock function for each item in a separate thread. The loop.run_in_executor method is used to submit the check_stock function to the executor, which allows it to run concurrently with other tasks. The asyncio.gather function is used to wait for all the tasks to complete before proceeding. Finally, asyncio.run is called to execute the main function, which starts the event loop and runs the asynchronous code.