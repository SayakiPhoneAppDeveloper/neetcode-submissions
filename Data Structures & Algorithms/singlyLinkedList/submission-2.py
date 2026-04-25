class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.value
            i += 1
            curr = curr.next
        return -1
        

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        
        curr = self.head
        i = 0
        while curr and i < index - 1:
            i += 1
            curr = curr.next

        if curr and curr.next:
            curr.next = curr.next.next
            return True
        return False


    def getValues(self) -> List[int]:
        curr = self.head
        res = []
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res