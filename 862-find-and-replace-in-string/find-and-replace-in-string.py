class Solution:
    # Time complexity: O(kl + n) and Space complexity: O(m+r), where l = avg len of source and r = len(new_s)
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replacement = {}
        for i in range(len(indices)):
            index = indices[i]
            source = sources[i]
            target = targets[i]

            s_part = s[index : index+len(source)]
            if s_part == source:
                replacement[index] = (source, target)

        new_s = []
        i = 0
        while i < len(s):
            if i not in replacement:
                new_s.append(s[i])
                i += 1
            else:
                source, target = replacement[i]
                new_s.append(target)
                i += len(source)

        return "".join(new_s)