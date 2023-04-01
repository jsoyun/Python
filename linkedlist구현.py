# append구현. 중요한것은 정확한 구동원리를 이해하는 것
class LinkedList(object):
    def _init_(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is Node:
            self.head = new_node
        # 맨 뒤의 node가 new_node를 가리켜야한다.
        else:
            current = self.head
            while (current.next):
                current = current.next
            current.next = new_node
