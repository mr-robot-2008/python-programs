class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # compares first letter of all words, then moves to next letter
        s = ""
        if len(strs)==0: #edge case, no elements in list
            return s
        elif len(strs)==1: #edge case, single element in list
            return strs[0]

        #word length of shortest word to prevent index out of range
        for a in range(len(min(strs))): 
            #loops through each word in list, starting with second word
            for b in range(1, len(strs)): 
                #compares nth character of first word to other words
                if strs[0][a]==strs[b][a]: 
                    #only adds to pattern if nth character same up to the last word
                    if b==len(strs)-1: 
                        s += strs[0][a]
                else: #exits when characters don't match
                    return s
        return s