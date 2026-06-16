class Solution:

    def encode(self, strs: List[str]) -> str:

        return "".join(f"{len(s)}#{s}" for s in strs)
        
        # if len(strs) == 0 : 
        #     return '-1'

        # def convert_to_ascii(letter : str) -> str : 
        #     converted_letter = ord(letter) + 83
        #     return str(converted_letter)

        # encoded_string = ""

        # for i in range(len(strs)): 
        #     word = strs[i]
        #     for j in range(len(word)) : 
        #         encoded_letter = convert_to_ascii(word[j])
        #         encoded_string += encoded_letter
        #         if j != len(word) - 1 : 
        #             encoded_string += '%'
        #     if i != len(strs)-1:
        #         encoded_string += '^'

        # return encoded_string
            


    def decode(self, s: str) -> List[str]:

        # if s == '-1':
        #     return []

        # ans = []

        # decoded_str_list = s.split('^')  # O(n)

        # for decoded_word in decoded_str_list :
        #     if not decoded_word : 
        #         ans.append("")
        #         continue
        #     decoded_string = ""
        #     split_decoded_word_by_char = decoded_word.split("%")
        #     for num in split_decoded_word_by_char : 
        #         decoded_letter = chr(int(num) - 83) 
        #         decoded_string += decoded_letter
                
        #     ans.append(decoded_string)
        # return ans


        ans = []
        i = 0
        while i < len(s):
            j = s.index('#',i)
            length = int(s[i:j])
            word = s[j+1:length + j + 1]
            ans.append(word)
            i = length + j + 1

        return ans

        # time complexity -> O(n)
        # space complexity -> O(n)



