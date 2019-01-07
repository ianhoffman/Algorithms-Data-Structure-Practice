"""
Given a string, find the length of the longest substring without repeating characters.

"""


def longest_non_repeating_substring_brute_force(s):  # O(n^3)
    longest = 0
    for i, c1 in enumerate(s):
        subs = c1
        for c2 in s[i + 1:]:
            if c2 in subs:
                break
            subs += c2
        if len(subs) > longest:
            longest = len(subs)
    return longest


def longest_non_repeating_substring_optimized_1(s):  # O(n)
    longest = 0
    n = len(s)
    i, j = 0, 0
    seen = set()

    while i < n and j < n:
        if s[j] in seen:
            seen.remove(s[i])
            i += 1
        else:
            seen.add(s[j])
            j += 1
            longest = max(longest, j - i)

    return longest


def longest_non_repeating_substring_optimized_2(s):  # O(n)
    longest = 0
    i = 0
    char_to_index = {}

    for j, c in enumerate(s):
        if c in char_to_index:
            i = max(char_to_index[c], i)
        char_to_index[c] = j + 1
        longest = max(longest, j + 1 - i)

    return longest


if __name__ == '__main__':
    assert longest_non_repeating_substring_brute_force('abcabcbb') == 3
    assert longest_non_repeating_substring_brute_force('bbbbb') == 1
    assert longest_non_repeating_substring_brute_force('pwwkew') == 3
    assert longest_non_repeating_substring_brute_force(' ') == 1
    assert longest_non_repeating_substring_brute_force('aab') == 2
    assert longest_non_repeating_substring_brute_force('dvdf') == 3

    assert longest_non_repeating_substring_optimized_1('abcabcbb') == 3
    assert longest_non_repeating_substring_optimized_1('bbbbb') == 1
    assert longest_non_repeating_substring_optimized_1('pwwkew') == 3
    assert longest_non_repeating_substring_optimized_1(' ') == 1
    assert longest_non_repeating_substring_optimized_1('aab') == 2
    assert longest_non_repeating_substring_optimized_1('dvdf') == 3

    assert longest_non_repeating_substring_optimized_2('abcabcbb') == 3
    assert longest_non_repeating_substring_optimized_2('bbbbb') == 1
    assert longest_non_repeating_substring_optimized_2('pwwkew') == 3
    assert longest_non_repeating_substring_optimized_2(' ') == 1
    assert longest_non_repeating_substring_optimized_2('aab') == 2
    assert longest_non_repeating_substring_optimized_2('dvdf') == 3

