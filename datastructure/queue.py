class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
            
    @property
    def dequeue(self):
        if self.head == None:
            return None

        data = self.head.data
        self.head = self.head.next
        return data

    @property
    def show(self):
        cur = self.head
        if not cur:
            return print([])
        while cur:
            print(f'{cur.data}', end=' ')
            cur = cur.next

if __name__ == '__main__':
    import random
    
    queue = Queue()

    n = int(input())
    data_list = [random.randint(1, 9) for _ in range(n)]

    for data in data_list:
        queue.enqueue(data)

    queue.show

    print('\n')
    [print(f'queue dequeue: {queue.dequeue}') for _ in range(n)]