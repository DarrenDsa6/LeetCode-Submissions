class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        neighbour_dict = collections.defaultdict(list)
        for word in wordList:
            for j in range (len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                neighbour_dict[pattern].append(word)
        visit = set([beginWord])
        queue = deque([beginWord])
        res = 1
        while queue:
            for i in range (len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neiword in neighbour_dict[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            queue.append(neiword)
            res += 1
        return 0
