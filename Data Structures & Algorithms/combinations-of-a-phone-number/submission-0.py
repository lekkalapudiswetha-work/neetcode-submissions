class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        numMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []

        def backtrack(digitIndex,curr):
            if digitIndex >= len(digits):
                if curr != '':
                    result.append(curr)
                return
            
            currDigit = digits[digitIndex]
            currStr = numMap[currDigit]
            for j in range(len(currStr)):
                backtrack(digitIndex+1,curr+currStr[j])
        
        backtrack(0,'')
        return result