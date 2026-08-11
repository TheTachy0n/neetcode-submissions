class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Goal is to get the top k most frequently occuring nums
        '''
        Approach using Hashmaps(dictionaries)
        - create a count dictionary
        - iterate through the array and add one for every occurence of a number
        - sort the dictionary in the reverse order of the values
        - create an answer array and append the k key values of the dict to the array
        - return the array
        '''

        count = {}

        for num in nums:
            count[num] = count.get(num,0) + 1

        sorted_items = sorted(count.items(),key = lambda x:x[1], reverse = True)

        ans = []
        for i in range(k):
            ans.append(sorted_items[i][0])

        return ans