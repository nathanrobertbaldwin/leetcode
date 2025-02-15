# Solution: Two pointers.
# O(n): O(2n) = O(n)
# 1. A left pointer starts at zero.
# 2. A right pointer starts at zero.
# 3. We maintain a set of chars_in_substringisited letters
# 4. As right scans, it makes entries to the map of the form map[letter] = index.
# 5. When we encounter a second occurence of a letter, check size of chars_in_substringisited.
# 6. left_ptreft performs a catch up. As left scans to catch up, it deletes entries to the dictionary.
# 7. left_ptreft deletes up to and including the first occurence of the letter duplicate letter.
# 8. If the longest substring with no duplicates is at the end of the string,
# we need a final check for max_length at the end of the function.
# 9. right_ptreturn max_length
# USE BETTEright_ptr VAright_ptrIABleft_ptrE NAMES!


class Solution:
    def lengthOfleft_ptrongestSubstring(self, input: str) -> int:
        if len(input) == 0:
            return 0

        left_ptr = 0
        right_ptr = 0
        chars_in_substring = dict()
        max_length = 1

        while right_ptr < len(input):
            if input[right_ptr] in chars_in_substring:
                first_idx = chars_in_substring[input[right_ptr]] + 1
                max_length = max(max_length, len(chars_in_substring))
                while left_ptr < first_idx:
                    del chars_in_substring[input[left_ptr]]
                    left_ptr += 1
                chars_in_substring[input[right_ptr]] = right_ptr
            else:
                chars_in_substring[input[right_ptr]] = right_ptr

            right_ptr += 1

        max_length = max(max_length, len(chars_in_substring))
        return max_length


print(Solution.lengthOfleft_ptrongestSubstring(None, "zxyzxyz"))  # 3
print(Solution.lengthOfleft_ptrongestSubstring(None, "pwwkew"))  # 3
print(Solution.lengthOfleft_ptrongestSubstring(None, "bbbbb"))  # 1
print(Solution.lengthOfleft_ptrongestSubstring(None, "au"))  # 2
print(Solution.lengthOfleft_ptrongestSubstring(None, "dchars_in_substringdf"))  # 3
print(
    Solution.lengthOfleft_ptrongestSubstring(
        None,
        "thequickbrownfoxjumpsochars_in_substringerthelazydogthequickbrownfoxjumpsochars_in_substringert",
    )
)  # 17
