# creation of a node
class Node:
    """Represents a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

# operations of Linkedlist
class LinkedList:
    """Represents a singly linked list."""
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        """Inserts a new node at the head of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        """Inserts a new node at the tail of the linked list."""
        if not self.head:
            self.head = Node(data)
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = Node(data)

    def insert_at_position(self, data, position):
        """Inserts a new node at the specified position in the linked list."""
        if position == 0:
            self.insert_at_head(data)
            return

        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1

        if not current:
            raise ValueError("Position out of range")

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete_at_head(self):
        """Deletes the node at the head of the linked list."""
        if self.head is None:
            return
        self.head = self.head.next


    def delete_at_position(self, position):
        """Deletes the node at the specified position in the linked list."""
        if position == 0:
            self.head = self.head.next
            return

        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1

        if not current or not current.next:
            raise ValueError("Position out of range")

        current.next = current.next.next

    def delete_at_end(self):
        if self.head is None or self.head.next is None:
            return

        current = self.head
        # Traverse the list until we reach the second last node
        while current.next.next:
            current = current.next

        current.next = None

    def print_list(self):
        """Prints the elements of the linked list."""
        current = self.head
        while current:
            print(current.data, end = " -> " if current.next else "\n")
            current = current.next
        


linked_list = LinkedList()

linked_list.insert_at_tail(10)
linked_list.insert_at_tail(20)
linked_list.insert_at_tail(30)
linked_list.print_list()

linked_list.insert_at_head(5)
linked_list.print_list()

linked_list.insert_at_position(25, 2)
linked_list.print_list()

linked_list.delete_at_position(1)
linked_list.print_list()

linked_list.delete_at_head()
linked_list.print_list()

linked_list.delete_at_end()
linked_list.print_list()