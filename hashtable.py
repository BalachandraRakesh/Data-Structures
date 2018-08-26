class hashtable:
    def __init__ (self,size):
        self.size = size
        self.hash_table = [[] for i in range(self.size)]
    def hash(self,key):
      hash_key = 0
      q = 11
      for i in range(len(key)):
          hash_key += (ord(key[i])*ord(key[i]))%q
      return hash_key
    def insert(self,key, value):
        hash_key = self.hash(key) % len(self.hash_table)
        key_exists = False
        bucket = self.hash_table[hash_key]    
        for i, kv in enumerate(bucket):
            k = kv[0]
            v = kv[1]
            if key == k:
                key_exists = True 
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))
    def exists(self, key):
      hash_key = self.hash(key) % len(self.hash_table)    
      bucket = self.hash_table[hash_key]
      for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return True
            else:
              return False
    def search(self, key):
        hash_key = self.hash(key) % len(self.hash_table)    
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v
    def delete(self, key):
        hash_key = self.hash(key) % len(self.hash_table)    
        key_exists = False
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv 
            if key == k:
                key_exists = True 
                break
        if key_exists:
            del bucket[i]
            print ('Key {} deleted'.format(key))
        else:
            print ('Key {} not found'.format(key))
    def show(self):
      print(self.hash_table)
h = hashtable(10)
h.insert('a',100)
h.insert('r',314)
h.insert('t',21)
h.insert('z',456)
h.insert('aa',100)
h.insert('hello',500)

h.show()
