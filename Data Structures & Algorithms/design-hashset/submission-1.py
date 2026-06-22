class MyHashSet:

    def __init__(self):
        self.setList = []

    def add(self, key: int) -> None:
        if key in self.setList:
            return None
        self.setList.append(key)

    def remove(self, key: int) -> None:
        if key not in self.setList:
            return None
        self.setList.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.setList:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)