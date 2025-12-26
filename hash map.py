class Hashtable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]
        self.keys = []
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char) # ord function for getting ascii value
        return hash % self.max
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if key not in self.keys:
            self.keys.append(key)
        self.arr[h] = value
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
        self.keys.remove(key)
    def __str__(self):
        hashes = []
        for key in self.keys:
            h = self.get_hash(key)
            value = self.arr[h]
            # if value is not None:
            hashes.append(f"{key}: {value}")
        return "{" + ", \n".join(hashes) + "}"

t = Hashtable()
t["fruit1"] = "apple"
t["fruit2"] = "Dragon fruit"
t["fruit3"] = "Banana"
del t["fruit3"]
print(t)
