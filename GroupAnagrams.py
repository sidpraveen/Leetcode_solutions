def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new = defaultdict(list)
        for x in strs:
            sortedX = ''.join(sorted(x))
            new[sortedX].append(x)
        return list(new.values())