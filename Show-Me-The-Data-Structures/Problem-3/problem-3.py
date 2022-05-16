
import sys


class Node:
    def __init__(self, value, frequency):
        self.value = value
        self.right = None
        self.left = None
        self.frequency = frequency
        self.code = None
        self.parent = None
        self.next = None
        self.previous = None

    def left_(self, node):
        if type(node) != Node and node != None:
            print('this function only accepts Nodes or None')
            return None
        node.parent = self
        self.left = node
        node.code = '0'
        print("left node:", node.value)

    def right_(self, node):
        if type(node) != Node and node != None:
            print('this function only accepts Nodes or None')
            return None
        node.parent = self
        self.right = node
        node.code = '1'
        print("right node:", node.value)

    def leaf(self, newnode):
        existing_node = None
        # print("existing_node: none")
        #There should really only be one existing node
        if self.left:
            # print("passes self.left")
            existing_node = self.left
        elif self.right:
            # print("passes self.right")
            existing_node = self.right
        
        if existing_node:
            # print("existing node")

            if type(existing_node.value) == int:
                value = existing_node.value
            else:
                value = existing_node.frequency
            
            if newnode.frequency > value:
                self.right_(newnode)
                # huffman_tree.head.right.code = huffman_tree.head.code + '1'
                self.left_(existing_node)
                # huffman_tree.head.left.code = huffman_tree.head.code + '0'
            else:
                self.left_(newnode)
                # huffman_tree.head.left.code = huffman_tree.head.code + '0'
                self.right_(existing_node)
                # huffman_tree.head.right.code = huffman_tree.head.code + '1'
        else:
            # print("no existing node")
            self.left_(newnode)
            

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.dict = dict()
    
    def shape(self):

        linked_list = {}
        node = self.head
        while node:
            linked_list[node.value] = node.frequency
            node = node.next
        print(linked_list)
    
    
    def enqueue(self, value, frequency = 1):
        """ Prepend a node to the beginning of the list """

        if self.head is None:
            self.head = Node(value, frequency)
            self.tail = self.head
            self.size += 1
            self.dict[value] = self.head
            self.head.next = None
            self.head.previous = None
            # self.frequency = frequency
            print("enqueued value for no head:", self.head.value)
            return

        new_head = Node(value, frequency)
        new_head.next = self.head
        self.head.previous = new_head
        self.head = new_head
        self.size += 1
        # self.frequency = frequency

        self.dict[value] = self.head
        print("enqueued value:", self.head.value)
        return
    
    def is_empty(self):
        return self.size <= 0

    def dequeue(self):
        if self.is_empty():
            return None
        self.size -= 1
        if self.is_empty():
            #this means we just dequeued the last item
            head_ = self.head
            self.head = None
            self.tail = None
            value = head_.value
            print("dequeued value:",value)
            return head_
        else:
            head_ = self.head  
            value = head_.value        
            self.head = head_.next       
            
            print("dequeued value:",value)
            return head_

    def shift(self, key):
        """Shift the node left or right based on whether it is greater than it's neighbors"""
        if len(self.dict) == 0:
            self.enqueue(key)
            self.dict[key] = self.head
            return
            

        # Helper references
        #if self.dict.get(key) == self.head:
            #print("this is a head")
        #    return

        current_node = self.dict.get(key)
        one_previous = current_node.previous
        one_next = current_node.next
        
        # #handle neighbors
        # shift = False
        # #if the previous is none then that means we called the head
        # if one_previous and current_node.frequency > one_previous.frequency:
        #         shift = True
            
        #     #one_previous.right = one_next
        # #else:
        # #   print(key, " has no previous")
        # #if the next is none that means we called a tail
        # if one_next and current_node.frequency > one_next.frequency:
        #         shift = True


    
        if one_next:
            one_next.previous = one_previous
            current_node.previous = one_next
            new_next = one_next.next
            one_next.next = current_node
            if new_next:
                new_next.previous = current_node
                current_node.next = new_next
            else:
                self.tail = current_node
                self.tail.next = None
            if one_previous:
                one_previous.next = one_next
            else:
                self.head = one_next


        #new head
        # current_node.right = self.head
        # self.head.left = current_node  
        # self.head = current_node
        
        #set head previous to none
        # self.head.left = None
        
    def sort(self):
        '''brute force sort method that just shifts nodes to the right until the list is sorted'''

        def conditions(current):
            conditions = dict()
            conditions['current'] = current
            if current:
                conditions['left'] = current.previous 
                left = current.previous
                conditions['right'] = current.next
                right = current.next
                conditions['curr_f'] = current.frequency

                conditions['curr_children'] = current.right or current.left
                    

            if left:
                conditions['left_f'] = left.frequency
                conditions['left_children'] = left.right or left.left
            else:
                conditions['left_f'] = 1000

            
            if right:
                conditions['right_f'] = right.frequency
                conditions['right_children'] = right.right or right.left
            else:
                conditions['right_f'] = 1000

            conditions['continue'] = conditions.get('curr_f') > conditions.get('right_f')

            #the whole point of this below condition is to give it one last move to the right in case...
            #...we have two nodes that have the same values but one already has children
            if conditions.get('continue') == False and conditions.get('curr_f') == conditions.get('right_f'):
                if conditions.get('curr_children') and conditions.get('right_children') != True:
                    conditions['continue'] = True


            return conditions
            

        for key in reversed(list(self.dict.keys())):
            current = self.dict.get(key)

            cond = conditions(current)
            cont = cond.get('continue')
                    
            while cont:
                self.shift(key)
                cond = conditions(current)
                cont = cond.get('continue')
                # self.shape()

        #check whether the list still needs sorting
        count = 0
        for key in reversed(list(self.dict.keys())):
            current = self.dict.get(key)
            cond = conditions(current)
            if cond.get('continue'):
                count += 1
        if count > 0:
            self.sort()
    
    def code(self, value):
        n = self.dict.get(value)
        cd = None
        while n.code:
            # print("Node value: ", n.value)
            if cd == None:
                cd = n.code
            else:
                cd = cd + n.code
            ch = n
            n = n.parent

        #append an extra character at the end of the last two node to prevent prefixing
        if ch == n.right:
            cd = cd + '0'
        elif ch == n.left:
            cd = cd + '1'
        # print("the cumulative code is: ", cd)
        return cd


        

