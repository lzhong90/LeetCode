class Trie:

    def __init__(self):
        self.dic = {}
        

    def insert(self, word: str) -> None:
        cur = self.dic
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True
                
        

    def search(self, word: str) -> bool:
        cur = self.dic
        for i in word:
            if i not in cur:
                return False
            cur = cur[i]
            
        if '#' in cur:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.dic
        for i in prefix:
            if i not in cur:
                return False
            cur = cur[i]
        return True
        
