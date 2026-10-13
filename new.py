class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Create Linked List
    def create(self, n):
        for i in range(n):
            data = int(input("Enter node value: "))
            self.append(data)

    # Insert node at a specific position
    def insert(self, data, pos):
        newnode = Node(data)

        if pos == 1:
            newnode.next = self.head
            self.head = newnode
            return

        temp = self.head
        for i in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        newnode.next = temp.next
        temp.next = newnode

    # Append node
    def append(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newnode

    # Traverse and print node values
    def display(self):
        temp = self.head

        if temp is None:
            print("Linked List is empty")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # Find middle node
    def middle(self):
        slow = self.head
        fast = self.head

        if self.head is None:
            print("Linked List is empty")
            return

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle node:", slow.data)

    # Delete node at a specific position
    def delete(self, pos):
        if self.head is None:
            print("Linked List is empty")
            return

        if pos == 1:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(pos - 2):
            if temp.next is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next

    # Reverse linked list
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode

        self.head = prev

    # Sum every two consecutive node values
    def consecutive_sum(self):
        temp = self.head

        if temp is None or temp.next is None:
            print("Not enough nodes to calculate consecutive sums")
            return

        while temp and temp.next:
            print(temp.data + temp.next.data, end=" ")
            temp = temp.next

        print()


# Main program
ll = LinkedList()

while True:
    print("\n--- Singly Linked List Menu ---")
    print("1. Create Linked List")
    print("2. Display Linked List")
    print("3. Insert Node")
    print("4. Find Middle Node")
    print("5. Delete Node")
    print("6. Reverse Linked List")
    print("7. Sum Consecutive Nodes")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("How many nodes? "))
        ll.create(n)

    elif choice == 2:
        ll.display()

    elif choice == 3:
        data = int(input("Enter value: "))
        pos = int(input("Enter position: "))
        ll.insert(data, pos)

    elif choice == 4:
        ll.middle()

    elif choice == 5:
        pos = int(input("Enter position to delete: "))
        ll.delete(pos)

    elif choice == 6:
        ll.reverse()
        print("Linked List reversed successfully")

    elif choice == 7:
        ll.consecutive_sum()

    elif choice == 8:
        print("Program terminated")
        break

    else:
        print("Invalid choice")