def huffman_encoding(data):
    #establish classes
    print("------------------------Begin step 1: build a sorted linked list from the word----------------------------------------------")
    #STEP1: extract information about characters from data
    kew = Queue()
    #l_list = LinkedList()
    for letter in data:
        if kew.dict.get(letter):
            kew.dict[letter].frequency += 1
        else:
            kew.enqueue(letter)

    print("Unsorted list:")
    kew.shape()
    print("----------------------------------------------End of step 1-------------------------------------------------------------------")  

    print("----------------------------------------------Begin step 2: sort linked list--------------------------------------------------")  
        
    #STEP2: Sort by frequency
    #sort the dictionary now
    print("Sorted link list in order of frequency")
    kew.sort()
    kew.shape()
    print("----------------------------------------------End of step 2-------------------------------------------------------------------")  


    print("-----------------------------------Begin step 3: build Huffman tree-----------------------------------------------------------")
    #STEP3: CREATE HUFFMAN TREE
    # print("kew size:", kew.size)
    head = kew.dequeue()
    # print("kew size:", kew.size)
    newnode = kew.dequeue()
    # print("kew size:", kew.size)
    frequency = head.frequency + newnode.frequency
    kew.enqueue(frequency, frequency)
    # print("huff head left, right", huff.head.left, huff.head.right)
    kew.head.leaf(head)
    kew.head.leaf(newnode)
    # print("huff head left, right", kew.head.left.value, kew.head.right.value)
    while kew.size > 1:
        kew.sort()
        kew.shape()
        head = kew.dequeue()
        # print("huff deque remainder", huff.head, huff.head)
        # print("Head Value:", head.value)
        # print("head left, right", head.left, head.right)
        newnode = kew.dequeue()
        newnode2 = None
        # print("NewNode Valuee:", newnode.value)
        # print("kew size:", kew.size)
        if newnode2:
            frequency = newnode.frequency + newnode2.frequency
            kew.enqueue(frequency, frequency)
            kew.head.leaf(newnode)
            kew.head.leaf(newnode2)
            newnode = kew.dequeue()
            frequency = head.frequency + newnode.frequency
            kew.enqueue(frequency, frequency)
        else:
            frequency = head.frequency + newnode.frequency
            kew.enqueue(frequency, frequency)
        # print("enqueue head left, right", huff.head.left, huff.head.right)
        kew.head.leaf(head)
        kew.head.leaf(newnode)

    #Make it easy to encode by capturing all the codes in a dictionary
    codes = {}
    for key in reversed(list(kew.dict.keys())):
        
        if type(key) != int:
            #if statement reduces the number of loops
            # print("This is the path for key:", key)
            codes[key] = kew.code(key)
    
    #BRUTE FORCE ALERT: fix the codes when a code is a prefix of another code
    c = codes
    for key in c:
        prefix = c.get(key)
        for letter in c:
            fix = c.get(letter)
            if prefix == fix:
                continue
            if prefix == fix[0:len(prefix)]:
                # print("hit", prefix, fix)
                first = fix[0]
                if first == '0':
                    first = '1'
                else:
                    first = '0'
                new = first + fix
                c[letter] = new
    print("codes:", c)
    print("----------------------------------------------End of step 3-------------------------------------------------------------------")  

    print("-------------------------------------------Begin step 4: Encode Data!---------------------------------------------------------")  
    #STEP4: ENCODE DATA
    encoded = None
    for letter in data:
        if encoded:
            encoded = encoded + c.get(letter)
        else:
            encoded = c.get(letter)
        
    print("encoded data: ", encoded)
    print("----------------------------------------------End of step4-------------------------------------------------------------------") 
    print("----------------------------------------------Encoding Complete!-------------------------------------------------------------------")   
    return encoded, c

def huffman_decoding(data, tree):
    
    print("--------------------------------Begin Step 1: build the rosetta stone for decrypting-----------------------------------------------")
    rosetta_stone = {}
    for key in tree:
        value = tree.get(key)
        rosetta_stone[value] = key

    print("Rosetta Stone: ", rosetta_stone)
    print("----------------------------------------End of Step 1-------------------------------------------------------------------------------")
    

    print("----------------------------------Begin Step 2: decrypt the data--------------------------------------------------------------------")
    
    encrypted = data
    decrypted = ''
    sub_l = 2
    
    while len(encrypted) >= sub_l:
        print(encrypted[0:sub_l])
        key = rosetta_stone.get(encrypted[0:sub_l])
        if key:
            decrypted = decrypted + key
            encrypted = encrypted[sub_l:]
            sub_l = 1
        else:
            sub_l += 1
        print("decrypted: ",decrypted)
    
    print("-----------------------------------End of Step 2, The End-----------------------------------------------------------------------------------")
    
    return decrypted

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
