class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # Time complexity: O(n log n) and Space complexity: O(n)
        if len(properties) < 2:
            return 0

        properties.sort(key=lambda property: (-property[0], property[1]))

        max_defense = weak_count = 0

        for attack, defense in properties:
            if defense < max_defense:
                weak_count += 1
            max_defense = max(max_defense, defense)

        return weak_count