# Step 1: Define the Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Step 2: Create the LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None

# Step 3: Implement the Append Method
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# Step 4: Implement the Display Method
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

# Step 5: Implement the Insert Method
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

# Step 6: Implement the Delete Method
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

# Step 7: Implement the Search Method
    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

# Step 8: Implement the Reverse Method
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Step 9: Implement the Find Middle Method
    def find_middle(self):
        slow = self.head  # Slow pointer for middle
        fast = self.head  # Fast pointer to find the end
        # Move slow by one step and fast by two steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None  # Return the middle data

# Step 10: Implement the Has Cycle Method
    def has_cycle(self):
        slow = self.head  # Slow pointer for cycle detection
        fast = self.head  # Fast pointer for cycle detection
        # Use two pointers to determine if there is a cycle
        while fast and fast.next:
            slow = slow.next  # Move slow by one step
            fast = fast.next.next  # Move fast by two steps
            if slow == fast:  # If they meet, there is a cycle
                return True
        return False  # If no cycle is found

# Step 11: Implement the Remove Duplicates Method
    def remove_duplicates(self):
        if not self.head:
            return  # If the list is empty, return
        current = self.head
        seen = set([current.data])  # Initialize the set with the first element
        # Traverse the linked list to remove duplicates
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next  # Skip the duplicate
            else:
                seen.add(current.next.data)  # Add to the set
                current = current.next  # Move to the next node

# Step 12: Implement the Merge Method
    def merge(self, other):
        # If the current list is empty, return the other list's head
        if not self.head:
            return other.head
        # If the other list is empty, return the current list's head
        if not other.head:
            return self.head

        # Create a new linked list to hold the merged result
        merged_list = LinkedList()
        
        # Start merging the lists
        current1 = self.head
        current2 = other.head

        # Initialize the head of the merged list
        if current1.data < current2.data:
            merged_list.head = current1  # Set the smaller head
            current1 = current1.next
        else:
            merged_list.head = current2  # Set the smaller head
            current2 = current2.next
        
        current_merged = merged_list.head

        # Merge the two lists
        while current1 and current2:
            if current1.data < current2.data:
                current_merged.next = current1  # Append the smaller node
                current1 = current1.next
            else:
                current_merged.next = current2  # Append the smaller node
                current2 = current2.next
            current_merged = current_merged.next  # Move to the next position in merged list

        # Attach any remaining elements from either list
        if current1:
            current_merged.next = current1  # Append remaining nodes from current1
        elif current2:
            current_merged.next = current2  # Append remaining nodes from current2

        return merged_list  # Return the merged list

# Testing the methods
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # Output: 1 -> 2 -> 3

ll.insert(4, 1)
ll.display()  # Output: 1 -> 4 -> 2 -> 3

ll.delete(2)
ll.display()  # Output: 1 -> 4 -> 3

print("Search for 4:", ll.search(4))  # Output: 1
print("Search for 5:", ll.search(5))  # Output: -1

ll.reverse()
ll.display()  # Output: 3 -> 4 -> 1

print("Middle element:", ll.find_middle())  # Output: 4

# Testing the has_cycle method
# Creating a cycle manually by linking the last node to the second node
ll.head.next.next.next = ll.head.next

print("Has cycle:", ll.has_cycle())  # Output: True

# Reset the list without a cycle for testing
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print("Has cycle:", ll.has_cycle())  # Output: False

# Testing the remove_duplicates method
ll_with_duplicates = LinkedList()
ll_with_duplicates.append(1)
ll_with_duplicates.append(2)
ll_with_duplicates.append(2)
ll_with_duplicates.append(3)
ll_with_duplicates.append(3)
ll_with_duplicates.append(4)
print("Before removing duplicates:")
ll_with_duplicates.display()  # Output: 1 -> 2 -> 2 -> 3 -> 3 -> 4

ll_with_duplicates.remove_duplicates()
print("After removing duplicates:")
ll_with_duplicates.display()  # Output: 1 -> 2 -> 3 -> 4

# Testing the merge method
ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)
print("List 1:")
ll1.display()  # Output: 1 -> 3 -> 5

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)
print("List 2:")
ll2.display()  # Output: 2 -> 4 -> 6

merged_list = ll1.merge(ll2)
print("Merged List:")
merged_list.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6

