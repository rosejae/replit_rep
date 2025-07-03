import time
from queue import Queue

data_list = [i for i in range(100000)]

start_time = time.time()

queue = []
for data in data_list:
    queue.append(data)
while queue:
    queue.pop(0)

print(f"Elapsed time: {time.time() - start_time} seconds.")
print(queue)

start_time = time.time()

queue = Queue()
for data in data_list:
    queue.enqueue(data)
while queue.head != None:
    queue.dequeue

print(f"Elapsed time: {time.time() - start_time} seconds.")
queue.show