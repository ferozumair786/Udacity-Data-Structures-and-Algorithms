import hashlib

from datetime import datetime, timezone

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.previous = None
    
    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()
# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

class Blockchain:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def link(self,data):
        if data == None:
            return None
        if self.size > 98:
            error = "The blockchain is too damn long!"
            print(error)
            return None

        
        date = datetime.now(timezone.utc)
        timestamp = date.strftime("%H:%M:%S, %m/%d/%Y")
        
        if self.size == 0 or self.head == None:
            previous_hash = 0
            newhead = Block(timestamp, data, previous_hash)
            self.head = newhead
            self.tail = newhead
            self.size += 1
        else:
            head = self.head
            previous_hash = head.hash
            newhead = Block(timestamp, data, previous_hash)
            newhead.previous = head
            self.head = newhead
            self.size += 1

    def print_bchain(self):
        block = self.head
        
        while block != None:
            print("Timestamp: ",block.timestamp)
            print("Data: ", block.data)
            print("SHA256 Hash: ", block.hash)
            print("Previous Hash: ", block.previous_hash)
            print("V")
            print("_________________________________________")
            block = block.previous


# Test Case 1
# empty data
bchain = Blockchain()
bchain.link("This is the first block")
bchain.link("this is the second block")
bchain.link()

# Test Case 2
# print blockchain
bchain.print_bchain()

# Test Case 3
# blockchain too long
for i in range(100):
    bchain.link(i)
print("bchain size: ", bchain.size)