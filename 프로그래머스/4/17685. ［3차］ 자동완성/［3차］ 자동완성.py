class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0  # 현재 노드를 포함하는 단어의 개수

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1  # 해당 접두사가 몇 번 등장했는지 카운트
    
    def find_min_length(self, word):
        node = self.root
        for i, char in enumerate(word):
            node = node.children[char]
            if node.count == 1:  # 처음으로 유일한 접두사가 나오면 그 길이를 반환
                return i + 1
        return len(word)  # 모든 접두사가 겹친다면 단어 길이 전체가 필요

def solution(words):
    trie = Trie()
    
    # 트라이에 모든 단어 삽입
    for word in words:
        trie.insert(word)
    
    # 최소 입력 길이 계산
    return sum(trie.find_min_length(word) for word in words)