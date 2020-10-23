# prep DS-Algo
class MyQueue():
    def __init__(self):
        self.data = []

    def is_full(self):
        if len(self.data) == 5:
            return True
        else:
            return False

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def enqueue(self, element):
        if self.is_full():
            raise Exception('overflow')
        else:
            self.data.append(element)

    def dequeue(self):
        if self.is_empty():
            raise Exception('underflow')
        else:
            return self.data.pop(0)


if __name__ == '__main__':
    myqueue = MyQueue()
    myqueue.enqueue(100)
    myqueue.enqueue(200)
    print(myqueue.dequeue())
    print(myqueue.dequeue())