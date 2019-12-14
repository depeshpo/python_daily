class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        """
        Traverse across the linked list nodes and print the nodes
        """
        head = self.head
        while head:
            print(head.data)
            head = head.next

    def remove_duplicates(self):
        """
        Removes the duplicated node
        """
        head = self.head
        temp = []
        # to store the last node so that if any node after last node repeats
        # then we can jump from it to the next node of that repeating node
        prev = None
        while head:
            if head.data in temp:
                prev.next = head.next
            else:
                temp.append(head.data)
            prev = head
            head = head.next

    def reverse(self):
        prev = None
        head = self.head
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        self.head = prev


if __name__ == '__main__':

    ls = SingleLinkedList()

    node1 = Node(13)
    node2 = Node(12)
    node3 = Node(15)
    node4 = Node(12)
    node5 = Node(17)

    ls.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print("Before removing duplicates")
    ls.traverse()

    # print("After removing duplicates")
    # ls.remove_duplicates()
    # ls.traverse()

    print("After reversing")
    ls.reverse()
    ls.traverse()
