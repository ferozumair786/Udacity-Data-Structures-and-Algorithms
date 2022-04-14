#Least recently used cache.
#This has to be some kind of queue where I can add stuff kind of like a stack but then have the option to drop the bottom value
#However, how do I call something in the middle of the stack? I'd need a dictionary for that.
#If I use a dictionary AND a linked list I could keep constant time!

#Initiate Node Class
from inspect import _Object


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def prepend(self, value):
        """ Prepend a node to the beginning of the list """

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        
    def append(self, value):
        """ Append a node to the tail of the list """

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        new_tail = Node(value)
        self.tail.next = new_tail
        self.tail = new_tail


#starter code:
class LRU_Cache(object):

    def __init__(self, capacity=object):
        # Initialize class variables
        self.dict = dict()
        self.cache_size = capacity
        self.list = LinkedList()


        

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.dict.get(key) != None:
            return self.dict.get(key)
        else:
            return -1
        
        # The item searched has been touched now, it must be moved up in node


    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.get(key) == value:
            return
        else:
            #condition for first insertion
            if len(self.dict) == 0:
                self.list.head = Node(value)
                self.dict[key] = self.list.head
            elif len(self.dict) < self.cache_size:
                new_value = Node(value)
                #set the new key in the dictionary to this node
                #prepend this as the new head
                #add reference of new head to dictionary'
            else:
                #the len(self.dict) >= self.cache_size
                #This means we have to drop the smallest number
