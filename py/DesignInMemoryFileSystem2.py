# Screen 90分钟 4 个part题 Code Signal 实现FileSystem class
# 我只记得大概:
# Part 1 - 基本create(path, size), get(path) -> size, delete(path)
# Ex:
# create("/a/b/c", 123)
# get("/a/b/c") -> 123

# Part 2 - 实现get_largest(k)-> largest k files
# Ex:
# create("/a/b/c", 10)
# create("/a/b/d", 20)
# create("/a/b/e", 30)
# get_largest(2) -> ["/a/b/c", "/a/b/d"]

# Part 3 - 每个file 有owner user， 每个user有总体storage capacity limit create/delete要track, limit per user在FileSystem初始化给 还要实现 merge(user1, user2)
# user1 limit = 11
# create("/a", "user1", 10)
# create("/b", "user1", 2) -> false (limit exceeded)
# create("/c", "user2", 10)
# merge("user1", "user2")
# get("/a") -> 10, "user1"
# get("/c") -> 10, "user1" (since user2 merged into user1)

# Part 4 - 实现backup(user)和restore(user)
# Ex:
# create("/a", "user1", 10)
# backup("user1")
# delete("/a")
# get("/a") -> -1
# restore("user1")

from collections import defaultdict


class File:
    def __init__(self, path: str, size: int, owner: str = None):
        self.path: str = path
        self.size: int = size
        self.owner: str = owner

    def __str__(self):
        return f"{self.path} - {self.size} - {self.owner}"


class FileSystem:
    def __init__(self, limit: int):
        self.files = defaultdict(File)
        self.userLimits = defaultdict(int)
        self.backupData = defaultdict(list[File])
        self.limit = limit

    def create(self, path, size, user):
        if not user in self.userLimits:
            self.userLimits[user] = self.limit

        if path in self.files or size < 0 or self.userLimits[user] < size:
            raise ValueError("invalid")
        self.files[path] = File(path, size, user)
        self.userLimits[user] -= size

    def get(self, path):
        if path not in self.files:
            return None
        return self.files[path]

    def delete(self, path: str):
        if not path in self.files:
            raise ValueError()
        deletedFile = self.files.pop(path)
        self.userLimits[deletedFile.owner] += deletedFile.size
        print(f"{deletedFile.owner} has {self.userLimits[deletedFile.owner]} limit")

    def getLargest(self, k: int):
        sizeArray = sorted(
            [(file.size, file.path) for file in self.files.values()], reverse=True
        )
        return sizeArray[:k]

    def merge(self, user1: str, user2: str):
        if user1 not in self.userLimits or user2 not in self.userLimits:
            return False
        for _, file in self.files.items():
            if file.owner == user2:
                file.owner = user1
                self.userLimits[user1] += file.size
        self.userLimits.pop(user2)

    def backup(self, user: str):
        if user not in self.userLimits:
            return False
        self.backupData[user] = [
            file for file in self.files.values() if file.owner == user
        ] + [self.userLimits[user]]

    def restore(self, user: str):
        if user not in self.backupData:
            raise ValueError("invalid")
        for file in self.files.values():
            if file.owner == user:
                self.files.pop(file.path)
        self.userLimits.pop(user)
        for file in self.backupData[user][:-1]:
            self.files[file.path] = file
        self.userLimits[user] = self.backupData[user][-1]
        self.backupData.pop(user)

        print([file.path for file in self.files.values() if file.owner == user])
        print(f"{user} has {self.userLimits[user]} limit")


fs = FileSystem(100)
fs.create("/a/b/c", 20, "user1")
fs.create("/a/b/d", 30, "user2")
fs.create("/a/b/e", 40, "user3")
try:
    fs.create("/a/b/f", 400, "user1")
except ValueError as e:
    print(e)
print(fs.get("/a/b/c"))
print(fs.getLargest(2))
fs.merge("user1", "user2")
print(fs.get("/a/b/d"))
fs.delete("/a/b/d")
fs.backup("user1")
print(fs.get("/a/b/c"))
fs.delete("/a/b/c")
print(fs.get("/a/b/c"))
fs.restore("user1")
