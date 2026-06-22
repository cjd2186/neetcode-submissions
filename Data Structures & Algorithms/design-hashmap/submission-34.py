class MyHashMap:

    def __init__(self):
        self.hashMap = []  

    def put(self, key: int, value: int) -> None:            
        for i in range(0, len(self.hashMap)):
            if key == self.hashMap[i][0]:
                self.hashMap[i] = [key, value]
                return
        self.hashMap.append([key,value])
    
    def get(self, key: int) -> int:
        for i in range(0, len(self.hashMap)):
            if key == self.hashMap[i][0]:
                return self.hashMap[i][1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(0, len(self.hashMap)):
            if key == self.hashMap[i][0]:
                self.hashMap.pop(i)
                return None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)