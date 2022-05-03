
import sys

    def huffman_encoding(data):
        #establish classes
        class Node:
            def __init__(self, value):
                self.value = value
                self.right = None
                self.left = None
                self.frequency = 1

        class Queue:
            def __init__(self):
                self.head = None
                self.tail = None
                self.size = 0
                self.dict = dict()
            
            def shape(self):
                # curr = self.head
                # for i in range(len(self.dict)):
                #     print(i, curr.value, curr.frequency)
                #     curr = curr.right
                #     i+=1
                # shape = {}
                # for key in reversed(list(self.dict.keys())):
                #      node = self.dict.get(key)
                #      shape[node.value] = node.frequency
                # print(shape)

                linked_list = {}
                node = self.head
                while node:
                    linked_list[node.value] = node.frequency
                    node = node.right
                print(linked_list)
            
            
            def enqueue(self, value):
                """ Prepend a node to the beginning of the list """

                if self.head is None:
                    self.head = Node(value)
                    self.tail = self.head
                    return

                new_head = Node(value)
                new_head.right = self.head
                self.head.left = new_head
                self.head = new_head
                self.size += 1
            
            def is_empty(self):
                return self.size == 0

            def dequeue(self):
                if self.is_empty():
                    return None
                value = self.head.value          
                self.head = self.head.next       
                self.size -= 1
                return value

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
                one_previous = current_node.left
                one_next = current_node.right
                
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
                    one_next.left = one_previous
                    current_node.left = one_next
                    new_next = one_next.right
                    one_next.right = current_node
                    if new_next:
                        new_next.left = current_node
                        current_node.right = new_next
                    else:
                        self.tail = current_node
                        self.tail.right = None
                    if one_previous:
                        one_previous.right = one_next
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
                        conditions['left'] = current.left
                        left = current.left
                        conditions['right'] = current.right
                        right = current.right
                        conditions['curr_f'] = current.frequency

                    if left:
                        conditions['left_f'] = left.frequency
                    else:
                        conditions['left_f'] = 1000
                    
                    if right:
                        conditions['right_f'] = right.frequency
                    else:
                        conditions['right_f'] = 1000

                    conditions['continue'] = conditions.get('curr_f') > conditions.get('right_f')

                    return conditions
                    

                for key in reversed(list(self.dict.keys())):
                    current = self.dict.get(key)

                    cond = conditions(current)
                    cont = cond.get('continue')

                    # if current:
                    #     left = current.left
                    #     right = current.right
                    #     curr_f = current.frequency

                    # if left:
                    #     left_f = left.frequency
                    # else:
                    #     left_f = 1000
                    
                    # if right:
                    #     right_f = right.frequency
                    # else:
                    #     right_f = 1000
                            
                            
                            
                    while cont:
                        self.shift(key)
                        cond = conditions(current)
                        cont = cond.get('continue')
                        self.shape()

                #check whether the list still needs sorting
                count = 0
                for key in reversed(list(self.dict.keys())):
                    current = self.dict.get(key)
                    cond = conditions(current)
                    if cond.get('continue'):
                        count += 1
                if count > 0:
                    self.sort()


        #extract information about characters from data
        kew = Queue()
        #l_list = LinkedList()
        for letter in data:
            if kew.dict.get(letter):
                kew.dict[letter].frequency += 1
            else:
                kew.enqueue(letter)
                kew.dict[letter] = kew.head
        
        kew.shape()
        #pseudocode
        #sort the dictionary now
        kew.sort()
        #brute force method
        # kew.sort()
        # kew.sort()
        # kew.sort()
        # kew.sort()

        # kew.shape()

        #now iterate over the dictionary tocreate a tree?
        #sort the dictionary into a linked list? Pop off the list to create tree?

        return kew 

def huffman_decoding(data,tree):
    pass

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
