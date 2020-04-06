#!/usr/bin/python3
"""
Simple implementation of LinkedList
"""
from node import Node


class LinkedList:
    # Simple implementation of LinkedList
    def __init__(self):
        # Initialize a LinkedList
        self.head = None

    def is_empty(self):
        # Check if the list is empty
        return self.head is None

    def add(self, item):
        # Add an item to the beginning of the list
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        # Return the length of the list
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        # Search for a node
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()
        return False

    def remove(self, item):
        # Remove a node from the list
        current = self.head
        previous = None
        found = False
        while not found:
            if current is None:
                print(str(item) + ' is not in the list')
                return
            elif current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head == current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        # Add an item to the end of the list
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
        temp = Node(item)
        current.set_next(temp)

    def insert(self, pos, item):
        # Add an item to the list at a specified position
        if pos < 0 or pos > self.size():
            print('Out of range')
            return
        current = self.head
        previous = None
        count = 0
        while count < pos and current is not None:
            count += 1
            previous = current
            current = current.get_next()
        if previous is None:
            self.add(item)
        temp = Node(item)
        if previous:
            previous.set_next(temp)
        temp.set_next(current)

    def index(self, item):
        # Return the position of the item in the list
        current = self.head
        pos = 0
        while current is not None:
            if current.get_data() == item:
                return pos
            else:
                current = current.get_next()
                pos += 1
        return None

    def pop(self):
        # Remove and return the last item in the list
        current = self.head
        previous = None
        if self.size() == 0:
            return None
        while current.get_next() is not None:
            previous = current
            current = current.get_next()
        if previous is None:
            self.head = None
        else:
            previous.set_next(None)
        return current.get_data()

    def __str__(self):
        # Print a linked list
        if self.head is None:
            return 'Empty list'
        current = self.head
        string = str(current.get_data())
        while current.get_next() is not None:
            current = current.get_next()
            string += ' -> ' + str(current.get_data())
        return string


if __name__ == '__main__':
    mylist = LinkedList()

    mylist.add(31)
    mylist.insert(0, 77)
    mylist.append(17)
    mylist.insert(3, 93)
    mylist.add(26)
    mylist.insert(2, 54)
    print(mylist)
    print('size is ' + str(mylist.size()))

    print('index of 31 is ' + str(mylist.index(31)))
    print('index of 77 is ' + str(mylist.index(77)))
    print('index of 17 is ' + str(mylist.index(17)))
    print('index of 93 is ' + str(mylist.index(93)))
    print('index of 26 is ' + str(mylist.index(26)))
    print('index of 54 is ' + str(mylist.index(54)))
    print('index of 100 is ' + str(mylist.index(100)))

    print('insert 95 at position 5')
    mylist.insert(5, 95)
    print(mylist)

    print('insert 50 at position 8')
    mylist.insert(8, 50)
    print(mylist)

    print('insert 50 at position 7')
    mylist.insert(7, 50)
    print(mylist)

    print('remove 54')
    mylist.remove(54)
    print(mylist)

    print('remove 100')
    mylist.remove(100)
    print(mylist)

    print(mylist.pop())
    print(mylist)
    print(mylist.pop())
    print(mylist)
    print(mylist.pop())
    print(mylist)
    print(mylist.pop())
    print(mylist)
    print(mylist.pop())
    print(mylist)
    print(mylist.pop())
    print(mylist)
    print(mylist.pop())
    print(mylist)
    print(mylist.pop())
    print(mylist)
