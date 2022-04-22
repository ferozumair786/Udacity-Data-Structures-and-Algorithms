#Least recently used cache.
#This has to be some kind of queue where I can add stuff kind of like a stack but then have the option to drop the bottom value
#However, how do I call something in the middle of the stack? I'd need a dictionary for that.
#If I use a dictionary AND a linked list I could keep constant time!

#Initiate Node Class
#from inspect import _Object


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

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
        self.head.previous = new_head
        self.head = new_head
        #self.tail = self.head.next


#starter code:
class LRU_Cache(object):

    def __init__(self, capacity=object):
        # Initialize class variables
        self.dict = dict()
        self.list = LinkedList()
        if capacity <= 64:
            self.cache_size = capacity
        else:
            self.cache_size = 64
            print("your cache is too big. It has been set to the max size of 64")


    def cut(self):
        """cut off the tail of the linked list"""

        tail_ = self.list.tail
        tail_key = tail_.value
        one_previous = tail_.previous

        #change tail reference
        if one_previous:
            one_previous.next = None
        self.list.tail = one_previous

        #remove tail value from dictionary
        del self.dict[tail_key]


    def move_up(self, key=0):
        """move the node from the selected key up the list. She is a """
        if len(self.dict) == 0:
            self.list.prepend(key)
            self.dict[key] = self.list.head
            return
            

        # Helper references
        if self.dict.get(key) == self.list.head:
            #print("this is a head")
            return

        current_node = self.dict.get(key)
        one_previous = current_node.previous
        one_next = current_node.next
        
        #handle neighbors
        
        #if the previous is none then that means we called the head
        if one_previous:
            one_previous.next = one_next
        #else:
         #   print(key, " has no previous")
        #if the next is none that means we called a tail
        if one_next:
            one_next.previous = one_previous
        else:
        #    print(key, " has no next")
            self.list.tail = one_previous

        #new head
        current_node.next = self.list.head
        self.list.head.previous = current_node  
        self.list.head = current_node
        
        #set head previous to none
        self.list.head.previous = None
        

    def get(self, key=None):
        """This function accepts one argument, which is a key to look up. If not provided, the function will return the most recently touched value"""

        #return top value if no argument is provided
        if key == None:
            return self.list.head.value
        
        
        # Retrieve item from provided key. Return -1 if nonexistent. 
        return_node = self.dict.get(key)
        if return_node != None:
            
            # The item searched has been touched now, it must be moved up in node
            self.move_up(key)

            # return the dictionary value
            return return_node.value
        else:
            return -1
        

    def set(self, key=0, value=0):
        """This function adds a new value in our LRU cache. The key and value are required, however the LRU can function without them provided. 
        
        It accepts two arguments, a key and a value. Either could be a string or an int or a float. The combination must be unique.
        
        Granted, the default if key or value are not provided will be 0.
        if you call the function without any arguments, it will attempt set(0,0) into the dict. 
        If you only pass one argument, then the value will be set to 0. For example, set(1) would be equivalent to set(1,0) 
        """
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.get(key) == value:
            return
        else:
            #condition for first insertion
            if len(self.dict) == 0:
                self.dict[key] = Node(value)
                self.list.head = self.dict.get(key)
                self.list.tail = self.dict.get(key)
            elif len(self.dict) < self.cache_size:
                #prepend this as the new head
                self.list.prepend(value)

                #point new dictionary entry to new head
                self.dict[key] = self.list.head
            else:
                #the len(self.dict) >= self.cache_size
                #This means we have to cut the tail
                self.cut()

                #now we can insert a new value
                self.list.prepend(value)

                #point new entry in the dictionary to head
                self.dict[key] = self.list.head

        return

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
#the value called is a tail or a head which means next or previous might be null
our_cache.get(1) 

# Test Case 2
#Value is null in set and get functions
our_cache.set()
our_cache.get()

# Test Case 3
#LRU cache is too big. Beyond like 64 items, it might not make much sense.
LRU_Cache(65)