class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''Hashmap
        - create a hashmap
        - for every word in strings
        - set the key as the sorted array
        - now in groups keep the sorted list as the keys and append each word as the value
        - return the list of values only
        '''

        groups = {}
        for i in strs:
            key = "".join(sorted(i))
        
            if key not in groups:
                groups[key] = []

            groups[key].append(i)
        return list(groups.values())