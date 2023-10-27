class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counter):
            count = 0
            for tile in counter:
                if counter[tile] > 0:
                    counter[tile] -= 1
                    count += 1 + backtrack(counter)
                    counter[tile] += 1
            return count

        from collections import Counter
        counter = Counter(tiles)
        return backtrack(counter)
