# prep DS-Algo
class MyStack():

    def __init__(self):
        self.data = []

    # lenght
    # is_full:
    # push
    # pop

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self.data) == 5:
            return True
        else:
            return False

    def push(self, element):
        if self.is_full():
            raise Exception('overflow')
        else:
            self.data.append(element)

    def pop(self):
        if self.is_empty():
            raise Exception('underflow')
        else:
            return self.data.pop()


if __name__ == '__main__':
    mystack = MyStack()
    mystack.push(1)
    mystack.push(2)
    mystack.push(1)
    mystack.push(2)
    mystack.push(1)
    mystack.push(2)

    print(mystack.pop())
    print(mystack.pop())