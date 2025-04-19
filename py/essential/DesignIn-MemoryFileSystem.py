# https://leetcode.ca/2017-07-10-588-Design-In-Memory-File-System/
# Grind

from typing import List


class Trie:
    def __init__(self):
        self.name = None
        self.isFile = False
        self.content = []
        self.children = {}

    def insert(self, path: str, isFile: bool):
        node = self
        ps = path.split('/')
        for p in ps[1:]:
            if p not in node.children:
                node.children[p] = Trie()
            node = node.children[p]
        node.isFile = isFile
        if isFile:
            node.name = ps[-1] # the file name
        return node

    def search(self, path: str):
        node = self
        if path == '/':
            return node
        ps = path.split('/')
        for p in ps[1:]:
            if p not in node.children:
                return None
            node = node.children[p]
        return node

class FileSystem:
    def __init__(self):
        self.root = Trie()

    def ls(self, path: str) -> List[str]:
        node = self.root.search(path)
        if node is None:
            return []
        if node.isFile:
            return [node.name]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self.root.insert(path, False)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root.insert(filePath, True)
        node.content.append(content)

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root.search(filePath)
        return ''.join(node.content)
    
s=FileSystem()
s.mkdir("/a/b/c")
s.addContentToFile("/a/b/c/d.txt", "hello")
print(s.ls("/a/b/c")) # ["d.txt"]
print(s.readContentFromFile("/a/b/c/d.txt")) # "hello"
s.mkdir("/a/b/e")
print(s.ls("/a/b")) # ["c", "e"]
print(s.ls("/a")) # ["b"]
print(s.ls("/")) # ["a"]
s.addContentToFile("/a/b/c/d.txt", "hello1")
print(s.readContentFromFile("/a/b/c/d.txt")) # "hellohello1"