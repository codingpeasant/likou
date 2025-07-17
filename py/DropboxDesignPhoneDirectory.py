# https://leetcode.ca/2016-12-13-379-Design-Phone-Directory/#379-design-phone-directory
# https://github.com/insideofdrop/Dropbox-Interview-Prep/blob/main/code/allocate_id.py
# https://massivealgorithms.blogspot.com/2016/03/dropbox-interview-misc.html


class Allocator:
    def __init__(self, max_val):
        self.max_val = max_val
        self.boolSet = set()
        self.curId = 1

    def allocate(self):
        if len(self.boolSet) == self.max_val + 1:
            return -1
        self.boolSet.add(self.curId)
        self.curId += 1

        return self.curId - 1

    def release(self, id):
        """Releases the id and allows it to be allocated"""
        if (not 0 <= id < self.max_val) or (id not in self.boolSet):
            return -1
        self.boolSet.remove(id)
        self.curId = min(self.curId, id)


class SpaceEfficientAllocator:

    def __init__(self, max_val):
        self.max_val = max_val
        self.bool_array = [False] * max_val

    def allocate(self):
        """Returns an unallocated id"""
        for id, value in enumerate(self.bool_array):
            if value == False:  # The id has not been allocated
                self.bool_array[id] = True
                return id
        return -1

    def release(self, id):
        """Releases the id and allows it to be allocated"""
        if (not 0 <= id < self.max_val) or (self.bool_array[id] == True):
            return -1
        self.bool_array[id] = False


class AllocatorTree:
    def __init__(self, maxId: int):
        self.maxId = maxId
        # only create the exact number of tree nodes as needed
        self.tree = [False] * (maxId * 2 if maxId % 2 == 1 else maxId * 2 - 1)

    def getIdFromIndex(self, index: int):
        return index - len(self.tree) // 2 + 1

    def getIndexFromId(self, id: int):
        return id - 1 + len(self.tree) // 2

    def allocate(self):
        index = 0
        if self.tree[index] == True:
            return -1
        while index < len(self.tree) // 2:
            leftIndex = index * 2 + 1
            rightIndex = index * 2 + 2
            if not self.tree[leftIndex]:
                index = leftIndex
            elif rightIndex < len(self.tree) and not self.tree[rightIndex]:
                index = rightIndex
            else:
                return -1

        id = self.getIdFromIndex(index)
        self.tree[index] = True
        self.updateTree(index)
        return id

    def release(self, id: int):
        if not 1 <= id <= self.maxId:
            return -1
        index = self.getIndexFromId(id)
        if self.tree[index] == False:
            return -1
        self.tree[index] = False
        self.updateTree(index)
        return index

    def updateTree(self, index: int):
        while index > 0:
            parentIndex = index // 2 if index % 2 == 1 else (index - 1) // 2
            bothAreTrue = False
            if index % 2 == 1:
                if (
                    self.tree[index]
                    and index + 1 < len(self.tree)
                    and self.tree[index + 1]
                ) or (self.tree[index] and index + 1 == len(self.tree)):
                    bothAreTrue = True
            else:
                if self.tree[index] and self.tree[index - 1]:
                    bothAreTrue = True
            self.tree[parentIndex] = bothAreTrue
            index = parentIndex
        self.tree[0] = self.tree[1] and self.tree[2]


# a = Allocator(3)
# print(a.allocate())
# print(a.allocate())
# print(a.allocate())
# print(a.allocate())
# print(a.allocate())  # error
# a.release(2)
# assert a.release(10) == -1  # error
# print(a.allocate())  # 2

a = AllocatorTree(3)  # ids: 1,2,3
print(a.allocate())
print(a.allocate())
print(a.allocate())
print(a.allocate())  # error
a.release(2)
assert a.release(10) == -1  # error
print(a.allocate())  # 2
