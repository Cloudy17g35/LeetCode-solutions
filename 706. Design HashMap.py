class MyHashMap:

    def __init__(self):
        self.container = []
        

    def put(self, key: int, value: int) -> None:
        
        found = False
        for element in self.container:
            k, v = element[0], element[1]
            if k == key:
                element[1] = value
                found = True
        if not found:
            self.container.append([key, value])
    
    def get(self, key: int) -> int:
        for element in self.container:
            k, v = element[0], element[1]
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        for i, element in enumerate(self.container):
            k, v = element[0], element[1]
            if k == key:
                self.container = self.container[:i] + self.container[i + 1:]
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
