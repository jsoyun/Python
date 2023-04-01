# get연산자
class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, value):
        pass

    def get(self, idx):  # 몇번째 인덱스값으로 가져올건지
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

# 시간 복잡도 빅0 n.


# insert_at(idx,value)
# 이거 아님~ 다시 해~
class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, value):
        pass

    def insert_at(idx, value):  # 몇번째 인덱스값으로 가져올건지

        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

# insert_back tail version


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = Nond

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 맨 뒤의 node가 new_node를 가리켜야한다.
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
