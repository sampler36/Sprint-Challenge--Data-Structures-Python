class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

# to append an item 
# have to compare the capacity first 
# then if the capacity dont fit basically make a new one
# else have to check the storage if it can hold the new item
  def append(self, item):
    # we can overwrite the current item / 
    # maybe init it to the new elem
    self.storage[self.current] = item
    # check if current is less than capacity -1
    if self.current < self.capacity -1:   # O(n)
      # if true then increment the current value by 1
      self.current += 1
      # else just reset the index to 0
    else:
      self.current = 0
  
  def get(self):
    # setting the empty buffer
    buffer = []
    # if storage in not none
    if self.storage != None:   # O(n)
      # loop thru
      for i in self.storage:   
        if i != None:
          # then append
          buffer.append(i)
    # print and return everythin gn the buffer /  array
    print(buffer)      
    return buffer
    