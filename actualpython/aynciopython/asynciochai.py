import asyncio
async def brew_chai():
    print("Boiling water...")
    await asyncio.sleep(2)
    print("Steeping the tea...")
    await asyncio.sleep(3)
    print("Pouring into cup...")
    await asyncio.sleep(1)
    print("Adding sugar and milk...")
    await asyncio.sleep(1)
    print("Chai is ready!")
    
asyncio.run(brew_chai())

# one more example
async def main():
    await brew_chai()
asyncio.run(main())
# what it basicly does is it allows us to write asynchronous code in a way that looks synchronous. It allows us to write code that can be paused and resumed, which is useful for tasks that involve waiting for something to happen, like waiting for a response from a server or waiting for a file to be read.