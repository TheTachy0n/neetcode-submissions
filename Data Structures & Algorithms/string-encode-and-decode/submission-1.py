class Solution:

    #to excrypt and decrypt a string using some logic
    '''
    The most efficient encoding and decoding algo
    use the string length and a hashtag before the string while encoding and decoding
    '''
    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res
    '''
    Encoding algorithm is fairly simple
    - create an empty string
    - for loop through the list
    - add the length of the word + hashtag + word itself to the empty string
    - return the string
    '''
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            j += 1
            word = s[j:j+length]
            res.append(word)
            i = j + length
        return res
    '''
    Decoding is a bit tricky
    - inorder to decode, set an empty list res,
    - set i = 0
    - while i is less than length of the string
    - set another pointer j equal to i and increment till the s[j] is equal to # -> this part is the lenght of the string
    - now after # the length of the word would be from j till j+lenght
    - append the word to the array
    - return the array
    '''
