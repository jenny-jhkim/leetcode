class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        hIndex = 0

        for i, c in enumerate(citations):
            if i+1 <= c:
                hIndex += 1
            else:
                break

        return hIndex

                