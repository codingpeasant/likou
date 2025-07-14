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


class BinaryHeapAllocator:
    def __init__(self, maxId):
        self.maxId = maxId
        self.bool_array = [False] * (
            2 * maxId
        )  # if maxId is odd, the right most leaf is null

    def allocate(self):
        """Returns an unallocated id"""
        index = 0
        if self.bool_array[index] == True:  # all children are true
            return -1
        while index < self.maxId:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            if (
                self.bool_array[left_child_index] == False
            ):  # There's an unallocated id in the subtree
                index = left_child_index
            elif (
                right_child_index < len(self.bool_array)
                and self.bool_array[right_child_index] == False
            ):  # ... in the right subtree
                index = right_child_index
            else:  # Both subtrees are allocated, this actually means you broke your tree
                return -1

        id = self.get_id_from_index(index)
        self.bool_array[index] = True
        self.update_tree(index)
        return id

    def release(self, id):
        """Releases the id and allows it to be allocated"""
        if not 0 <= id <= self.maxId:
            return -1
        idx = self.get_index_from_id(id)
        if self.bool_array[idx] == False:
            return -1
        self.bool_array[idx] = False
        self.update_tree(idx)

    def get_index_from_id(self, id):  # all ids are at the leaf level
        return id + self.maxId - 1

    def get_id_from_index(self, idx):
        return idx - (self.maxId - 1)

    def update_tree(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            both_children_are_true = False
            if index % 2 == 1:  # this is a left child
                if (
                    self.bool_array[index] == True
                    and index + 1 < len(self.bool_array)
                    and self.bool_array[index + 1] == True
                ):
                    both_children_are_true = True
            else:  # this is a right child
                if self.bool_array[index] == True == self.bool_array[index - 1]:
                    both_children_are_true = True
            self.bool_array[parent_index] = both_children_are_true
            index = parent_index
        self.bool_array[0] = self.bool_array[1] and self.bool_array[2]


# a = Allocator(3)
# print(a.allocate())
# print(a.allocate())
# print(a.allocate())
# print(a.allocate())
# print(a.allocate())  # error
# a.release(2)
# assert a.release(10) == -1  # error
# print(a.allocate())  # 2

a = BinaryHeapAllocator(3)  # ids: 1,2,3
print(a.allocate())
print(a.allocate())
print(a.allocate())
print(a.allocate())  # error
a.release(2)
assert a.release(10) == -1  # error
print(a.allocate())  # 2
