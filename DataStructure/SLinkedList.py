class Node:
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def __str__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append(None)
        return '->'.join([str(data) for data in nodes])
    

    def append(self, data) -> None:
        node = Node(data)
        current =  self.head
        while current.next is not None:
            current =  current.next
        current.next = node


    def push(self, data) -> None:
        node = Node(data)
        node.next = self.head
        self.head = node
        

list = SLinkedList()
list.head = Node(1)
list.append(4)
list.push(2)
print(list)
