class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        hIndex = 0

        for i, c in enumerate(citations):
            if i+1 <= c: #compare papers and current citations[i]
                hIndex += 1
            else:
                break

        return hIndex

                