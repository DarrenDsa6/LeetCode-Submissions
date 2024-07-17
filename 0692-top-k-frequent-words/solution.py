class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        my_dict = {}
        for i in words:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        sorted_dict = sorted(my_dict.items(), key=lambda item: (-item[1], item[0]))
        result = [word for word, count in sorted_dict[:k]]
        return result
