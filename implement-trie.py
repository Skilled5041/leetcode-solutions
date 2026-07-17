class Trie:

    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word: str) -> None:
        self.insert_helper(word, 0)

    def insert_helper(self, word: str, index: int) -> None:
        # End of word
        if len(word) - 1 == index:
            self.children[word[index]] = Trie() if word[index] not in self.children else self.children[word[index]]
            self.children[word[index]].end = True
        else:
            self.children[word[index]] = Trie() if word[index] not in self.children else self.children[word[index]]
            self.children[word[index]].insert_helper(word, index + 1)

    def search(self, word: str) -> bool:
        return self.search_helper(word, 0)

    def search_helper(self, word: str, index: int) -> bool:
        if word[index] not in self.children:
            return False
        elif len(word) - 1 == index and self.children[word[index]].end:
            return True
        elif len(word) - 1 == index and not self.children[word[index]].end:
            return False
        else:
            return self.children[word[index]].search_helper(word, index + 1)

    def startsWith(self, prefix: str) -> bool:
        return self.starts_with_helper(prefix, 0)

    def starts_with_helper(self, prefix: str, index: int) -> bool:
        if prefix[index] not in self.children:
            return False
        elif len(prefix) - 1 == index and self.children[prefix[index]]:
            return True
        else:
            return self.children[prefix[index]].starts_with_helper(prefix, index + 1)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
