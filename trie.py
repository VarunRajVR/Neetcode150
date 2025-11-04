#implement trie data structure
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur  =self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]= TrieNode()
            cur = cur.children[c]
        cur.end = True
        

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end
       

    def startsWith(self, prefix):
        cur =self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

#design add and search words data structure:
class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word):
        def dfs(j, node):
            cur = node  # Use the passed node
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # If the character is a dot, check all children recursively
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    # If the character is not in the current node's children, return False
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        # Call dfs starting from the root node
        return dfs(0, self.root)

#word search II:
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board, words) :
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        
        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] not in node.children or (r, c) in visit:
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)
