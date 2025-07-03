class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.is_empty():
            return None

        data = self.head.data
        self.head = self.head.next
        return data

    def top(self):
        if self.is_empty():
            None
        return self.head.data

    def show(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next

    def is_empty(self):
        return self.head is None

if __name__ == '__main__':
    stack = Stack()
    arr = [9, 7, 2, 5, 6, 4, 2]
    [stack.push(num) for num in arr]
    stack.show()
    print("\n")

    while not stack.is_empty():
        print(stack.pop())

    

