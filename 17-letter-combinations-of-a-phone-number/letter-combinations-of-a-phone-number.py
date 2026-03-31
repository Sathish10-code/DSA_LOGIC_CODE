class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneKeypad = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if not digits:
            return []
            
        # Start with a list containing an empty string
        combinations = [""] 

        for digit in digits:
            # Get the letters for the current digit
            letters = phoneKeypad[digit]
            # Generate new combinations by appending each letter to existing combinations
            combinations = [existing + letter for existing in combinations for letter in letters]

        return combinations