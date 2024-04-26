


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            i = ord(char) - ord('a')
            if current.children[i] is None:
                current.children[i] = Node()
            current = current.children[i]

        current.endOfWord = True

    def search(self, word: str) -> bool:
        current = self.root

        for char in word:
            i = ord(char) - ord('a')
            if current.children[i] is None:
                return False
            current = current.children[i]
        return current.endOfWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            i = ord(char) - ord('a')
            if current.children[i] is None:
                return False
            current = current.children[i]
        return True

    def print_nodes(self):
        self._print_nodes_recursive(self.root, "")

    def _print_nodes_recursive(self, node, prefix):
        if node.endOfWord:
            print(prefix)

        for i, child in enumerate(node.children):
            if child is not None:
                char = chr(ord('a') + i)
                self._print_nodes_recursive(child, prefix + char)


class Node:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.endOfWord = False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# Test the Trie implementation
def test_trie():
    trie = Trie()
    actions = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    values = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    expected_output = [None, None, True, False, True, None, True]

    for action, value, expected in zip(actions, values, expected_output):
        if action == "Trie":
            trie = Trie()
            print("Trie initialized.")
        elif action == "insert":
            trie.insert(*value)
            print(f"Inserted '{value[0]}' into Trie.")
        elif action == "search":
            result = trie.search(*value)
            print(f"Search for '{value[0]}': {result}. Expected: {expected}")
        elif action == "startsWith":
            result = trie.startsWith(*value)
            print(f"StartsWith '{value[0]}': {result}. Expected: {expected}")

    print("\nNodes in the Trie:")
    trie.print_nodes()

test_trie()

