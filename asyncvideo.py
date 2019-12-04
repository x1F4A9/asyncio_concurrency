#aiohttp for webservers
import asyncio

#standard
def find_divisibles(inrange, div_by):
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i% div_by == 0:
            located.append(i)
    print("done with nums in range {} divisible by {}".format(inrange, div_by))

#coroutine
async def find_divisibles_async(inrange, div_by):
    #bulk task -- this is still syncronous
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i% div_by == 0:
            located.append(i)
        #causes a momentary hang
        #lets other processes _RUN_ before the long process
        #makes a VERY small pause
        if i % 500000 == 0:
            await asyncio.sleep(0.00001)
    print("done with nums in range {} divisible by {}".format(inrange, div_by))

#standard
def main():
    divs1 = find_divisibles(5080000, 34133)
    divs2 = find_divisibles(100052, 3210)
    divs3 = find_divisibles(500, 3)

#async
async def main_async():
    #adds variables to loop
    #function MUST be declared with async def otherwise you will get an AssertionError
    divs1 = loop.create_task(find_divisibles_async(508000, 34133))
    divs2 = loop.create_task(find_divisibles_async(100052, 3210))
    divs3 = loop.create_task(find_divisibles_async(500, 3))
    #need to WAIT for batches otherwise we fire off hundreds or thousands of coroutines
    #always necessary
    #waits for coroutines to run and return
    #still _hangs_ with the async.io
    await asyncio.wait([divs1, divs2, divs3])
#establish main loop
#add in tasks


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        #run main coroutine until task is complete
        loop.run_until_complete(main_async())
        #uncomment for syncio
        #maybe unnecessary
        loop.close()
    except Exception as e:
        #logging
        pass
    finally:
        #always close the loop
        loop.close()
    #main()

