import asyncio
from concurrent.futures import ThreadPoolExecutor
import time

def encrypt_data(data):
    print(f"Encrypting data: {data}")
    time.sleep(2)
    encrypted = data[::-1]  # simple encryption by reversing the string
    print(f"Encrypted data: {encrypted}")
    return encrypted

async def main():
    data = "Hello, World!"
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as executor:
        encrypted_data = await loop.run_in_executor(executor, encrypt_data, data)
        print(f"Encrypted data received in main: {encrypted_data}")
        
asyncio.run(main())
# let me explain what this code does. It defines a function encrypt_data that simulates encrypting data by sleeping for 2 seconds and then reversing the string. The main function is an asynchronous function that uses a ThreadPoolExecutor to run the encrypt_data function in a separate thread. The loop.run_in_executor method is used to submit the encrypt_data function to the executor, which allows it to run concurrently with other tasks. Finally, asyncio.run is called to execute the main function, which starts the event loop and runs the asynchronous code. 
# let me explain in more detail. The encrypt_data function is a synchronous function that simulates a time-consuming operation by sleeping for 2 seconds. The main function is an asynchronous function that uses a ThreadPoolExecutor to run the encrypt_data function in a separate thread. The loop.run_in_executor method is used to submit the encrypt_data function to the executor, which allows it to run concurrently with other tasks. The await keyword is used to wait for the result of the encrypt_data function before proceeding. Finally, asyncio.run is called to execute the main function, which starts the event loop and runs the asynchronous code.