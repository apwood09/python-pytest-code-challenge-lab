def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """
    if not s:
        return ""

    longest = ""

    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the substring 
        return s[left + 1 : right]

    for i in range(len(s)):
        # Odd length palindromes (e.g., "aba", center is 'b')
        p1 = expand_around_center(i, i)
        if len(p1) > len(longest):
            longest = p1

        # Even length palindromes (e.g., "abba", center is between 'b's)
        p2 = expand_around_center(i, i + 1)
        if len(p2) > len(longest):
            longest = p2

    return longest