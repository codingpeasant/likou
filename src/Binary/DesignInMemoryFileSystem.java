package Binary;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// https://leetcode.ca/2017-07-10-588-Design-In-Memory-File-System/
class DesignInMemoryFileSystem {
    class Node {
        String path;
        boolean isFile;
        List<Node> children;

        public Node() {
            this("", false);
        }

        public Node(String path, boolean isFile) {
            this.path = path;
            this.isFile = isFile;
            if (!isFile)
                children = new ArrayList<>();
        }
    }

    Node root;
    Map<String, String> fileContentMap;

    public DesignInMemoryFileSystem() {
        root = new Node();
        fileContentMap = new HashMap<>();
    }

    public List<String> ls(String path) {
        String[] array = path.substring(1).split("/");
        Node node = root;
        int length = path.length() == 1 ? 0 : array.length;
        for (int i = 0; i < length; i++) {
            String subPath = array[i];
            int index = binarySearch(node.children, subPath);
            if (index >= 0)
                node = node.children.get(index);
            else
                return new ArrayList<>();
        }
        List<String> list = new ArrayList<>();
        if (node.isFile) {
            list.add(node.path);
        } else {
            List<Node> children = node.children;
            for (Node child : children) {
                list.add(child.path);
            }
        }
        return list;
    }

    public void mkdir(String path) {
        if (path.equals("/"))
            return;
        String[] array = path.substring(1).split("/");
        Node node = root;
        int length = array.length;
        for (int i = 0; i < length; i++) {
            String subPath = array[i];
            int index = binarySearch(node.children, subPath);
            if (index >= 0)
                node = node.children.get(index);
            else {
                Node newNode = new Node(subPath, false);
                node.children.add(-index - 1, newNode);
                node = newNode;
            }
        }
    }

    public void addContentToFile(String filePath, String content) {
        String[] array = filePath.substring(1).split("/");
        Node node = root;
        int length = array.length - 1;
        for (int i = 0; i < length; i++) {
            String subPath = array[i];
            int index = binarySearch(node.children, subPath);
            if (index >= 0)
                node = node.children.get(index);
            else {
                Node newNode = new Node(subPath, false);
                node.children.add(-index - 1, newNode);
                node = newNode;
            }
        }
        Node fileNode = new Node(array[length], true);
        int index = binarySearch(node.children, array[length]);
        if (index < 0)
            node.children.add(-index - 1, fileNode);
        String prevContent = fileContentMap.getOrDefault(filePath, "");
        String newContent = prevContent + content;
        fileContentMap.put(filePath, newContent);
    }

    public String readContentFromFile(String filePath) {
        return fileContentMap.getOrDefault(filePath, "");
    }

    private int binarySearch(List<Node> list, String key) {
        int low = 0, high = list.size() - 1;
        while (low <= high) {
            int mid = (high - low) / 2 + low;
            Node node = list.get(mid);
            if (node.path.equals(key))
                return mid;
            else if (node.path.compareTo(key) > 0)
                high = mid - 1;
            else
                low = mid + 1;
        }
        return -low - 1;
    }
}
