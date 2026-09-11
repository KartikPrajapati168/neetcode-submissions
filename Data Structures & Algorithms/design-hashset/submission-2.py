class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        self.size = 1009
        self.buckets = [None] * self.size

    def add(self, key: int) -> None:

        index = key % self.size

        current = self.buckets[index]

        # Check if key already exists
        while current is not None:

            if current.key == key:
                return

            current = current.next

        # Create new node
        new_node = Node(key)

        # Insert at beginning
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node


    def remove(self, key: int) -> None:

        index = key % self.size

        current = self.buckets[index]
        previous = None

        while current is not None:

            if current.key == key:

                # Key is first node
                if previous is None:
                    self.buckets[index] = current.next

                # Key is middle/last node
                else:
                    previous.next = current.next

                return

            previous = current
            current = current.next


    def contains(self, key: int) -> bool:

        index = key % self.size

        current = self.buckets[index]

        while current is not None:

            if current.key == key:
                return True

            current = current.next

        return False